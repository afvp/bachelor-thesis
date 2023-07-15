import time

from sic_framework.devices.common_naoqi.naoqi_motion_streamer import NaoMotionStreamer,NaoJointAngles, StartStreaming, StopStreaming,NaoMotionStreamerConf

from sic_framework.devices.common_naoqi.naoqi_motion_streamer import StartStreaming, StopStreaming, \
    NaoMotionStreamerConf

conf = NaoMotionStreamerConf(samples_per_second=60)

streamer = NaoMotionStreamer("192.168.0.210", conf=conf)


consumer = NaoMotionStreamer("192.168.0.151")
consumer.connect(streamer)

streamer.request(StartStreaming(["Body"]))

time.sleep(30)
print("Done")
streamer.request(StopStreaming())