cmd_/root/kyoukofb.ko := ld -r -m elf_x86_64 -T ./scripts/module-common.lds --build-id  -o /root/kyoukofb.ko /root/kyoukofb.o /root/kyoukofb.mod.o
