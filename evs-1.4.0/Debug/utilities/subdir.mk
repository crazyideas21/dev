################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../utilities/nlmon.o \
../utilities/ovs-appctl.o \
../utilities/ovs-benchmark.o \
../utilities/ovs-controller.o \
../utilities/ovs-dpctl.o \
../utilities/ovs-ofctl.o \
../utilities/ovs-vlan-bug-workaround.o \
../utilities/ovs-vsctl.o 

C_SRCS += \
../utilities/nlmon.c \
../utilities/ovs-appctl.c \
../utilities/ovs-benchmark.c \
../utilities/ovs-controller.c \
../utilities/ovs-dpctl.c \
../utilities/ovs-ofctl.c \
../utilities/ovs-vlan-bug-workaround.c \
../utilities/ovs-vsctl.c 

OBJS += \
./utilities/nlmon.o \
./utilities/ovs-appctl.o \
./utilities/ovs-benchmark.o \
./utilities/ovs-controller.o \
./utilities/ovs-dpctl.o \
./utilities/ovs-ofctl.o \
./utilities/ovs-vlan-bug-workaround.o \
./utilities/ovs-vsctl.o 

C_DEPS += \
./utilities/nlmon.d \
./utilities/ovs-appctl.d \
./utilities/ovs-benchmark.d \
./utilities/ovs-controller.d \
./utilities/ovs-dpctl.d \
./utilities/ovs-ofctl.d \
./utilities/ovs-vlan-bug-workaround.d \
./utilities/ovs-vsctl.d 


# Each subdirectory must supply rules for building sources it contributes
utilities/%.o: ../utilities/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


