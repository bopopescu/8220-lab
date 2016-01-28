/*************************************************************************
	> File Name: user.c
	> Author: yitian li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 27 Jan 2016 06:43:20 PM EST
 ************************************************************************/

#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <math.h>
#include <linux/ioctl.h>
#include <sys/mman.h>
#include <sys/types.h>

#define GRAPHICS_ON 1
#define GRAPHICS_OFF 0
#define VMODE			_IOW(0xcc,0,unsigned long)
#define FIFO_QUEUE		_IOWR(0xcc,3,unsigned long)
#define FIFO_FLUSH		_IO(0xcc,4)

struct u_kyouko_device{
	unsigned int *u_control_base;
	unsigned int *u_framebuffer_base;
} kyouko3;

#define KYOUKO_CONTROL_SIZE (65535)
#define Device_RAM 0x0020

struct fifo_entry{
	unsigned int command;
	unsigned int value;
};

unsigned int U_READ_REG(unsigned int rgister){
	return (*(kyouko3.u_control_base+(rgister>>2)));
}

unsigned int U_WRITE_FB(unsigned int address, unsigned int value){
	*(kyouko3.u_framebuffer_base + address) = value;
}

int main()
{
	int fd;
	int result;
	unsigned int i;
	fd = open("/dev/kyouko3", O_RDWR);
	kyouko3.u_control_base = mmap(0, KYOUKO_CONTROL_SIZE, PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
	kyouko3.u_framebuffer_base = mmap(0, 1024*768*4, PROT_READ|PROT_WRITE,MAP_SHARED,fd,0x80000000);
	ioctl(fd, VMODE, GRAPHICS_ON);
	//printf("VMODE:%x\n",VMODE);
	for (i = 200*1024; i < 201*1024; ++i){
		U_WRITE_FB(i, 0xff0000);
	}
	struct fifo_entry entry;
	entry.command = 0x5010;
	entry.value = 0;
	ioctl(fd, FIFO_QUEUE, &entry);
	ioctl(fd, FIFO_FLUSH, 0);
	sleep();
	ioctl(fd, VMODE, GRAPHICS_OFF);
	close(fd);
	return 0;
}


