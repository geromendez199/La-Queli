#!/usr/bin/python3
# vim: ts=4:sw=4:expandtab

# LaQueli
# Copyright (C) 2008-2023 Andrew Ziem
# https://www.LaQueli.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Launcher
"""

import os
import sys


if 'posix' == os.name:
    if os.path.isdir('/usr/share/LaQueli'):
        # This path contains LaQueli/{C,G}LI.py .  This section is
        # unnecessary if installing LaQueli in site-packages.
        sys.path.append('/usr/share/')

    # The two imports from LaQueli must come after sys.path.append(..)
    import LaQueli.Unix
    from LaQueli import _

    if (
        LaQueli.Unix.is_display_protocol_wayland_and_root_not_allowed()
    ):
        print(_('To run a GUI application on Wayland with root, allow access with this command:\n'
              'xhost si:localuser:root\n'
                'See more about xhost at https://docs.LaQueli.org/doc/frequently-asked-questions.html'))
        sys.exit(1)

if os.name == 'nt':
    # change error handling to avoid popup with GTK 3
    # https://github.com/LaQueli/LaQueli/issues/651
    import win32api
    import win32con
    win32api.SetErrorMode(win32con.SEM_FAILCRITICALERRORS |
                          win32con.SEM_NOGPFAULTERRORBOX | win32con.SEM_NOOPENFILEERRORBOX)

if 1 == len(sys.argv):
    import LaQueli.GUI
    app = LaQueli.GUI.LaQueli()
    sys.exit(app.run(sys.argv))
else:
    import LaQueli.CLI
    LaQueli.CLI.process_cmd_line()
