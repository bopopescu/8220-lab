/*************************************************************************
	> File Name: user.c
	> Author: Yitian Li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 09 Mar 2016 05:35:39 PM EST
 ************************************************************************/

#include<stdio.h>
#include <errno.h>
#include <sys/syscall.h>

#define deepsleep() syscall(328)  // ...or whatever number is next
int main()
{
	printf("goodnight, Irene\n");
 	deepsleep();
 	printf("oops ... woke up!\n");
}

