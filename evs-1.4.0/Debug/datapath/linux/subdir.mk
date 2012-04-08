################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../datapath/linux/actions.o \
../datapath/linux/addrconf_core-openvswitch.o \
../datapath/linux/brcompat.o \
../datapath/linux/brcompat_mod.mod.o \
../datapath/linux/brcompat_mod.o \
../datapath/linux/checksum.o \
../datapath/linux/datapath.o \
../datapath/linux/dev-openvswitch.o \
../datapath/linux/dp_notify.o \
../datapath/linux/dp_sysfs_dp.o \
../datapath/linux/dp_sysfs_if.o \
../datapath/linux/flex_array.o \
../datapath/linux/flow.o \
../datapath/linux/genetlink-brcompat.o \
../datapath/linux/genetlink-openvswitch.o \
../datapath/linux/ip_output-openvswitch.o \
../datapath/linux/kmemdup.o \
../datapath/linux/netdevice.o \
../datapath/linux/openvswitch_mod.mod.o \
../datapath/linux/openvswitch_mod.o \
../datapath/linux/reciprocal_div.o \
../datapath/linux/skbuff-openvswitch.o \
../datapath/linux/time.o \
../datapath/linux/tunnel.o \
../datapath/linux/vlan.o \
../datapath/linux/vport-capwap.o \
../datapath/linux/vport-generic.o \
../datapath/linux/vport-gre.o \
../datapath/linux/vport-internal_dev.o \
../datapath/linux/vport-netdev.o \
../datapath/linux/vport-patch.o \
../datapath/linux/vport.o 

C_SRCS += \
../datapath/linux/brcompat_mod.mod.c \
../datapath/linux/openvswitch_mod.mod.c 

OBJS += \
./datapath/linux/brcompat_mod.mod.o \
./datapath/linux/openvswitch_mod.mod.o 

C_DEPS += \
./datapath/linux/brcompat_mod.mod.d \
./datapath/linux/openvswitch_mod.mod.d 


# Each subdirectory must supply rules for building sources it contributes
datapath/linux/%.o: ../datapath/linux/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


