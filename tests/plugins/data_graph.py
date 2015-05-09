import matplotlib.pyplot as plt
import os
from nose2.events import Plugin
from tests.data_storage import Performance_data

class DataGraph(Plugin):
    configSection = 'data_graph'

    def stopTestRun(self, event):
        """
        Writes the requirment, description, and test run against requirement
        to req_output.txt when the test is done running

        :param event: Plugin event
        :type event: event

        :return: None
        """

        if not os.path.exists('DataGraphs'):
            os.makedirs('DataGraphs')

        for graph in Performance_data.keys():
            x_vals = []
            y_vals = []
            for data in Performance_data[graph][1:]:
                x_vals.append(data[0])
                y_vals.append(data[1])
            plt.plot(x_vals, y_vals)
            plt.title(graph)
            plt.xlabel(Performance_data[graph][0][0])
            plt.ylabel(Performance_data[graph][0][1])

            #save plot
            plt.savefig('DataGraphs/' + graph + '.png')
            plt.close()