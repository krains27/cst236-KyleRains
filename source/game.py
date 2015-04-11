"""
:mod:`source.Game` -- Game source code
==============================================

The following code will be used to describe the game that
is being played
"""
from kingdom import Kingdom
import logging

class Game(object):
    """
    Game being played

    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.__kingdom = Kingdom()
        self.done = False

    def check_perimeter(self):
        """
        Checks the kingdom perimeter for orcs

        :return: True if perimeter is breached
        :rtype: bool
        """
        if self.__kingdom.check_perimeter():
            self.logger.info('Perimeter Breached')

    def display_orcs_distance(self):
        """
        Displays all the orcs' distances

        :return: None
        """
        for orc in self.__kingdom.orcs:
            self.logger.info('Orc distance={}'.format(orc.distance))

    def display_orcs_velocity(self):
        """
        Displays all the orcs' velocities

        :return: None
        """
        for orc in self.__kingdom.orcs:
            self.logger.info('Orc velocity={}'.format(orc.velocity))

    def get_input(self):
        """
        Gets input from player

        :return: Input from player
        :rtype: string
        """
        return raw_input('Enter your command: ')

    def handle_command(self):
        """
        Handles user command
        :return: None
        """
        user_command = self.get_input()

        if user_command in self.commands.keys():
            self.commands[user_command](self)
        else:
            self.logger.warning('Invalid command')

    def set_alert_level(self, module, level):
        """
        Sets the log level of the given module

        :param module: Name of module to set log level to
        :type module: basestring

        :param level: Logger level
        :type level: logging.level

        :return: None
        """
        logging.getLogger(module).setLevel(level)

    def start(self):
        """
        Starts the defense game

        :return: None
        """
        self.logger.info('Game has started')

    def stop(self):
        """
        Stops the game

        :return: None
        """
        self.logger.info('Game has ended')

    commands = {'P': check_perimeter,
                'X': stop,
                'D': display_orcs_distance,
                'V': display_orcs_velocity}

