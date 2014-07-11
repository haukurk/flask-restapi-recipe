"""
 * Author: Lukasz Jachym
 * Date: 6/28/13
 * Time: 3:49 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
"""

import logbook


class LoggingSetup(object):
    """
    Base Logging setup class based on logbook.
    """
    format_string = None
    handlers = None

    def __init__(self, log_level, format_string=None):
        self.handlers = []
        self.log_level = log_level

        if not format_string:
            self.format_string = '[{record.time}]: {record.level_name} - {record.channel}: {record.message}'

    def add_handler(self, handler):
        self.handlers.append(handler)

    def add_stderr_log(self):
        stderr_handler = logbook.StderrHandler(level=self.log_level)
        stderr_handler.format_string = self.format_string
        stderr_handler.formatter

        self.add_handler(stderr_handler)

    def get_nested_setup(self):
        nested_log_setup = logbook.NestedSetup(self.handlers)

        return nested_log_setup

    def get_default_setup(self):

        self.add_stderr_log()

        return self.get_nested_setup()


class ProductionLoggingSetup(LoggingSetup):
    """
    Logging setup class for production, inherits Base Logging class LoggingSetup.
    """
    def __init__(self, log_level, filebased_log_path, format_string=None):
        super(ProductionLoggingSetup, self).__init__(log_level, format_string)

        self.filebased_log_path = filebased_log_path

    def add_filebased_log(self, filename):
        time_rotating_handler = logbook.TimedRotatingFileHandler(filename,
                                                                 date_format='%Y-%m-%d',
                                                                 format_string=self.format_string)
        self.add_handler(time_rotating_handler)

    def get_default_setup(self):
        super(ProductionLoggingSetup, self).get_default_setup()

        self.add_filebased_log(self.filebased_log_path)

        return self.get_nested_setup()
