import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

rclpy.init()

node = Node('move_robot')

publisher = node.create_publisher(Twist, '/cmd_vel', 10)

msg = Twist()

print("Moving robot forward...")

start_time = time.time()

while time.time() - start_time < 5:

    msg.linear.x = 0.2
    msg.angular.z = 0.0

    publisher.publish(msg)

    rclpy.spin_once(node, timeout_sec=0.1)

# stop robot
msg.linear.x = 0.0
publisher.publish(msg)

print("Robot stopped.")

node.destroy_node()
rclpy.shutdown()
