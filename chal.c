#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// gcc -o chal chal.c -no-pie -static
int darling(){
	printf("\n================ FRANXX System Activated ================\n");
	printf("Activating Weapon System........................Done\n");
	sleep(1);
	printf("Activating shield protocols.....................Done\n");
	sleep(1);
	printf("Initializing core reactor.......................Done\n");
	sleep(1);
	printf("Engaging stealth mode...........................Done\n");
	sleep(1);
	printf("Scanning target area............................Done\n");
	sleep(1);
	printf("Deploying defense grid..........................Done\n");
	sleep(1);
	printf("Syncing combat units............................Done\n");
	sleep(1);
	printf("Loading mission parameters......................Done\n");
	sleep(1);

	int arr[11] = {0,1,2,3,4,5,6,7,8,9,10};
	int index = 0;
	printf("\n\nSelect login user > ");
	scanf("%d", &index);
	printf("User %x selected\n", arr[index]);
	printf("\nEnter login passcode > ");
	scanf("%d", &index);
	printf("Passcode %x selected\n", arr[index]);

	printf("Continuing process...\n");
}


int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);

	char input[0x30] = {};

	printf("\n==================== The Best Anime ====================\n");
    printf("What is my favorite anime > ");
    scanf("%[^\n]", input);
    if(strcmp(input, "Darling in the FRANXX") == 0){
        darling();
    }
    else{
        printf("I do not want to talk with you anymore!\n");
		exit(0);
    }

	printf("Write a 1000-word experience about Darling in the FRANXX > ");
	scanf("%s", input);
}