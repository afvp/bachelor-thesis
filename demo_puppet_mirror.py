import time

from sic_framework.devices.common_naoqi.naoqi_motion_streamer import NaoMotionStreamer,NaoJointAngles, StartStreaming, StopStreaming,NaoMotionStreamerConf

from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoMotion

from sic_framework.devices.common_naoqi.nao_motion import NaoMotion, NaoPostureRequest, NaoRestRequest, NaoMoveRequest, NaoMoveToRequest

def getOppositeAngles(angles):
    new_angles= []
    counter= 0
    one = 0.0
    two = 0.0
    three = 0.0
    four = 0.0
    five = 0.0
    six = 0.0
    for angle in angles:
        if (counter == 3):
            one = angle * -1
        elif counter == 4:
            two = angle * -1
        elif counter == 5:
            three = angle * -1
        elif counter == 6:
            four = angle * -1
        elif counter == 7 :
            five = angle
        elif counter == 2 :
            six = angle
        elif counter == 20:
            angle = six
        elif counter == 21:
            angle = one
        elif counter == 22:
            angle = two
        elif counter == 23:
            angle = three
        elif counter == 24:
            angle = four
        elif counter == 25:
            angle = five
        new_angles.append(angle)
        counter += 1

    return new_angles


def mirror_arms(motion_message):

    motion_message.angles = getOppositeAngles(motion_message.angles)

    consumer.send_message(motion_message)


conf = NaoMotionStreamerConf(samples_per_second=60, stiffness=0.6)
streamer = NaoMotionStreamer("192.168.0.210", conf=conf)
walking_counter = 0
streamer.request(StartStreaming(["Body"]))
consumer = NaoMotionStreamer("192.168.0.151")
streamer.register_callback(mirror_arms)
print("Ready")
time.sleep(30)
streamer.request(StopStreaming())
print(walking_counter)