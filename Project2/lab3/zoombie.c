/*************************************************************************
	> File Name: zoombie.c
	> Author: Yitian Li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 09 Mar 2016 05:36:52 PM EST
 ************************************************************************/

#include<stdio.h>
int main()
{
	int pid;
    switch(pid=fork()){
    case 0:
		printf("try to kill pid %d\n",getpid());
		exit(0);
	default:
		printf("without killing %d\n",getpid());
		while(1){
			sleep(20);
		}
	}
	return 0;
}
