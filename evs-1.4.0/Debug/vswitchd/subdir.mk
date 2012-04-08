################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../vswitchd/bridge.o \
../vswitchd/ovs-brcompatd.o \
../vswitchd/ovs-vswitchd.o \
../vswitchd/system-stats.o \
../vswitchd/vswitch-idl.o \
../vswitchd/xenserver.o 

C_SRCS += \
../vswitchd/bridge.c \
../vswitchd/ovs-brcompatd.c \
../vswitchd/ovs-vswitchd.c \
../vswitchd/system-stats.c \
../vswitchd/vswitch-idl.c \
../vswitchd/xenserver.c 

OBJS += \
./vswitchd/bridge.o \
./vswitchd/ovs-brcompatd.o \
./vswitchd/ovs-vswitchd.o \
./vswitchd/system-stats.o \
./vswitchd/vswitch-idl.o \
./vswitchd/xenserver.o 

C_DEPS += \
./vswitchd/bridge.d \
./vswitchd/ovs-brcompatd.d \
./vswitchd/ovs-vswitchd.d \
./vswitchd/system-stats.d \
./vswitchd/vswitch-idl.d \
./vswitchd/xenserver.d 


# Each subdirectory must supply rules for building sources it contributes
vswitchd/%.o: ../vswitchd/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


