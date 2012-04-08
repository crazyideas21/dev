################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../datapath/linux/compat/addrconf_core-openvswitch.c \
../datapath/linux/compat/dev-openvswitch.c \
../datapath/linux/compat/flex_array.c \
../datapath/linux/compat/genetlink-brcompat.c \
../datapath/linux/compat/genetlink-openvswitch.c \
../datapath/linux/compat/ip_output-openvswitch.c \
../datapath/linux/compat/kmemdup.c \
../datapath/linux/compat/netdevice.c \
../datapath/linux/compat/reciprocal_div.c \
../datapath/linux/compat/skbuff-openvswitch.c \
../datapath/linux/compat/time.c 

OBJS += \
./datapath/linux/compat/addrconf_core-openvswitch.o \
./datapath/linux/compat/dev-openvswitch.o \
./datapath/linux/compat/flex_array.o \
./datapath/linux/compat/genetlink-brcompat.o \
./datapath/linux/compat/genetlink-openvswitch.o \
./datapath/linux/compat/ip_output-openvswitch.o \
./datapath/linux/compat/kmemdup.o \
./datapath/linux/compat/netdevice.o \
./datapath/linux/compat/reciprocal_div.o \
./datapath/linux/compat/skbuff-openvswitch.o \
./datapath/linux/compat/time.o 

C_DEPS += \
./datapath/linux/compat/addrconf_core-openvswitch.d \
./datapath/linux/compat/dev-openvswitch.d \
./datapath/linux/compat/flex_array.d \
./datapath/linux/compat/genetlink-brcompat.d \
./datapath/linux/compat/genetlink-openvswitch.d \
./datapath/linux/compat/ip_output-openvswitch.d \
./datapath/linux/compat/kmemdup.d \
./datapath/linux/compat/netdevice.d \
./datapath/linux/compat/reciprocal_div.d \
./datapath/linux/compat/skbuff-openvswitch.d \
./datapath/linux/compat/time.d 


# Each subdirectory must supply rules for building sources it contributes
datapath/linux/compat/%.o: ../datapath/linux/compat/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


