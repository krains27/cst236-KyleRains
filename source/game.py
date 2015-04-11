"""
:mod:`source.Game` -- Game source code
==============================================

The following code will be used to describe the game that
is being played
"""
from kingdom import Kingdom
from common import unit_list
import logging

class Game(object):
    """
    Game being played

    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.__kingdom = Kingdom()
        self.__units = 'Imperial'


    def check_perimeter(self):
        """
        Checks the kingdom perimeter for orcs

        :return: True if perimeter is breached
        :rtype: bool
        """
        if self.__kingdom.check_perimeter():
            self.logger.info('Perimeter Breached')

    def display_commands(self):
        """
        Displays a list of commands

        :return: None
        """
        for command in self.command_docs:
            self.logger.info(command)

    def display_orcs_distance(self):
        """
        Displays all the orcs' distances

        :return: None
        """
        for orc in self.__kingdom.orcs:
            self.logger.info('Orc distance={} {}'.format(orc.distance,
                                                         unit_list[self.__units]))

    def display_orc_types(self):
        """
        Displays the type of orcs that are attacking

        :return: None
        """
        for orc in self.__kingdom.orcs:
            self.logger.info('Orc type: {}'.format(orc.orc_type))

    def display_orcs_velocity(self):
        """
        Displays all the orcs' velocities

        :return: None
        """
        for orc in self.__kingdom.orcs:
            self.logger.info('Orc velocity={} {}/HR'.format(orc.velocity,
                                                             unit_list[self.__units]))

    def get_orc(self, orc_id):
        """
        Finds an orc with specific id in list of orcs

        :param orc_id: ID to look for
        :type orc_id: int

        :return: Desired orc
        :rtype: source.Orc
        """

        for orc in self.__kingdom.orcs:
            if orc.id == orc_id:
                return orc

        self.logger.warning('Orc ID {} is an invalid ID'.format(orc_id))  # Fall through

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
        elif user_command[:2] == 'PR':
            self.set_priority(user_command[3:])
        else:
            self.logger.warning('Invalid command')

    def remove_orc(self):
        """
        Remove orc by id

        :return: None
        """
        orc_id = raw_input('Enter id of orc to remove: ')

        orc = self.get_orc(orc_id)

        if orc:
            self.__kingdom.remove_orc(orc)
            self.logger.info('Orc {} was removed'.format(orc_id))

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

    def set_priority(self, command_str):
        """
        Sets an orc's priority

        :param command_str: String to parse that contains ID and Priority
        :type command_str: basestring

        :return: None
        """
        parsed_command = str.split(command_str, ' ')

        if len(parsed_command) != 2:
            self.logger.warning('Invalid priority command')
        else:
            orc_id = int(parsed_command[0])
            orc_priority = parsed_command[1]

            orc = self.get_orc(orc_id)

            if orc:
                orc.priority = orc_priority

    def set_units(self):
        """
        Sets the type of units to display

        :return: None
        """
        units = raw_input('Enter unit type (Imperial, Metric, Nautical, Parsec): ')

        if units in unit_list.keys():
            self.__units = units
            self.__kingdom.units = units
        else:
            self.logger.warning('Invalid units entered')

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
                'V': display_orcs_velocity,
                'T': display_orc_types,
                'R': remove_orc,
                'U': set_units,
                '?': display_commands}

    command_docs = ['Command: P Desc: Check Perimeter',
                    'Command: X Desc: Stop Game',
                    'Command: D Desc: Display Orc Distance',
                    'Command: V Desc: Display Orc Velocity',
                    'Command: T Desc: Display Orc Types',
                    'Command: R Desc: Remove Orc By ID',
                    'Command: U Desc: Set Units',
                    'Command: PR [ID] [Priority] Desc: Sets orc with [ID] to [Priority]',
                    'Command: ? Desc: Display Commands']