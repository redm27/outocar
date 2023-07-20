#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy, rospkg, time
import numpy, cv2, math
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Imu
from xycar_msgs.msg import xycar_motor
from cv_bridge import CvBridge
from tf.transformations import euler_from_quaternion

rospy.init_node('best_driver’)

rospy.Subscriber("/usb_cam/image_raw/", Image, cam_callback)
rospy.Subscriber('xycar_ultrasonic', Int32MultiArray, ultra_callback)
rospy.Subscriber("imu", Imu, imu_callback)
motor_publisher = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)


image = np.empty(shape=[0])
bridge = CvBridge() 

def cam_callback(data):
global image
image = bridge.imgmsg_to_cv2(data, "bgr8")


ultra_msg = [0,0,0,0,0,0,0,0]

def ultra_callback(data):
global ultra_msg
ultra_msg = data.data


imu_msg = None

def imu_callback(data):
global imu_msg, roll, pitch, yaw
imu_msg = [data.orientation.x, data.orientation.y, 
data.orientation.z, data.orientation.w]


motor_msg = xycar_motor()
motor_publisher = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

def car_drive(angle, speed):
motor_msg.angle = angle
motor_msg.speed = speed
motor_publisher.publish(motor_msg)
car_drive(30, 20)


while not rospy.is_shutdown():
...
if (image ...):
...
if (ultra_msg ...):
...
if (imu_msg ...):
...
...
car_drive(new_angle, new_speed)
...
