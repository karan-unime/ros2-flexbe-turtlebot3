from flexbe_core import EventState
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from flexbe_core.proxy import ProxyPublisher


class StopRobotState(EventState):

    def __init__(self):
        super().__init__(outcomes=['done'])

        qos = QoSProfile(depth=10)
        self._pub = ProxyPublisher({'/cmd_vel': Twist}, qos)

    def execute(self, userdata):

        msg = Twist()

        self._pub.publish('/cmd_vel', msg)

        return 'done'
