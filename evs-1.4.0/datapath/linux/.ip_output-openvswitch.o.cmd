cmd_/root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.o := gcc -Wp,-MD,/root/dev/evs-1.4.0/datapath/linux/.ip_output-openvswitch.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/4.4.5/include -I/root/dev/evs-1.4.0/include -I/root/dev/evs-1.4.0/datapath/linux/compat -I/root/dev/evs-1.4.0/datapath/linux/compat/include  -I/usr/src/linux-headers-2.6.35-32-generic/arch/x86/include -Iinclude  -include include/generated/autoconf.h -Iubuntu/include  -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m64 -mtune=generic -mno-red-zone -mcmodel=kernel -funit-at-a-time -maccumulate-outgoing-args -fstack-protector -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -Wframe-larger-than=1024 -fno-omit-frame-pointer -fno-optimize-sibling-calls -pg -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DVERSION=\"1.4.0\" -I/root/dev/evs-1.4.0/datapath/linux/.. -I/root/dev/evs-1.4.0/datapath/linux/.. -DBUILDNR=\"\" -g -include /root/dev/evs-1.4.0/datapath/linux/kcompat.h  -DMODULE -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(ip_output_openvswitch)"  -D"KBUILD_MODNAME=KBUILD_STR(openvswitch_mod)"  -c -o /root/dev/evs-1.4.0/datapath/linux/.tmp_ip_output-openvswitch.o /root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.c

deps_/root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.o := \
  /root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.c \
  /root/dev/evs-1.4.0/datapath/linux/kcompat.h \
  include/linux/version.h \

/root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.o: $(deps_/root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.o)

$(deps_/root/dev/evs-1.4.0/datapath/linux/ip_output-openvswitch.o):
