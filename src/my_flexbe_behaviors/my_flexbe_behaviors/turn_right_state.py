from flexbe_core import EventState
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from flexbe_core.proxy import ProxyPublisher


class TurnLeftState(EventState):

    def __init__(self, duration=3.0):
        super().__init__(outcomes=['done'])

        self._duration = duration
        self._start_time = None

        qos = QoSProfile(depth=10)
        self._pub = ProxyPublisher({'/cmd_vel': Twist}, qos)

    def execute(self, userdata):

        elapsed = self._node.get_clock().now().nanoseconds / 1e9 - self._start_time

        if elapsed >= self._duration:

            stop_msg = Twist()
            self._pub.publish('/cmd_vel', stop_msg)

            return 'done'

        msg = Twist()
        msg.angular.z = -0.5

        self._pub.publish('/cmd_vel', msg)

    def on_enter(self, userdata):

        self._start_time = self._node.get_clock().now().nanoseconds / 1e9
