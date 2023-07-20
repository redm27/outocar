import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Imu
from xycar_msgs.msg import xycar_motor
from cv_bridge import CvBridge

# 전역 변수 초기화
image = None
ultra_msg = [0, 0, 0, 0, 0, 0, 0, 0]
imu_msg = [0, 0, 0, 0]
bridge = CvBridge()

# ROS 노드 초기화
rospy.init_node('best_driver')

# ROS 토픽에 대한 콜백 함수 정의
def cam_callback(data):
    global image
    # ROS Image 메시지를 OpenCV 이미지로 변환
    image = bridge.imgmsg_to_cv2(data, "bgr8")
    
def ultra_callback(data):
    global ultra_msg
    ultra_msg = data.data
    
def imu_callback(data):
    global imu_msg
    imu_msg = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]

# ROS 노드에 카메라, 초음파 센서, IMU 센서에 대한 토픽(Subscribers) 등록
rospy.Subscriber("/usb_cam/image_raw/", Image, cam_callback)
rospy.Subscriber('xycar_ultrasonic', Int32MultiArray, ultra_callback)
rospy.Subscriber("imu", Imu, imu_callback)

# 모터 제어 함수 정의
def car_drive(angle, speed):
    motor_msg = xycar_motor()
    motor_msg.angle = angle
    motor_msg.speed = speed
    motor_publisher.publish(motor_msg)

# 모터 토픽(Publisher) 등록
motor_publisher = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

# 주행 로직 구현
while not rospy.is_shutdown():
    # 카메라 이미지 처리 로직
    if image is not None:
        # 이미지 처리 로직 작성 (예: 주차를 위한 객체 인식, 차선 인식 등)
        # 감지된 결과에 따라 new_angle, new_speed 결정

    # 초음파 센서 데이터 처리 로직
    if ultra_msg is not None:
        # 초음파 센서 데이터 활용하여 주행 로직 작성
        # 감지된 결과에 따라 new_angle, new_speed 결정

    # IMU 센서 데이터 처리 로직
    if imu_msg is not None:
        # IMU 센서 데이터 활용하여 주행 로직 작성
        # 감지된 결과에 따라 new_angle, new_speed 결정

    # 결정된 new_angle, new_speed로 자동차를 제어
    car_drive(new_angle, new_speed)
