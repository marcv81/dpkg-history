# Prints the log events in chronological order.

import lib.installed
import lib.history
import lib.pretty

history = lib.history.History()
installed = lib.installed.Installed()

for event in history.events:
    lib.pretty.print_event(event, installed)
