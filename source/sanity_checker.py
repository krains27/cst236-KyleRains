import sys
import os

import logging
import inspect

"""
class_params should hold any expected class name as a key along with a list of valid
parameters as the value. Classes that do not require parameters should contain and empty
list
"""
class_params = {'FibSeqFinder': [],
                'Interface': [],
                'QA': ['test question', 'test answer']}

"""
func_params should hold any expected function name along with a list of valid parameters
as the value. Functions that do not require parameters should contain and empty
list
"""
func_params = {'feet_to_miles': [42],
               'get_fibonacci_seq': [1],
               'get_git_branch': [],
               'get_git_url': [],
               'get_other_users': [],
               'hal_20': []}

"""
method_params should hold any expected method name along with a list of
valid parameters as the value. Methods that do not require parameters
should contain and empty list
"""
method_params = {'ask': ['Who invented Python'],
                 'teach': [''],
                 'correct': [''],
                 '_Interface__add_answer': [''],
                 'stop': []}


class SanityChecker(object):
    """
    Provides a sanity check on all modules in a given directory.

    :param directory: The directory to start in
    :type directory: str
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(ch)

    def __init__(self, directory):
        self.dir_to_check = directory
        sys.path.append(os.path.abspath(self.dir_to_check))
        self.module_list = []
        self.class_list = []
        self.missed_methods = []

    def import_modules(self):
        """
        Attempts to import all modules in the given directory.

        :return: None
        :rtype: None
        """
        for py_file in os.listdir(self.dir_to_check):
            if py_file.endswith('.py') and '__init__.py' not in py_file:
                module = py_file[:-3]
                try:
                    globals()[module] = __import__(module)
                    self.module_list.append(module)
                    self.logger.info('Successfully imported ' + module)
                except ImportError as err:
                    self.logger.error('\nError while importing {}'.format(module))
                    self.logger.error(err.message + '\n')

    def instantiate_classes(self):
        """
        Attempts to instantiate each class in each module that was in the given directory

        :return: None
        :rtype: None
        """
        for mod in self.module_list:
            for name, obj in inspect.getmembers(sys.modules[mod]):
                if inspect.isclass(obj):
                    try:
                        self.class_list.append(obj(*class_params[name]))
                        self.logger.info('Successfully instantiated class ' + name)
                    except Exception as err:
                        self.logger.error('\nError while instantiating ' + name + ' from ' + mod + ' module')
                        self.logger.error('Exception: {}'.format(type(err)))
                        self.logger.error(err.message + '\n')

    def call_methods(self):
        """
        Attempts to call each method associated with each class that was found in all
        the modules in the directory.

        :return: None
        :rtype: None
        """
        for cls in self.class_list:
            for name, obj in inspect.getmembers(cls):
                if callable(obj) and name in method_params:
                    try:
                        obj(*method_params[name])
                        self.logger.info('Successfully called method ' + name)
                    except Exception as err:
                        self.logger.error('\nError while calling ' + name + ' from class ' + cls.__class__.__name__)
                        self.logger.error('Exception: {}'.format(type(err)))
                        self.logger.error('Exception message: ' + err.message + '\n')

    def call_functions(self):
        """
        Attepmts to call all the module level functions in each module that was found in
        the directory.

        :return: None
        :rtype: None
        """
        for mod in self.module_list:
            for name, obj in inspect.getmembers(sys.modules[mod]):
                if inspect.isfunction(obj):
                    try:
                        obj(*func_params[name])
                        self.logger.info('Successfully called function ' + name)
                    except Exception as err:
                        self.logger.error('\nError while calling ' + name + ' from module ' + mod)
                        self.logger.error('Exception: {}'.format(type(err)))
                        self.logger.error('Exception message: ' + err.message + '\n')

"""
A simple example on how to use the class
"""
if __name__ == '__main__':
    path = '.\Pytona'

    x = SanityChecker(directory=path)
    x.import_modules()
    x.instantiate_classes()
    x.call_functions()
    x.call_methods()