from behave import given, when, then
import sys
import os
import StringIO
from nose import tools
sys.path.insert(0, os.path.abspath(".."))

from source.speed_calculator import SpeedCalculator


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