from utils.glog import GetLogger
import subprocess
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def ExecuteCmdExt(_cmd, workingdir=None):
    outstr = ''
    cmd = _cmd  # .split()

    logger = GetLogger()
    logger.debug('ExecuteCmdExt: {}'.format(cmd))
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               cwd=workingdir)

    try:
        exitcode = process.wait(60.0 * 5)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return "timeout", -1

    for line in iter(process.stdout.readline, ' '):
        if(line == b''):
            break
        logger.debug("stdout: {}".format(line.rstrip().decode('utf-8', errors='ignore')))
        outstr += line.rstrip().decode('utf-8', errors='ignore') + "\n"

    for line in iter(process.stderr.readline, ' '):
        if(line == b''):
            break
        logger.debug("stderr: {}".format(line.rstrip().decode('utf-8', errors='ignore')))
        outstr += line.rstrip().decode('utf-8', errors='ignore') + "\n"

    return outstr, process.returncode
