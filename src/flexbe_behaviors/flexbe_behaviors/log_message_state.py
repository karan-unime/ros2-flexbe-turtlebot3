#!/usr/bin/env python3

from flexbe_core import EventState, Logger


class LogMessageState(EventState):
    """
    Logs a message once then exits immediately.

    -- message  str  Message to display

    <= done
    """

    def __init__(self, message='Hello from FlexBE'):
        super(LogMessageState, self).__init__(
            outcomes=['done']
        )

        self._message = message
        self._done = False

    def on_enter(self, userdata):
        Logger.loginfo(f'[LOG] {self._message}')
        self._done = True

    def execute(self, userdata):
        if self._done:
            return 'done'
        return None

    def on_exit(self, userdata):
        self._done = False
