from behave import given, when, then
import sys
import os
import StringIO
from nose import tools
sys.path.insert(0, os.path.abspath(".."))

from source.speed_calculator import SpeedCalculator, PresetSpeeds


@given('a city text file')
def step_impl(context):
    context.file = StringIO.StringIO()
    context.file.write('Portland\nSeattle\nSalem')
    context.file.seek(0)
    context.cities = ['Portland', 'Seattle', 'Salem']


@when('the cities are read')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(context.file, 'city')


@then('my app should contain the cities read')
def step_impl(context):
    tools.eq_(context.speed_calc.cities, context.cities)


@given('a distance text file')
def step_impl(context):
    context.file = StringIO.StringIO()
    context.file.write('50\n217\n5')
    context.file.seek(0)
    context.distances = [50, 217, 5]


@when('the distances are read')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(context.file, 'distance')


@then('my app should contain the distances read')
def step_impl(context):
    tools.eq_(context.speed_calc.distances, context.distances)


@given('a speed text file')
def step_impl(context):
    context.file = StringIO.StringIO()
    context.file.write('100\n50\n15')
    context.file.seek(0)
    context.speeds = [100, 50, 15]


@when('the speeds are read')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(context.file, 'speed')


@then('my app should contain the speeds read')
def step_impl(context):
    tools.eq_(context.speed_calc.speeds, context.speeds)


@given('an estimated speed')
def step_impl(context):
    context.estimated_speed = 50


@when('estimated speed is selected')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.speed_calc.transfer_speed = context.estimated_speed


@then('estimated speed will be used in calculation')
def step_impl(context):
    tools.eq_(context.speed_calc.transfer_speed, context.estimated_speed)


@given('a size')
def step_impl(context):
    context.hdd_size = 100


@when('the size is 100')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.speed_calc.hdd_size = context.hdd_size


@then('the current hdd size should be 100')
def step_impl(context):
    tools.eq_(context.speed_calc.hdd_size, context.hdd_size)


@given('Seattle, 100 mb/sec and 100 GB of data')
def step_impl(context):
    city_file = StringIO.StringIO()
    city_file.write('Portland\nSeattle\nSalem')
    city_file.seek(0)
    distance_file = StringIO.StringIO()
    distance_file.write('50\n217\n5')
    distance_file.seek(0)

    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(city_file, 'city')
    context.speed_calc.read_file(distance_file, 'distance')

    context.speed_calc.city = 'Seattle'
    context.speed_calc.hdd_size = 100
    context.speed_calc.transfer_speed = 100


@when('time between traveling to Seattle and transferring are calculated')
def step_impl(context):
    context.result = context.speed_calc.determine_faster_method()


@then('transferring is faster')
def step_impl(context):
    tools.eq_(context.result, 'Transferring')


@given('Salem, 50 mb/sec and 500 GB of data')
def step_impl(context):
    city_file = StringIO.StringIO()
    city_file.write('Portland\nSeattle\nSalem')
    city_file.seek(0)
    distance_file = StringIO.StringIO()
    distance_file.write('50\n217\n5')
    distance_file.seek(0)

    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(city_file, 'city')
    context.speed_calc.read_file(distance_file, 'distance')
    context.speed_calc.city = 'Salem'
    context.speed_calc.hdd_size = 500
    context.speed_calc.transfer_speed = 50


@when('time between traveling to Salem and transferring are calculated')
def step_impl(context):
    context.result = context.speed_calc.determine_faster_method()


@then('driving is faster')
def step_impl(context):
    tools.eq_(context.result, 'Driving')


@given('Seattle, 100 mb/sec and 100 GB of data (difference)')
def step_impl(context):
    city_file = StringIO.StringIO()
    city_file.write('Portland\nSeattle\nSalem')
    city_file.seek(0)
    distance_file = StringIO.StringIO()
    distance_file.write('50\n217\n5')
    distance_file.seek(0)

    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(city_file, 'city')
    context.speed_calc.read_file(distance_file, 'distance')

    context.speed_calc.city = 'Seattle'
    context.speed_calc.hdd_size = 100
    context.speed_calc.transfer_speed = 100


@when('differnce between traveling to Seattle and transferring are calculated')
def step_impl(context):
    context.result = context.speed_calc.determine_time_difference()


@then('difference equals ~1.72 hours')
def step_impl(context):
    tools.assert_almost_equal(context.result, 1.72, 2)


@given('Porsche preset speed equals 100')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    tools.eq_(PresetSpeeds.PORSCHE, 100)

@when('Porsche preset selected')
def step_impl(context):
    context.speed_calc.driving_speed = PresetSpeeds.PORSCHE


@then('driving speed will be 100')
def step_impl(context):
    tools.eq_(context.speed_calc.driving_speed, 100)


@given('Bus preset speed equals 65')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    tools.eq_(PresetSpeeds.BUS, 65)

@when('Bus preset selected')
def step_impl(context):
    context.speed_calc.driving_speed = PresetSpeeds.BUS


@then('driving speed will be 65')
def step_impl(context):
    tools.eq_(context.speed_calc.driving_speed, 65)


@given('Cement Truck preset speed equals 55')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    tools.eq_(PresetSpeeds.CEMENT_TRUCK, 55)

@when('Cement Truck preset selected')
def step_impl(context):
    context.speed_calc.driving_speed = PresetSpeeds.CEMENT_TRUCK


@then('driving speed will be 55')
def step_impl(context):
    tools.eq_(context.speed_calc.driving_speed, 55)


@given('Swallow preset speed equals 10')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    tools.eq_(PresetSpeeds.SWALLOW, 10)

@when('Swallow preset selected')
def step_impl(context):
    context.speed_calc.driving_speed = PresetSpeeds.SWALLOW


@then('driving speed will be 10')
def step_impl(context):
    tools.eq_(context.speed_calc.driving_speed, 10)


@given('city not in list of cities')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    tools.assert_not_in('Klamath Falls', context.speed_calc.cities)

@when('city is entered')
def step_impl(context):
    context.speed_calc.city = 'Klamath Falls'


@then('city will be added to list of cities')
def step_impl(context):
    tools.assert_in('Klamath Falls', context.speed_calc.cities)


@given('city not in list of cities (file)')
def step_impl(context):
    context.write_file = StringIO.StringIO()

    context.speed_calc = SpeedCalculator()
    context.speed_calc.read_file(context.write_file, 'city')

    tools.assert_not_in('Klamath Falls', context.speed_calc.cities)

@when('city is entered (file)')
def step_impl(context):
    context.speed_calc.city = 'Klamath Falls'

@then('city will be written to city file')
def step_impl(context):
    context.write_file.seek(0)
    tools.eq_(context.write_file.buf, 'Klamath Falls\n')

@given('10 different cities')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.cities = ['Portland', 'Seattle', 'Los Angeles', 'San Diego', 'Las Vegas',
                      'Salem', 'Reno', 'Klamath Falls', 'Grants Pass', 'Chicago']

@when('cities are added to route')
def step_impl(context):
    for city in context.cities:
        context.speed_calc.add_to_route(city)

@then('cities will be saved in route')
def step_impl(context):
    tools.eq_(context.cities, context.speed_calc.route)


@given('a city')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.starting_city = 'Keizer'

@when('starting city is set to city')
def step_impl(context):
    context.speed_calc.starting_city = context.starting_city

@then('starting city will be given city')
def step_impl(context):
    tools.eq_(context.starting_city, context.speed_calc.starting_city)

@given('a latency')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.latency = 300

@when('transfer time is calculated')
def step_impl(context):
    context.speed_calc.hdd_size = 500
    context.speed_calc.transfer_speed = 100
    context.no_lat = context.speed_calc.calculate_transfer_time()

    context.speed_calc.latency = context.latency
    context.with_lat = context.speed_calc.calculate_transfer_time()

@then('the calculation will account for the latency')
def step_impl(context):
    tools.assert_not_equal(context.with_lat, context.no_lat)

@given('a hard drive speed')
def step_impl(context):
    context.speed_calc = SpeedCalculator()
    context.drive_speed = 10 ** -15

@when('transfer time is calculated (hdd)')
def step_impl(context):
    context.speed_calc.hdd_size = 500
    context.speed_calc.transfer_speed = 100
    context.no_affect = context.speed_calc.calculate_transfer_time()

    context.speed_calc.drive_speed = context.drive_speed
    context.affect = context.speed_calc.calculate_transfer_time()

@then('the calculation will account for the hard drive speed')
def step_impl(context):
    tools.assert_not_equal(context.affect, context.no_affect)
