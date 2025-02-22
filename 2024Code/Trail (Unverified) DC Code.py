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
motor_group_8_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
motor_group_8 = MotorGroup(motor_group_8_motor_a, motor_group_8_motor_b)

# Intake Motor
Intake = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)

# Pistons 
Piston1 = DigitalIn(brain.three_wire_port.a)
Piston2 = DigitalIn(brain.three_wire_port.b)



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



# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)

# Code for the X+B Motor Group ( the 2 5.5 motors)
            if remote_control_code_enabled:
            # check the buttonX/buttonB status
            # to control motor_group_8 
            if controller_1.buttonX.pressing():
                motor_group_8.spin(FORWARD)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif controller_1.buttonB.pressing():
                motor_group_8.spin(REVERSE)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif not controller_1_x_b_buttons_control_motors_stopped:
                motor_group_8.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_x_b_buttons_control_motors_stopped = True

    # Code for the r1+r2 buttons on controller 
            # to control motor_7
            if controller_1.buttonR1.pressing():
                Intake.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                Intake.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                Intake.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
    # Control for Piston 2 Group, L1+L2
            if controller_1.buttonL1.pressing():
                Intake.spin(FORWARD)
                Piston2.set(High)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                Piston2.set(Low)
                controller_1_left_shoulder_control_motors_stopped = False
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
    # Control for Piston 1 Group, Up+Down
        if remote_control_code_enabled:
            # check the buttonUp/buttonDown status
            # to control motor_1
            if controller_1.buttonUp.pressing():
                Piston1.set(High)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif controller_1.buttonDown.pressing():
                Piston1.set(Low)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif not controller_1_up_down_buttons_control_motors_stopped:
                motor_1.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_up_down_buttons_control_motors_stopped = True

        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

myVariable = 0

def when_started1():
    global myVariable
    pass

when_started1()

drivetrain.set_drive_velocity(100, PERCENT)
