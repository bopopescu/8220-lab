#include <linux/linkage.h>
#include <linux/signal.h>
#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/wait.h>
#include <linux/sched.h>


__sched sleep_on(wait_queue_head_t *q)
{
	unsigned long flags;
	wait_queue_t wait;

	init_waitqueue_entry(&wait, current);
	__set_current_state(TASK_UNINTERRUPTIBLE);
	spin_lock_irqsave(&q->lock, flags);
	__add_wait_queue(q, &wait);
	spin_unlock(&q->lock);
	schedule();
	spin_lock_irq(&q->lock);
	__remove_wait_queue(q, &wait);
	spin_unlock_irqrestore(&q->lock, flags);
	return ;
}

DECLARE_WAIT_QUEUE_HEAD(gone);

SYSCALL_DEFINE0(deepsleep)
{
	sleep_on(&gone);
}



extern unsigned long sum_of_services;
extern unsigned long sum_of_waits;
extern unsigned long num_of_requests_seen;
SYSCALL_DEFINE0(summary_init)
{
	sum_of_waits=0;
	sum_of_services=0;
	num_of_requests_seen=0;
	return (0);
}

SYSCALL_DEFINE0(summary_print)
{
	if (num_of_requests_seen)
	{
		printk(KERN_ALERT "Mean Service Time:%ld\nMean Wait Time:%ld\n",
			sum_of_services*1000/num_of_requests_seen,
			sum_of_waits*1000/num_of_requests_seen
		);
		return (0);
	}else
	{
		printk(KERN_ALERT "Number of Requests is ZERO!\n");
		return (-1);
	}	
}