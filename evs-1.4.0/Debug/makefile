################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir.mk
-include vswitchd/subdir.mk
-include utilities/subdir.mk
-include tests/subdir.mk
-include ovsdb/subdir.mk
-include ofproto/subdir.mk
-include lib/subdir.mk
-include datapath/subdir.mk
-include datapath/linux/subdir.mk
-include datapath/linux/compat/subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: evs

# Tool invocations
evs: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C Linker'
	gcc  -o"evs" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(OBJS)$(C_DEPS)$(EXECUTABLES) evs
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
