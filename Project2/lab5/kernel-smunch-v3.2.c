#include <linux/linkage.h>
#include <linux/signal.h>
#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/wait.h>
#include <linux/sched.h>

SYSCALL_DEFINE2(smunch, int, pid, unsigned long, bit_pattern)
{
	
	struct task_struct *p;
	unsigned long flags;
	sigset_t signal;
	signal.sig[0]=bit_pattern;
	
	rcu_read_lock();
	p = pid_task(find_vpid(pid),PIDTYPE_PID);
	//p=find_task_by_vpid(pid);
	if (!p)
	{
		printk(KERN_ALERT "Find Process PID failed!\n");
		rcu_read_unlock();
		return (-1);
	}
	
	if (thread_group_empty(p)!=1 ||(p->ptrace & PT_SEIZED))
	{
		printk(KERN_ALERT "This is not Single or Traced!\n");
		rcu_read_unlock();
		return (-1);
	}

	//check if there is SIGKILL and is ZOMBIE:
	if (sigismember(&signal,SIGKILL)==1 && p->exit_state==EXIT_ZOMBIE)
	{
		release_task(p);
		rcu_read_unlock();
		return (0);
	}	
	
	//Load signal and Wake it up
	if (lock_task_sighand(p,&flags)){
		p->pending.signal=signal;
		wake_up_process(p);
		unlock_task_sighand(p,&flags);
	}
	rcu_read_unlock();
	return (0);
}