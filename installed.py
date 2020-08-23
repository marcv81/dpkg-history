# Prints the installations that were not reverted in chronological order.

import lib.installed
import lib.history
import lib.pretty

history = lib.history.History()
installed = lib.installed.Installed()


def is_relevant(event):
    """Returns if the event is an installation that was not reverted.

    Returns true if the event installed at least one package which is still
    installed and which was not subsequently reinstalled."""

    if "Install" not in event:
        return False
    for package in event["Install"]:
        name = package["Name"]
        if (
            installed.is_installed(name)
            and history.last_installed(name) == event["Start-Date"]
        ):
            return True
        if (
            installed.is_multiarch_installed(name)
            and history.last_multiarch_installed(name) == event["Start-Date"]
        ):
            return True
    return False


for event in history.events:
    if is_relevant(event):
        lib.pretty.print_event(event, installed)
