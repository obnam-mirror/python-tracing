#!/usr/bin/python
# Copyright (C) 2011  Lars Wirzenius <liw@liw.fi>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from distutils.core import setup, Extension

setup(name='tracing',
      version='0.2',
      author='Lars Wirzenius',
      author_email='liw@liw.fi',
      url='http://liw.fi/tracing/',
      description='debug log/trace messages',
      long_description='''\
This package provides a couple of functions for logging debug messages.
It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time.

This module provides a way to turn such debugging or tracing messages
on and off, based on the filename they occur in.
''',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: System :: Logging',
      ],
      py_modules=['tracing'],
     )
