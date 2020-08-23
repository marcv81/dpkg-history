# Prints in chronological order the log events of the current user.

import lib.installed
import lib.history
import lib.pretty
import os

history = lib.history.UserHistory(os.getlogin(), os.getuid())
installed = lib.installed.Installed()

for event in history.events:
    lib.pretty.print_event(event, installed)
