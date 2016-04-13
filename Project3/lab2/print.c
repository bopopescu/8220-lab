#include <stdio.h>
#include <sys/syscall.h>
#define sum_init syscall(327)
#define sum_print syscall(328)

int main()
{
	sum_print;
	
	return 0;
}
