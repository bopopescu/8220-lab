/*************************************************************************
	> File Name: user.c
	> Author: Yitian Li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 17 Feb 2016 04:50:04 PM EST
 ************************************************************************/

#include<stdio.h>
#define My_SysCall(arg) syscall(325,arg)
int main(){
	My_SysCall(5);
	return 0;
}
