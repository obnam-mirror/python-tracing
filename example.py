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


import logging
import tracing


class Foo(object):

    def foo(self):
        self.bar()
        
    def bar(self):
        tracing.trace('this is output')

f = Foo()

logging.basicConfig(level=logging.DEBUG)
tracing.trace_add_pattern('example')
f.foo()
tracing.trace_clear_patterns()
f.foo()

