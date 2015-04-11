"""
:mod:`source.Kingdom` -- Kingdom source code
==============================================

The following code will be used to describe the kingdom
that is being protected.
"""
import logging

class Kingdom(object):
    """
    Fortress that will be protected


    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.__orcs_attacking = []

    def add_orc(self, orcs):
        """
        Add a list of orcs to the list of attacking orcs

        :param orcs: Orcs to add
        :type orcs: list or tuple
        :return: None
        """
        for orc in orcs:
            self.__orcs_attacking.append(orc)
            self.logger.info('Orc spotted with velocity={} and distance={}'.format(orc.velocity,
                                                                                   orc.distance))

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

    @property
    def orcs(self):
        """
        Returns the list of orcs

        :return: List of orcs
        :rtype: List
        """
        return self.__orcs_attacking