"""
:mod:`source.Orc` -- Orc source code
==============================================

The following code will be used to describe the orcs that
will be attacking the fortress
"""
import logging
from common import orc_priority


class Orc(object):
    """
    Orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    logger = logging.getLogger(__name__)
    orc_id = 0

    def __init__(self, velocity=0, distance=0, type='Base'):
        Orc.orc_id += 1
        self.__velocity = velocity
        self.__distance = distance
        self.__type = type
        self.__id = Orc.orc_id
        self.__priority = 'HIGH'
        self.logger.info('Orc #{} created'.format(self.__id))

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
    def id(self):
        """
        Returns the id of the orc

        :return: Orc ID
        :rtype: int
        """
        return self.__id

    @property
    def orc_type(self):
        """
        Returns type of orc

        :return: Orc type
        :rtype: basestring
        """
        return self.__type

    @property
    def priority(self):
        """
        Returns the priority of the orc

        :return: Orc priority
        :rtype: basestring
        """
        return self.__priority

    @priority.setter
    def priority(self, pri):
        """
        Sets the priority of the orc

        :param pri: Orc priority
        :type pri: basestring

        :return: None
        """
        if pri in orc_priority:
            self.__priority = pri
            self.logger.info('Orc {} priority set to {}'.format(self.__id, pri))
        else:
            self.logger.warning('Invalid orc priority')

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


class StrongOrc(Orc):
    """
    Strong orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(StrongOrc, self).__init__(velocity=velocity, distance=distance, type='Strong')


class UglyOrc(Orc):
    """
    Ugle orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(UglyOrc, self).__init__(velocity=velocity, distance=distance, type='Ugly')


class StinkyOrc(Orc):
    """
    Stinky orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(StinkyOrc, self).__init__(velocity=velocity, distance=distance, type='Stinky')


class GiantOrc(Orc):
    """
    Giant orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(GiantOrc, self).__init__(velocity=velocity, distance=distance, type='Giant')


class WeakOrc(Orc):
    """
    Weak orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(WeakOrc, self).__init__(velocity=velocity, distance=distance, type='Weak')


class ZombieOrc(Orc):
    """
    Zombgie orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(ZombieOrc, self).__init__(velocity=velocity, distance=distance, type='Zombie')


class ArmoredOrc(Orc):
    """
    Armored orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(ArmoredOrc, self).__init__(velocity=velocity, distance=distance, type='Armored')


class FastOrc(Orc):
    """
    Fast orcs that will be attacking

    :param velocity: Orc velocity
    :type velocity: int

    :param distance: Orc distance
    :type distance: int
    """
    def __init__(self, velocity=0, distance=0):
        super(FastOrc, self).__init__(velocity=velocity, distance=distance, type='Fast')