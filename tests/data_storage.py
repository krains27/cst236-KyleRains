Performance_data = {}

def add_axes_title(key, x_axis_title, y_axis_title):
    """
    Sets the titles of the axes.

    :param key: Key of the data
    :type key: str

    :param x_axis_title: Title of the x axis
    :type x_axis_title: str

    :param y_axis_title: Title of the y axis
    :type y_axis_title: str

    :return: None
    :rtype: None
    """
    Performance_data[key].insert(0, [x_axis_title, y_axis_title])

def add_data(key, data_points):
    """
    Add X, Y data pair to Performance_data.

    :param key: Key of data
    :type key: str

    :param data_points: X, Y data point
    :type data_points: list

    :return: None
    :rtype: None
    """
    Performance_data[key].append(data_points)

def add_title(title):
    """
    Adds a title as an entry to the perfomance data table.

    :param title: Graph Title
    :type title: str

    :return: None
    :rtype: None
    """
    Performance_data[title] = []