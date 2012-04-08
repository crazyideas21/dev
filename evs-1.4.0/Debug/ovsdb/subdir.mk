################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
O_SRCS += \
../ovsdb/column.o \
../ovsdb/condition.o \
../ovsdb/execution.o \
../ovsdb/file.o \
../ovsdb/jsonrpc-server.o \
../ovsdb/log.o \
../ovsdb/mutation.o \
../ovsdb/ovsdb-client.o \
../ovsdb/ovsdb-server.o \
../ovsdb/ovsdb-tool.o \
../ovsdb/ovsdb.o \
../ovsdb/query.o \
../ovsdb/row.o \
../ovsdb/server.o \
../ovsdb/table.o \
../ovsdb/transaction.o \
../ovsdb/trigger.o 

C_SRCS += \
../ovsdb/column.c \
../ovsdb/condition.c \
../ovsdb/execution.c \
../ovsdb/file.c \
../ovsdb/jsonrpc-server.c \
../ovsdb/log.c \
../ovsdb/mutation.c \
../ovsdb/ovsdb-client.c \
../ovsdb/ovsdb-server.c \
../ovsdb/ovsdb-tool.c \
../ovsdb/ovsdb.c \
../ovsdb/query.c \
../ovsdb/row.c \
../ovsdb/server.c \
../ovsdb/table.c \
../ovsdb/transaction.c \
../ovsdb/trigger.c 

OBJS += \
./ovsdb/column.o \
./ovsdb/condition.o \
./ovsdb/execution.o \
./ovsdb/file.o \
./ovsdb/jsonrpc-server.o \
./ovsdb/log.o \
./ovsdb/mutation.o \
./ovsdb/ovsdb-client.o \
./ovsdb/ovsdb-server.o \
./ovsdb/ovsdb-tool.o \
./ovsdb/ovsdb.o \
./ovsdb/query.o \
./ovsdb/row.o \
./ovsdb/server.o \
./ovsdb/table.o \
./ovsdb/transaction.o \
./ovsdb/trigger.o 

C_DEPS += \
./ovsdb/column.d \
./ovsdb/condition.d \
./ovsdb/execution.d \
./ovsdb/file.d \
./ovsdb/jsonrpc-server.d \
./ovsdb/log.d \
./ovsdb/mutation.d \
./ovsdb/ovsdb-client.d \
./ovsdb/ovsdb-server.d \
./ovsdb/ovsdb-tool.d \
./ovsdb/ovsdb.d \
./ovsdb/query.d \
./ovsdb/row.d \
./ovsdb/server.d \
./ovsdb/table.d \
./ovsdb/transaction.d \
./ovsdb/trigger.d 


# Each subdirectory must supply rules for building sources it contributes
ovsdb/%.o: ../ovsdb/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/usr/src/linux-headers-2.6.38-11/include -I/usr/src/linux-headers-2.6.38-11/arch/x86/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


