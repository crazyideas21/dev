################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../ofproto/collectors.o \
../ofproto/connmgr.o \
../ofproto/fail-open.o \
../ofproto/in-band.o \
../ofproto/names.o \
../ofproto/netflow.o \
../ofproto/ofproto-dpif-sflow.o \
../ofproto/ofproto-dpif.o \
../ofproto/ofproto.o \
../ofproto/pinsched.o \
../ofproto/pktbuf.o 

C_SRCS += \
../ofproto/collectors.c \
../ofproto/connmgr.c \
../ofproto/fail-open.c \
../ofproto/in-band.c \
../ofproto/names.c \
../ofproto/netflow.c \
../ofproto/ofproto-dpif-sflow.c \
../ofproto/ofproto-dpif.c \
../ofproto/ofproto.c \
../ofproto/pinsched.c \
../ofproto/pktbuf.c 

OBJS += \
./ofproto/collectors.o \
./ofproto/connmgr.o \
./ofproto/fail-open.o \
./ofproto/in-band.o \
./ofproto/names.o \
./ofproto/netflow.o \
./ofproto/ofproto-dpif-sflow.o \
./ofproto/ofproto-dpif.o \
./ofproto/ofproto.o \
./ofproto/pinsched.o \
./ofproto/pktbuf.o 

C_DEPS += \
./ofproto/collectors.d \
./ofproto/connmgr.d \
./ofproto/fail-open.d \
./ofproto/in-band.d \
./ofproto/names.d \
./ofproto/netflow.d \
./ofproto/ofproto-dpif-sflow.d \
./ofproto/ofproto-dpif.d \
./ofproto/ofproto.d \
./ofproto/pinsched.d \
./ofproto/pktbuf.d 


# Each subdirectory must supply rules for building sources it contributes
ofproto/%.o: ../ofproto/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


