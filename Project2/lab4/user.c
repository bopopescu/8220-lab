/*************************************************************************
	> File Name: user.c
	> Author: Yitian Li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 17 Feb 2016 04:50:04 PM EST
 ************************************************************************/

#include<stdio.h>
#include<errno.h>
#include<sys/syscall.h>
#include<sys/signal.h>
#include<time.h>

void son()
{
	//int num;
	
	printf("child get SIGUSR1\n");
}

int main()
{
	int pid,ret;
	switch(pid=fork()){
		case 0:
			signal(SIGUSR1,son);
			while(1){
				printf("child is playing\n");
				sleep(1);
			}
			break;
		default :
			while(1){
				printf("parent is going to sleep!\n");
				sleep(3);
				printf("wake up, check on child\n\n");
				ret = kill(pid, SIGUSR1);
				printf("kill USR1 returned %d\n\n");
			}
	}
	return 0;
}
