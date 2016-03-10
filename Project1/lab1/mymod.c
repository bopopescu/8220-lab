#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/kernel_stat.h>
#include <linux/fs.h>
#include <linux/cdev.h>

MODULE_LICENSE("Proprietary");
MODULE_AUTHOR("Yitian Li");


int kyouko3_open(struct inode *inode, struct file *fp){

	printk(KERN_ALERT "Opening Kyouko3...");
	//fd=open("/dev/kyouko3", O_RDWR);

return 0;
}

int kyouko3_release(struct inode *inode, struct file *fp){

	printk(KERN_ALERT "Closing Kyouko3...");
	//fd=close(fd);

return 0;
}

struct file_operations kyouko3_fops = {
	.open= 		kyouko3_open,
	.release=	kyouko3_release,
	.owner=		THIS_MODULE
};
struct cdev whatever;
static int my_init_function(void)
{
	
	cdev_init(&whatever, &kyouko3_fops);
	cdev_add(&whatever, MKDEV(500,127),1);
	printk(KERN_ALERT "Initializing...");
	return 0;
}
static void  my_exit_function(void)
{
	//struct cdev whatever;
	cdev_del(&whatever);
	printk(KERN_ALERT "Exiting...");
	
}

module_init(my_init_function);
module_exit(my_exit_function);

