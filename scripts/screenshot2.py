#!/usr/bin/env python


import numpy as np
import cv2
import rospy

from std_msgs.msg import Bool
from std_msgs.msg import UInt16
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

import pyautogui

bridge = CvBridge()

#===================
NUC_NUM = 1
#NUC_NUM = 2
#==================

image_pub = rospy.Publisher("/screenshot/image_raw", Image, queue_size = 1)

def screenshot_listen():
    rospy.init_node('screenshot_node', anonymous=True)

    subscriber = rospy.Subscriber("/mission",UInt16, callback, queue_size = 1)

    rospy.spin()

def callback(data_):

    if (NUC_NUM==1 and data_.data == 1000) or (NUC_NUM==2 and data_.data == 2000):

        global image_pub

        img = pyautogui.screenshot()
        open_cv_image = np.array(img)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        #im = cv2.resize(open_cv_image, (640, 480))

        msg = bridge.cv2_to_imgmsg(open_cv_image,"bgr8")
        image_pub.publish(msg)



'''if __name__ == '__main__':
    main(sys.argv)'''

if __name__ == '__main__':
    screenshot_listen()
