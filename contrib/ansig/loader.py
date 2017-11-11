#!/usr/bin/env python

'''
See https://github.com/rudisimo/ansig for more information.
'''

from os import path
import ansig

if __name__ == '__main__':
    BASEDIR = path.abspath(path.dirname(__file__))
    ansig.load(filename=path.join(BASEDIR, 'config.ini'))
