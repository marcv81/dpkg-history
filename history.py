# Prints in chronological order the log events of the current user.
# Green packages are still installed, red packages are not.

import lib.history
import lib.pretty
import lib.status
import os

history = lib.history.UserHistory(os.getlogin(), os.getuid())
installed = lib.status.all_installed()

for event in history.events:
    lib.pretty.print_event(event, installed)
