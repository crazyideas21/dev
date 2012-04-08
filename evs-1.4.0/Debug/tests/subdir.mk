################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../tests/idltest.o \
../tests/test-aes128.o \
../tests/test-bundle.o \
../tests/test-byte-order.o \
../tests/test-classifier.o \
../tests/test-csum.o \
../tests/test-file_name.o \
../tests/test-flows.o \
../tests/test-hash.o \
../tests/test-hmap.o \
../tests/test-json.o \
../tests/test-jsonrpc.o \
../tests/test-list.o \
../tests/test-lockfile.o \
../tests/test-multipath.o \
../tests/test-odp.o \
../tests/test-ovsdb.o \
../tests/test-packets.o \
../tests/test-random.o \
../tests/test-reconnect.o \
../tests/test-sha1.o \
../tests/test-stp.o \
../tests/test-strtok_r.o \
../tests/test-timeval.o \
../tests/test-type-props.o \
../tests/test-unix-socket.o \
../tests/test-util.o \
../tests/test-uuid.o \
../tests/test-vconn.o 

C_SRCS += \
../tests/idltest.c \
../tests/test-aes128.c \
../tests/test-bundle.c \
../tests/test-byte-order.c \
../tests/test-classifier.c \
../tests/test-csum.c \
../tests/test-file_name.c \
../tests/test-flows.c \
../tests/test-hash.c \
../tests/test-hmap.c \
../tests/test-json.c \
../tests/test-jsonrpc.c \
../tests/test-list.c \
../tests/test-lockfile.c \
../tests/test-multipath.c \
../tests/test-odp.c \
../tests/test-ovsdb.c \
../tests/test-packets.c \
../tests/test-random.c \
../tests/test-reconnect.c \
../tests/test-sha1.c \
../tests/test-stp.c \
../tests/test-strtok_r.c \
../tests/test-timeval.c \
../tests/test-type-props.c \
../tests/test-unix-socket.c \
../tests/test-util.c \
../tests/test-uuid.c \
../tests/test-vconn.c 

OBJS += \
./tests/idltest.o \
./tests/test-aes128.o \
./tests/test-bundle.o \
./tests/test-byte-order.o \
./tests/test-classifier.o \
./tests/test-csum.o \
./tests/test-file_name.o \
./tests/test-flows.o \
./tests/test-hash.o \
./tests/test-hmap.o \
./tests/test-json.o \
./tests/test-jsonrpc.o \
./tests/test-list.o \
./tests/test-lockfile.o \
./tests/test-multipath.o \
./tests/test-odp.o \
./tests/test-ovsdb.o \
./tests/test-packets.o \
./tests/test-random.o \
./tests/test-reconnect.o \
./tests/test-sha1.o \
./tests/test-stp.o \
./tests/test-strtok_r.o \
./tests/test-timeval.o \
./tests/test-type-props.o \
./tests/test-unix-socket.o \
./tests/test-util.o \
./tests/test-uuid.o \
./tests/test-vconn.o 

C_DEPS += \
./tests/idltest.d \
./tests/test-aes128.d \
./tests/test-bundle.d \
./tests/test-byte-order.d \
./tests/test-classifier.d \
./tests/test-csum.d \
./tests/test-file_name.d \
./tests/test-flows.d \
./tests/test-hash.d \
./tests/test-hmap.d \
./tests/test-json.d \
./tests/test-jsonrpc.d \
./tests/test-list.d \
./tests/test-lockfile.d \
./tests/test-multipath.d \
./tests/test-odp.d \
./tests/test-ovsdb.d \
./tests/test-packets.d \
./tests/test-random.d \
./tests/test-reconnect.d \
./tests/test-sha1.d \
./tests/test-stp.d \
./tests/test-strtok_r.d \
./tests/test-timeval.d \
./tests/test-type-props.d \
./tests/test-unix-socket.d \
./tests/test-util.d \
./tests/test-uuid.d \
./tests/test-vconn.d 


# Each subdirectory must supply rules for building sources it contributes
tests/%.o: ../tests/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


