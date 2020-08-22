# Prints in chronological order the installations of the current user that were not reverted.
# Green packages are still installed, red packages are not.

import lib.history
import lib.pretty
import lib.status
import os

history = lib.history.UserHistory(os.getlogin(), os.getuid())
installed = lib.status.all_installed()


def contains_last_install(event):
    """Returns true if the user did not remove at least one package installed in the event."""

    if "Install" not in event:
        return False
    for package in event["Install"]:
        last_event = history.last_events[package["Name"]]
        if last_event["Installed"] and last_event["Start-Date"] == event["Start-Date"]:
            return True
    return False


for event in history.events:
    if contains_last_install(event):
        lib.pretty.print_event(event, installed)
