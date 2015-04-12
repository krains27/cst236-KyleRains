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
        self.route = []
        self.__transfer_speed = 1
        self.__driving_speed = 55
        self.__hdd_size = 0
        self.__current_city = ''
        self.__starting_city = ''
        self.__latency = 0
        self.__drive_speed = 1.0
        self.file_hnd = None

    def add_to_route(self, city):
        """
        Adds city to current route

        :param city: City to add
        :type city: basestring

        :return: None
        """
        self.city = city
        self.route.append(city)

    def calculate_driving_time(self):
        """
        Calculates the time to drive hard drive

        :return: Time in hours
        :rtype: float
        """
        try:
            distance_index = self.cities.index(self.__current_city)
            driving_time = self.distances[distance_index] / float(self.__driving_speed)
        except ValueError:
            pass

        return driving_time

    def calculate_transfer_time(self):
        """
        Calculate time to transfer data

        :return: Time to transfer data in hours
        :rtype: float
        """
        transfer_time = (self.__hdd_size * 8 * 10 ** 9) / float((self.__transfer_speed * 10 ** 6))
        transfer_time += (self.__latency * 10 ** -3)
        time_hdd_speed = max(transfer_time, ((self.__hdd_size * 8 * 10 ** 9)/ float(self.__drive_speed * 10 ** 9)))
        time_hdd_speed /= 3600  # Convert to hours

        return time_hdd_speed

    def determine_faster_method(self):
        """
        Determines which is faster: driving or transferring

        :return: Either Driving or Transferring
        :rtype: basestring
        """
        driving_time = self.calculate_driving_time()

        transfer_time = self.calculate_transfer_time()

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
        driving_time = self.calculate_driving_time()

        transfer_time = self.calculate_transfer_time()

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
    def drive_speed(self):
        """
        Returns the drive speed

        :return: Drive speed
        :rtype: float
        """
        return self.__drive_speed

    @drive_speed.setter
    def drive_speed(self, speed):
        """
        Sets the drive speed

        :param speed: Drive speed
        :type speed: float

        :return: None
        """
        self.__drive_speed = speed

    @property
    def latency(self):
        """
        Return network latency

        :return: Network latency
        :rtype: int
        """
        return self.__latency

    @latency.setter
    def latency(self, lat):
        """
        Sets the network latency

        :param lat: Network latency
        :type lat: int

        :return: None
        """
        self.__latency = lat

    @property
    def starting_city(self):
        """
        Returns the starting city

        :return: Starting City
        :rtype: basestring
        """
        return self.__starting_city

    @starting_city.setter
    def starting_city(self, s_city):
        """
        Sets the starting city

        :param s_city: Starting city
        :type s_city: basestring

        :return: None
        """
        self.__starting_city = s_city

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