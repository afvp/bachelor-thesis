import time

from sic_framework.devices.common_naoqi.naoqi_motion_streamer import NaoMotionStreamer, NaoJointAngles, StartStreaming, \
    StopStreaming, NaoMotionStreamerConf

from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoMotion

from sic_framework.devices.common_naoqi.nao_motion import NaoMotion, NaoPostureRequest, NaoRestRequest, NaoMoveRequest, \
    NaoMoveToRequest


def regular(motion_message):
    global walking_counter_a
    global walking_counter_b
    angles = motion_message.angles
    print(motion_message.joints)
    print(angles)
    counter = 0
    value = 0.0
    for angle in angles:
        if (counter == 0):
            if angle >= 0.5 and angle <= 1.5:
                walking_counter_a = 0.0
                walking_counter_b = 0.2
            elif angle <= 0.5 and angle >= -0.5:
                walking_counter_a = 0.2
                walking_counter_b = 0.0
            elif angle <= -0.5 and angle >= -1.5:
                walking_counter_a = 0.0
                walking_counter_b = -0.2
        counter += 1


conf = NaoMotionStreamerConf(samples_per_second=60, stiffness=0.2)
streamer = NaoMotionStreamer("192.168.0.210", conf=conf)
walking_counter_a = 0.0
walking_counter_b = 0.0
streamer.request(StartStreaming(["Body"]))
streamer.register_callback(regular)
print("Ready")
time.sleep(10)
streamer.request(StopStreaming())

motion = NaoMotion(ip="192.168.0.151")
a = NaoPostureRequest("Stand", .3)

reply = motion.request(a)
c = NaoMoveToRequest(walking_counter_a, walking_counter_b, 0)
reply_a = motion.request(a)
reply_c = motion.request(c)
print("Done")

