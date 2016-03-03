/*************************************************************************
	> File Name: user.c
	> Author: Yitian Li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 17 Feb 2016 04:50:04 PM EST
 ************************************************************************/

#include<stdio.h>
#include<errno.h>
#include<sys/syscall.h>
#include<time.h>
#define My_SysCall(arg) syscall(325,arg)
struct tspec {
	time_t tv_sec;
	long tv_nsec;
};

int main(){
	int ret;
	unsigned long * systemtime;
	ret=My_SysCall(systemtime);
	printf("Kernel System Time is :%l\n",((struct tspec * ) systemtime)->tv_nsec);
	fprintf(stderr, "syscall returned %d\n");
	return 0;
}
