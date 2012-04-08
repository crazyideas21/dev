################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../datapath/actions.c \
../datapath/brcompat.c \
../datapath/checksum.c \
../datapath/datapath.c \
../datapath/dp_notify.c \
../datapath/dp_sysfs_dp.c \
../datapath/dp_sysfs_if.c \
../datapath/flow.c \
../datapath/tunnel.c \
../datapath/vlan.c \
../datapath/vport-capwap.c \
../datapath/vport-generic.c \
../datapath/vport-gre.c \
../datapath/vport-internal_dev.c \
../datapath/vport-netdev.c \
../datapath/vport-patch.c \
../datapath/vport.c 

OBJS += \
./datapath/actions.o \
./datapath/brcompat.o \
./datapath/checksum.o \
./datapath/datapath.o \
./datapath/dp_notify.o \
./datapath/dp_sysfs_dp.o \
./datapath/dp_sysfs_if.o \
./datapath/flow.o \
./datapath/tunnel.o \
./datapath/vlan.o \
./datapath/vport-capwap.o \
./datapath/vport-generic.o \
./datapath/vport-gre.o \
./datapath/vport-internal_dev.o \
./datapath/vport-netdev.o \
./datapath/vport-patch.o \
./datapath/vport.o 

C_DEPS += \
./datapath/actions.d \
./datapath/brcompat.d \
./datapath/checksum.d \
./datapath/datapath.d \
./datapath/dp_notify.d \
./datapath/dp_sysfs_dp.d \
./datapath/dp_sysfs_if.d \
./datapath/flow.d \
./datapath/tunnel.d \
./datapath/vlan.d \
./datapath/vport-capwap.d \
./datapath/vport-generic.d \
./datapath/vport-gre.d \
./datapath/vport-internal_dev.d \
./datapath/vport-netdev.d \
./datapath/vport-patch.d \
./datapath/vport.d 


# Each subdirectory must supply rules for building sources it contributes
datapath/%.o: ../datapath/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


