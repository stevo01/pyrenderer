#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""glog

common logging function
"""

import logging

logger = None


def logger_init(application_name, filename, level_file=logging.DEBUG, level_console=logging.DEBUG):
    global logger
    logger = logging.getLogger(application_name)
    logger.setLevel(level_console)

    filehandler = logging.FileHandler(filename)
    filehandler.setLevel(level_file)

    conhandler = logging.StreamHandler()
    conhandler.setLevel(level_console)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatter)
    conhandler.setFormatter(formatter)

    logger.addHandler(conhandler)
    logger.addHandler(filehandler)

    return logger


def GetLogger():
    global logger
    return logger
