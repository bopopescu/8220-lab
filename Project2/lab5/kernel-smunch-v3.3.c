#include <linux/linkage.h>
#include <linux/signal.h>
#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/wait.h>
#include <linux/sched.h>

SYSCALL_DEFINE2(smunch, int, pid, unsigned long, bit_pattern)
{
	unsigned long flags;
	sigset_t signal;
	struct task_struct *p= NULL;
	signal.sig[0]=bit_pattern;
	
	rcu_read_lock();
	p = pid_task(find_vpid(pid),PIDTYPE_PID);
	if (!p)
	{
		printk(KERN_ALERT "Find Process PID failed!\n");
		rcu_read_unlock();
		return (-1);
	}
	
	if (thread_group_empty(p)!=1 ||(p->ptrace & PT_SEIZED))
	{
		printk(KERN_ALERT "This is not Single Thread or Traced!\n");
		rcu_read_unlock();
		return (-1);
	}
	
	if (sigismember(&signal,SIGKILL)==1 && p->exit_state==EXIT_ZOMBIE)
	{
		if(cmpxchg(&p->exit_state, EXIT_ZOMBIE, EXIT_DEAD)!=EXIT_ZOMBIE)
		{
			rcu_read_unlock();
			return (-1);
		}
		release_task(p);
		printk(KERN_ALERT "Zombie:%d killed!\n",pid);
		rcu_read_unlock();
		return (0);
	}	
	
	if (lock_task_sighand(p,&flags)){
		p->pending.signal=signal;
		unlock_task_sighand(p,&flags);
	}
	wake_up_process(p);
	rcu_read_unlock();
	
	return (0);
}