#!/usr/bin/env python3

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyActionClient

from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
from action_msgs.msg import GoalStatus

import math


class NavigateToWaypointState(EventState):
    """
    Sends Nav2 navigation goal.

    -- goal_x     float
    -- goal_y     float
    -- goal_yaw   float

    <= arrived
    <= failed
    <= cancelled
    """

    def __init__(self,
                 goal_x=0.0,
                 goal_y=0.0,
                 goal_yaw=0.0):

        super(NavigateToWaypointState, self).__init__(
            outcomes=['arrived', 'failed', 'cancelled']
        )

        self._goal_x = goal_x
        self._goal_y = goal_y
        self._goal_yaw = goal_yaw

        self._topic = '/navigate_to_pose'

        self._client = ProxyActionClient({
            self._topic: NavigateToPose
        })

        self._goal_sent = False

    def on_enter(self, userdata):

        goal = NavigateToPose.Goal()

        goal.pose = PoseStamped()

        goal.pose.header.frame_id = 'map'

        goal.pose.pose.position.x = self._goal_x
        goal.pose.pose.position.y = self._goal_y

        goal.pose.pose.orientation.z = math.sin(
            self._goal_yaw / 2.0
        )

        goal.pose.pose.orientation.w = math.cos(
            self._goal_yaw / 2.0
        )

        try:

            self._client.send_goal(
                self._topic,
                goal
            )

            self._goal_sent = True

            Logger.loginfo(
                f'Goal sent: ({self._goal_x}, {self._goal_y})'
            )

        except Exception as e:

            Logger.logerr(
                f'Failed to send goal: {e}'
            )

            self._goal_sent = False

    def execute(self, userdata):

        if not self._goal_sent:
            return 'failed'

        if not self._client.has_result(self._topic):
            return None

        status = self._client.get_state(self._topic)

        if status == GoalStatus.STATUS_SUCCEEDED:

            Logger.loginfo('Goal reached')

            return 'arrived'

        elif status in [
            GoalStatus.STATUS_CANCELED,
            GoalStatus.STATUS_CANCELING
        ]:

            Logger.logwarn('Goal cancelled')

            return 'cancelled'

        else:

            Logger.logerr(
                f'Goal failed with status {status}'
            )

            return 'failed'

    def on_exit(self, userdata):

        if (
            self._goal_sent and
            not self._client.has_result(self._topic)
        ):

            self._client.cancel(self._topic)

    def on_stop(self):

        if (
            self._goal_sent and
            not self._client.has_result(self._topic)
        ):

            self._client.cancel(self._topic)
