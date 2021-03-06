/*************************************************************************
	> File Name: user.c
	> Author: yitian li
	> Mail: yitianl@g.clemson.edu 
	> Created Time: Wed 27 Jan 2016 06:43:20 PM EST
*************************************************************************/

#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <math.h>
#include <sys/mman.h>
#include <linux/ioctl.h>
#include "register.h"

int fd;
struct u_kyouko_device{
	unsigned int *u_control_base;
	unsigned int *u_framebuffer_base;
} kyouko3;

#define KYOUKO_CONTROL_SIZE (65535)

struct f_entry{
	unsigned int command;
	unsigned int value;
};

struct f_entry entry;

unsigned int U_READ_REG(unsigned int rgister){
	return (*(kyouko3.u_control_base+(rgister>>2)));
}

void U_WRITE_FB(unsigned int pixel, unsigned int value){
	kyouko3.u_framebuffer_base[pixel] = value;
}

unsigned int float_to_uint(float v)
{
	return *(unsigned int *) &v; 
}

void ioctlQueue(unsigned int reg, unsigned int value)
{
	entry.command = reg;
	entry.value = value; 
	ioctl(fd, FIFO_QUEUE, &entry);
}

void draw_point(float* xyzw, float* rgba){
	ioctlQueue(Vertex_Coordinate, float_to_uint(xyzw[0]));
	ioctlQueue(Vertex_Color, float_to_uint(rgba[0]));
	ioctlQueue(Vertex_Coordinate+4, float_to_uint(xyzw[1]));
	ioctlQueue(Vertex_Color+4, float_to_uint(rgba[1]));
	ioctlQueue(Vertex_Coordinate+8, float_to_uint(xyzw[2]));
	ioctlQueue(Vertex_Color+8, float_to_uint(rgba[2]));
	ioctlQueue(Vertex_Coordinate+12, float_to_uint(xyzw[3]));
	ioctlQueue(Vertex_Color+12, float_to_uint(rgba[3]));
}
int main(){
	int result;
	unsigned int i;
	fd = open("/dev/kyouko3", O_RDWR);
	kyouko3.u_control_base = mmap(0, KYOUKO_CONTROL_SIZE, PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
	kyouko3.u_framebuffer_base = mmap(0, 1024*768*4, PROT_READ|PROT_WRITE,MAP_SHARED,fd,0x80000000);
	
	ioctl(fd, VMODE, GRAPHICS_ON);
	for (i = 200*1024; i < 201*1024; ++i){
		U_WRITE_FB(i, 0xff0000);
	}
	printf("address: %x\n", &entry);
	printf("user_queue: %x , %d\n", entry.command, entry.value);
	printf("sizeofentry: %d\n",sizeof(entry));
	
	ioctlQueue(Flush, 0x0);
	sleep(2);
	ioctlQueue(Command_Primitive, 1);
	
	float p1[4]={-0.5,-0.5,0.0,1.0};
	float c1[4]={1.0, 0.0, 0.0, 1.0};
	draw_point(p1, c1);
	ioctlQueue(Vertex_Emit, 0x0);
	
	float p2[4]={0.5,0.0,0.0,1.0};
	float c2[4]={1.0, 1.0, 0.0, 1.0};
	draw_point(p2, c2);
	ioctlQueue(Vertex_Emit, 0x0);
			
	float p3[4]={0.125,0.5,0.0,1.0};
	float c3[4]={1.0, 0.0, 1.0, 1.0};
	draw_point(p3, c3);
	ioctlQueue(Vertex_Emit, 0x0);
	ioctlQueue(Command_Primitive, 0x0);
	ioctlQueue(Flush, 0x0);
	sleep(2);
	
	ioctl(fd, FIFO_FLUSH);
	sleep(4);
	ioctl(fd, VMODE, GRAPHICS_OFF);
	
	close(fd);
	return 0;
}

