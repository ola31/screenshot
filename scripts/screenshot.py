#!/usr/bin/env python
import rospy
import cv2
import numpy as np

from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

import pyautogui

bridge = CvBridge()

image_pub = rospy.Publisher("/screenshot/compressed", CompressedImage, queue_size = 1000)


def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz



    while not rospy.is_shutdown():
        global image_pub

        img = pyautogui.screenshot()
        open_cv_image = np.array(img)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        #im = cv2.resize(open_cv_image, (640, 480))

        msg = bridge.cv2_to_compressed_imgmsg(open_cv_image)
        image_pub.publish(msg)

        #cv2.imshow('frame', open_cv_image)
       # cv2.waitKey(1)
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        #cv2.destroyAllWindows()
        rate.sleep()

 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
