#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Piston1 = DigitalOut(brain.three_wire_port.a)

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_7 = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
"""
Code Header:
Date: November 14, 2024
Version: 1.5
Title: Drivetrain Test
Author: Shreyas Sharma
Team: E Team
Description: This code snippet configures the drivetrain for testing on a VEX V5 robot.

Note: Ensure that the remote_control_code_enabled variable is defined and the thread rc_auto_loop_thread_controller_1 is started for the controller task to run correctly.
"""



#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code

# Left Drive 
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
left_motor_c = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b, left_motor_c)

# Right Drive
right_motor_a = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
right_motor_b = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
right_motor_c = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b, right_motor_c)

drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)

# Twin 5.5w motors
motor_group_8_motor_a = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
motor_group_8_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
motor_group_8 = MotorGroup(motor_group_8_motor_a, motor_group_8_motor_b)

# Intake Motor
Intake = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)

# Pistons 
Piston1 = DigitalOut(brain.three_wire_port.a)


left_drive_smart.set_velocity(100, PERCENT)
right_drive_smart.set_velocity(100, PERCENT)
Intake.set_velocity(90, PERCENT)
motor_group_8.set_velocity(50, PERCENT)

while True:
    left_drive_smart.spin(FORWARD, controller_1.axis3.position(), VOLT)
    right_drive_smart.spin(FORWARD, controller_1.axis2.position(), VOLT)

    if (controller_1.buttonR1.pressing()):
        Intake.spin(REVERSE)
    elif (controller_1.buttonR2.pressing()):
        Intake.spin(FORWARD)
    else:
        Intake.stop()

    if (controller_1.buttonL1.pressing()):
        motor_group_8.spin(FORWARD)
    elif (controller_1.buttonL2.pressing()):
        motor_group_8.spin(REVERSE)
    else:
        motor_group_8.stop()
    
    if (controller_1.buttonUp.pressing()):
        Piston1.set(True)
    elif (controller_1.buttonDown.pressing()):
        Piston1.set(False)




