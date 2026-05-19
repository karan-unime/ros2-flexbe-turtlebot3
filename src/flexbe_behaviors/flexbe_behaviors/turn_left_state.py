#!/usr/bin/env python3

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from geometry_msgs.msg import Twist


class TurnLeftState(EventState):
    """
    Turns TurtleBot3 left.

    -- duration  float  Seconds to turn

    <= done
    """

    def __init__(self, duration=3.0):
        super(TurnLeftState, self).__init__(
            outcomes=['done']
        )

        self._duration = duration
        self._elapsed = 0.0

        self._pub = ProxyPublisher({
            '/cmd_vel': Twist
        })

    def on_enter(self, userdata):

        Logger.loginfo(
            f'TurnLeft: {self._duration}s'
        )

        self._elapsed = 0.0

    def execute(self, userdata):

        self._elapsed += 0.1

        if self._elapsed >= self._duration:
            return 'done'

        msg = Twist()
        msg.angular.z = 0.5

        self._pub.publish('/cmd_vel', msg)

        return None

    def on_exit(self, userdata):

        self._pub.publish('/cmd_vel', Twist())

    def on_stop(self):

        self._pub.publish('/cmd_vel', Twist())
