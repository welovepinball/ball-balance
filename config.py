"""

SERVO_SPEED = float(servo_config_file.readline())

#check speed
if SERVO_SPEED<.5:
    SERVO_SPEED=.5
elif SERVO_SPEED>2.5:
    SERVO_SPEED=2.5

servo_config_file.close()

"""
