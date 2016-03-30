#include <linux/linkage.h>
#include <linux/signal.h>
#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/wait.h>
#include <linux/sched.h>

SYSCALL_DEFINE2(smunch, int, pid, unsigned long, bit_pattern)
{
	
	struct task_struct *p;
	sigset_t signal;
	signal.sig[0]=bit_pattern;

	
	p = find_task_by_vpid(pid);
	if (!p)
	{
		printk(KERN_ALERT "Find Process PID failed!\n");
		return (-1);
	}
	
	if (thread_group_empty(p)!=1)
	{
		printk(KERN_ALERT "This is not Single Threaded!\n");
		return (-1);
	}

	//check if there is SIGKILL and is ZOMBIE:
	if (sigismember(&signal,SIGKILL)==1 && p->exit_state==EXIT_ZOMBIE)
	{
			//set_task_state(p, TASK_STOPPED);
			if (cmpxchg(&p->exit_state, EXIT_ZOMBIE, EXIT_DEAD)!= EXIT_ZOMBIE)
				return (0);
			release_task(p);
			return (0);
	}
	
	/*
	for(signum=0;signum<_NSIG;signum++)
	{
		if (sigismember(&signal, signum)==1)
		{
			sigaddset(&p->pending.signal,signum);
		}
	}*/
	p->pending.signal=signal;
	wake_up_process(p);
	//Check if it is in deepsleep,if in wake it up
	
	return (0);
}