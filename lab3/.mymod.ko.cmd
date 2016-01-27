cmd_/root/lab3/mymod.ko := ld -r -m elf_x86_64 -T ./scripts/module-common.lds --build-id  -o /root/lab3/mymod.ko /root/lab3/mymod.o /root/lab3/mymod.mod.o
