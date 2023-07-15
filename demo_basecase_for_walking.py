import time

from sic_framework.devices.common_naoqi.naoqi_motion_streamer import NaoMotionStreamer, NaoJointAngles, StartStreaming, \
    StopStreaming, NaoMotionStreamerConf

from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoMotion

from sic_framework.devices.common_naoqi.nao_motion import NaoMotion, NaoPostureRequest, NaoRestRequest, NaoMoveRequest, \
    NaoMoveToRequest

walking_counter_a = 0
walking_counter_b = 0
position = "CENTER"
t_end = time.time() + 10
t_start = time.time()
print("Choose a direction for the walk \n l -> left \n r -> right \n c -> center \n q -> to move the robot\n")
val = "none"
while val != "q" and time.time() < t_end:
    val = input("Current direction is " + position + ", input a new direction or press \"q\" to move""\n")
    if val in ['l', 'L']:
        if position == "CENTER":
            position = "LEFT"
        elif position == "RIGHT":
            position = "CENTER"
    elif val in ['r','R']:
        if position == "CENTER":
            position = "RIGHT"
        elif position == "LEFT":
            position = "CENTER"
    elif val in [ 'q']:
        pass
    else:
        print("Wrong input")

print("Moving the robot to the " + position)
if position == "LEFT":
    walking_counter_a = 0.0
    walking_counter_b = 0.2
elif position == "CENTER":
    walking_counter_a = 0.2
    walking_counter_b = 0.0
elif position == "RIGHT":
    walking_counter_a = 0.0
    walking_counter_b = -0.2


motion = NaoMotion(ip="192.168.0.151")
time.sleep(2)
a = NaoPostureRequest("Stand", .3)
reply = motion.request(a)
c = NaoMoveToRequest(walking_counter_a, walking_counter_b, 0)
reply_a = motion.request(a)
reply_c = motion.request(c)

