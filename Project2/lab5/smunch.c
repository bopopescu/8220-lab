/*************************************************************************
	> File Name: smunch.c
	> Author: Yitian Li
	> Mail: yitian@clemson.edu
	> Created Time: Tue 29 Mar 2016 10:27:12 PM EDT
 ************************************************************************/

#include <stdio.h>
#include <sys/syscall.h>
#define smunch(arg1,arg2) syscall(325,arg1,arg2)

int main(int argc, char* argv[])
{
	if (argc>1)
	{
		smunch(atoi(argv[1]),atoi(argv[2]));
		//kill(atoi)
	}
}
