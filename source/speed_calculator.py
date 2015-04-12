"""
:mod:`source.SpeedCalculator` -- Module that will compare transfer and driving
speed for data
==============================================================================

The following code will be used to calculate the speed of transferring and
driving data
"""


class PresetSpeeds(object):
    PORSCHE = 100
    BUS = 65
    CEMENT_TRUCK = 55
    SWALLOW = 10

    enum = {'PORSCHE': 100,
            'BUS': 65,
            'CEMENT_TRUCK': 55,
            'SWALLOW': 10}


class SpeedCalculator(object):
    def __init__(self):
        self.cities = []
        self.distances = []
        self.speeds = []
        self.__transfer_speed = 1
        self.__driving_speed = 55
        self.__hdd_size = 0
        self.__current_city = ''
        self.file_hnd = None

    def determine_faster_method(self):
        """
        Determines which is faster: driving or transferring

        :return: Either Driving or Transferring
        :rtype: basestring
        """
        try:
            distance_index = self.cities.index(self.__current_city)
            driving_time = self.distances[distance_index] / float(self.__driving_speed)
        except ValueError:
            pass

        transfer_time = (self.__hdd_size * 8 * 10 ** 9) / float((self.__transfer_speed * 10 ** 6))
        transfer_time /= 3600  # Convert to hours

        if transfer_time > driving_time:
            return 'Driving'
        else:
            return 'Transferring'

    def determine_time_difference(self):
        """
        Determines the difference in time between the 2 methods

        :return: Time difference
        :rtype: float
        """
        try:
            distance_index = self.cities.index(self.__current_city)
            driving_time = self.distances[distance_index] / float(self.__driving_speed)
        except ValueError:
            pass

        transfer_time = (self.__hdd_size * 8 * 10 ** 9) / float((self.__transfer_speed * 10 ** 6))
        transfer_time /= 3600  # Convert to hours

        return max(driving_time, transfer_time) - min(driving_time, transfer_time)

    def read_file(self, fhnd, type):
        """
        Read data from the passed in file handle

        :param fhnd: File handle
        :type fhnd: File object

        :param type: File type (city, distance, speed)
        :type type: basestring

        :return: None
        """
        self.file_hnd = fhnd
        lines = fhnd.read().splitlines()

        for line in lines:
            if type == 'city':
                self.cities.append(line)
            elif type == 'distance':
                self.distances.append(int(line))
            elif type == 'speed':
                self.speeds.append(int(line))

    @property
    def city(self):
        """
        Returns the current city

        :return: Current city
        :rtype: basestring
        """
        return self.__current_city

    @city.setter
    def city(self, city):
        """
        Sets the current city to travel to

        :param city: Current city
        :type city: basestring

        :return: None
        """
        if city not in self.cities:
            self.cities.append(city)

            if self.file_hnd:
                self.file_hnd.write(city + '\n')

        self.__current_city = city

    @property
    def transfer_speed(self):
        """
        Returns the current speed

        :return: Current speed
        :rtype: int
        """
        return self.__transfer_speed

    @transfer_speed.setter
    def transfer_speed(self, speed):
        """
        Sets the current speed

        :param speed: Current speed (mbps)
        :type speed: int

        :return: None
        """
        self.__transfer_speed = speed

    @property
    def hdd_size(self):
        """
        Returns the current hdd size

        :return: HDD size
        :rtype: int
        """
        return self.__hdd_size

    @hdd_size.setter
    def hdd_size(self, size):
        """
        Sets the current HDD size

        :param size: HDD size (GB)
        :type size: int

        :return: None
        """
        self.__hdd_size = size