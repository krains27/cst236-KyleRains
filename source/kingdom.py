"""
:mod:`source.Kingdom` -- Kingdom source code
==============================================

The following code will be used to describe the kingdom
that is being protected.
"""
import logging
from common import unit_list

class Kingdom(object):
    """
    Fortress that will be protected

    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.__orcs_attacking = []
        self.__units = 'Imperial'

    def add_orc(self, orcs):
        """
        Add a list of orcs to the list of attacking orcs

        :param orcs: Orcs to add
        :type orcs: list or tuple
        :return: None
        """
        for orc in orcs:
            self.__orcs_attacking.append(orc)
            self.logger.info('Orc spotted with velocity={} {}/HR and distance={} {}'.format(orc.velocity,
                                                                                              unit_list[self.__units],
                                                                                              orc.distance,
                                                                                              unit_list[self.__units]))

    def clear_orcs(self):
        """
        Clears orcs from kingdom

        :return: None
        """
        self.__orcs_attacking = []

    def check_perimeter(self):
        """
        Checks the list of attacking orcs to see if an orc has breached the
        perimeter
        :return: True if orc has breached, false if not
        :rtype: bool
        """
        for orc in self.__orcs_attacking:
            if orc.distance == 0:
                return True
        return False

    def remove_orc(self, orc):
        """
        Remove an orc from the list

        :param id: Orc ID
        :type id: int

        :return: None
        """
        self.__orcs_attacking.remove(orc)

    @property
    def orcs(self):
        """
        Returns the list of orcs

        :return: List of orcs
        :rtype: List
        """
        return self.__orcs_attacking

    @property
    def units(self):
        """
        Returns the current units

        :return: Current units
        :rtype: str
        """
        return self.__units

    @units.setter
    def units(self, units):
        """
        Sets the unit type

        :param units: Unit typs
        :type units: str

        :return: None
        """
        self.__units = units