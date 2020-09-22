from threading import Thread, Event
import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError


class ImageConverter:

    def __init__(self):
        self.brige = CvBridge()
        self.image_sub = rospy.Subscriber("/phone1/camera/image/compressed", CompressedImage, self.callback)
        self.cv_image = None

    def callback(self,data):
        try:
            self.cv_image = self.brige.compressed_imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)

def main():
    ic = ImageConverter()
    Thread(target=lambda: rospy.init_node("image_converter", disable_signals=True)).start()
    return ic.cv_image


if __name__ == '__main__':
    main()
