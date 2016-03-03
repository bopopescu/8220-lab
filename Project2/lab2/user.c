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

#define My_SysCall(arg) syscall(325,arg)
#define init(arg)		syscall(326,arg)
#define get(arg)		syscall(327,arg)

void son()
{
	//int num;
	get(SIGUSR1);
	printf("child get SIGUSR1\n");
}
void test()
{
	printf("there\n");
}
int main()
{
	int pid,ret;
	switch(pid=fork()){
		case 0:
			signal(SIGUSR1,son);
			signal(SIGWINCH, test);
			printf("here\n");
			init(pid);
			while(1){
				printf("child is playing\n");
				sleep(1);
			}
			break;
		default :
			while(1){
				printf("parent is going to sleep!\n");
				sleep(10);
				printf("wake up, check on child\n\n");
				ret = kill(pid, SIGUSR1);
				printf("kill USR1 returned %d\n\n");
				ret = kill(pid, SIGSTOP);
				printf("kill SIGSTOP returned %d\n\n");
				ret = kill(pid, SIGCONT);
				printf("kill SIGCONT returned %d\n\n");
				ret = kill(pid, SIGWINCH);
				printf("kill SIGWINCH returned %d\n\n");
			}
	}
//	fprintf(stderr, "syscall returned %d\n");
	return 0;
}
