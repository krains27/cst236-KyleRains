from nose2.events import Plugin
from tests.ReqTracer import Requirements

class OutputReqs(Plugin):
    configSection = 'output_reqs'

    def stopTestRun(self, event):
        """
        Writes the requirment, description, and test run against requirement
        to req_output.txt when the test is done running

        :param event: Plugin event
        :type event: event

        :return: None
        """
        reqs = 0
        reqs_tested = 0
        with open('req_output.txt', 'w+') as f:
            for req in Requirements.keys():
                reqs += 1
                f.write('Requirement: ' + req + '\nDescription: ' + Requirements[req].req_text)
                f.write('Tests:\n')
                if Requirements[req].func_name:
                    reqs_tested += 1
                for a in Requirements[req].func_name:
                    f.write(a + '\n')
                f.write('\n\n')
            req_percent_str = str((float(reqs_tested)/float(reqs)) * 100)
            f.write('Requirement Coverage: ' + req_percent_str)