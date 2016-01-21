cmd_/root/lab2/mymod.ko := ld -r -m elf_x86_64 -T ./scripts/module-common.lds --build-id  -o /root/lab2/mymod.ko /root/lab2/mymod.o /root/lab2/mymod.mod.o
