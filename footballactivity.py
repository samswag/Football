# GMT+1 10:00 pm
# Copyright (C) 2014, Samson Goddy <samsongoddy@hotmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
import os

import gtk
try:
    import gnash
except ImportError:
    import subprocess

from sugar.activity import activity

SWFNAME = 'Football.swf'

class FootballActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        try:
            view = gnash.View()
            view.props.uri = os.path.join(activity.get_bundle_path(), SWFNAME)
            self.set_canvas(view)
            view.show()

        except NameError:
            socket = gtk.Socket()
            self.set_canvas(socket)
            self.show_all()

            args = [
                'gnash', 
                '-x', str(socket.get_id()), 
                os.path.join(activity.get_bundle_path(), SWFNAME) 
            ]                    
            self._process = subprocess.Popen(args)
