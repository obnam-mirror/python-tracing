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
#
# =*= License: GPL-3+ =*=


''':mod:`tracing` -- fast debug trace messages
==================================

This module provides fast debugging log messages that can be
turned on and off during runtime.

It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time. Yet,
keeping the logging statements can be a good idea so that they can
be enabled if there is a problem that needs debugging, as long as
there is a way to disable them in normal production mode.

This module provides a way to achieve that. For example::

    # in the main program
    import tracing

    tracing.trace_add_pattern('foobar')
    tracing.trace_add_pattern('yeehaa')

    ...

    # in some other module
    tracing.trace('start procedure')
    tracing.trace('arg1=%s', arg1)
    tracing.trace('arg2=%s', arg2)

Only calls that happen in files whose names contain ``foobar`` or
``yeehaa`` will actually be logged. Pattern matching is based on
substring checking only, for speed, so there is no globbing or
regular expression matching.

'''

__version__ = '0.8'


import logging
import os
import traceback


trace_patterns = []
trace_cache = set()


def trace_add_pattern(pattern):
    '''Add a module name pattern.'''
    trace_patterns.append(pattern)


def trace_clear_patterns():
    '''Remove all module name patterns.

    After this, nothing will be traced. This is also the initial state.

    '''
    del trace_patterns[:]
    trace_cache.clear()


def trace(msg, *args):
    '''Log a trace message if the calling module's name matches a pattern.

    If any arguments are given, the message is formatted as if
    with ``msg % args``, otherwise the message is written out as is.

    '''

    if trace_patterns:
        frames = traceback.extract_stack(limit=2)
        filename, lineno, funcname, text = frames[0]
        log_it = filename in trace_cache
        if not log_it:
            for pattern in trace_patterns:
                if pattern in filename:
                    log_it = True
                    trace_cache.add(filename)
                    break
        if log_it:
            filename = os.path.basename(filename)
            if args:
                msg = msg % args
            logging.debug('%s:%s:%s: %s' % (filename, lineno, funcname, msg))
