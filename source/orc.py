"""
:mod:`source.Orc` -- Orc source code
==============================================

The following code will be used to describe the orcs that
will be attacking the fortress
"""
import logging


class Orc(object):
    """
    Orcs that will be attacking

    """
    logger = logging.getLogger(__name__)

    def __init__(self, velocity=0, distance=0):

        self.__velocity = velocity
        self.__distance = distance
        self.logger.info('Orc created with velocity={} and distance={}'.format(velocity,
                                                                               distance))

    @property
    def distance(self):
        """
        Returns the distance of the orc

        :return: The distance of the orc
        :rtype: int
        """
        return self.__distance

    @distance.setter
    def distance(self, distance):
        """
        Sets the orc's distance

        :param distance: Orc's distance
        :type distance: int

        :return: None
        """
        self.__distance = distance

    @property
    def velocity(self):
        """
        Returns the orc's velocity

        :return: Orc's velocity
        :rtype: int
        """
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        """
        Sets the orc's velocity

        :param velocity: Orc's velocity
        :type velocity: int

        :return: None
        """
        self.__velocity = velocity
