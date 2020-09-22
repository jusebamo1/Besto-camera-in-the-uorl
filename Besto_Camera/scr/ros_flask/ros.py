import rospy
import time, cv2
from threading import Thread, Event
from sensor_msgs.msg import Illuminance, Imu, MagneticField, CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist

class RosSensors:
    def __init__(self):
        Thread(target=lambda: rospy.init_node('ros_flask', disable_signals=True)).start()
        #self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        #self.cmd = Twist()
        self.illuminance_sub = rospy.Subscriber(
            '/phone1/android/illuminance', Illuminance, self.illuminance_callback, queue_size=1)
        self.imu_sub = rospy.Subscriber(
            '/phone1/android/imu', Imu, self.imu_callback, queue_size=1)
        self.magnetic_field_sub = rospy.Subscriber(
            '/phone1/android/magnetic_field', MagneticField, self.magnetic_field_callback, queue_size=1)
        self.brige = CvBridge()

    def __getattr__(self, item):
        return "Sensor Disconnected"

    def Publish(self, linear_x, angular_z):
        global cmd
        global vel_pub
        self,cmd.linear.x = linear_x
        self.cmd.angular.z = angular_z
        self.vel_pub.publish(cmd)

    def illuminance_callback(self, data):
        self.illu_data = data.illuminance
        self.Publicar(0.0, 0.0)
        time.sleep(1)

    def imu_callback(self, data):
        self.imu_data_ox = round(data.orientation.x, 10)
        self.imu_data_oy = round(data.orientation.y, 10)
        self.imu_data_oz = round(data.orientation.z, 10)
        self.imu_data_avx = round(data.angular_velocity.x, 10)
        self.imu_data_avy = round(data.angular_velocity.y, 10)
        self.imu_data_avz = round(data.angular_velocity.z, 10)
        self.imu_data_lax = round(data.linear_acceleration.x, 10)
        self.imu_data_lay = round(data.linear_acceleration.y, 10)
        self.imu_data_laz = round(data.linear_acceleration.z, 10)
        time.sleep(1)

    def magnetic_field_callback(self, data):
        self.mfx = data.magnetic_field.x * 1000
        self.mfy = data.magnetic_field.y * 1000
        self.mfz = data.magnetic_field.z * 1000
        time.sleep(1)

    def Publicar(self, linear_x, angular_z):
        self.cmd.linear.x = linear_x
        self.cmd.angular.z = angular_z
        self.vel_pub.publish(self.cmd)
