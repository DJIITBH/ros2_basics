#!/usr/bin/env python3 
#interpreter line this is
import rclpy #python library of ros2
from rclpy.node import Node

class MyNode(Node): #inherits node from ros2    
    def __init__(self):
        super().__init__("first_node") #call the super constructor for the Node class and initialize your node name here
        self.get_logger().info("hello chutiye! ros2 seekh liyo!")
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("samjha?")

def main(args = None):
    rclpy.init(args = args)
    #write code here
    node = MyNode()
    rclpy.spin(node)#this will ensure that your node runs indefinitely until and unless it is killed  and will call the callbacks
    rclpy.shutdown()

if __name__ == '__main__':
    main()
