#include <stdio.h>
#include <sys/syscall.h>
#define sum_init syscall(327)
#define sum_print syscall(328)

int main()
{
	sum_init;
	while(1)
	{
		sum_print;		
		sleep(1);
	}
	return 0;
}
