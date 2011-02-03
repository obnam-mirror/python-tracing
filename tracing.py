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


'''Python debubbing log messages.

This module provides a couple of functions for logging debug messages.
It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time.

This module provides a way to turn such debugging or tracing messages
on and off, based on the filename they occur in. For example:

    import tracing
    
    tracing.trace_add_pattern('foobar')
    tracing.trace_add_pattern('yeehaa')
    
    ...
    
    tracing.trace('start procedure')
    tracing.trace('arg1=%s' % arg1)
    tracing.trace('arg2=%s' % arg2)
    
Only calls that happen in files whose names contain 'foobar' or
'yeehaa' will actually be logged. Pattern matching is based on
substring checking only, no globbing or regexps, sorry.

'''


import logging
import os
import traceback


trace_patterns = []


def trace_add_pattern(pattern):
    trace_patterns.append(pattern)
    
    
def trace_clear_patterns():
    del trace_patterns[:]


def trace(msg):
    if trace_patterns:
        frames = traceback.extract_stack(limit=2)
        filename, lineno, funcname, text = frames[0]
        filename = os.path.basename(filename)
        for pattern in trace_patterns:
            if pattern in filename:
                logging.debug('%s:%s:%s: %s' % 
                              (filename, lineno, funcname, msg))
                break

