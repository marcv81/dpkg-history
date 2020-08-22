import lib.events


class UserHistory:
    """Reads and analyses the log events for a user"""

    def __init__(self, login, id):
        self._read_events(login, id)
        self._find_last_events()

    def _read_events(self, login, id):
        """Reads and chronologically sorts the log events for a user."""

        user = "%s (%s)" % (login, id)
        events = [
            event
            for event in lib.events.all_events()
            if "Requested-By" in event and event["Requested-By"] == user
        ]
        self.events = list(sorted(events, key=lambda event: event["Start-Date"]))

    def _find_last_events(self):
        """Finds the last installation or removal for each package."""

        self.last_events = {}
        for event in self.events:
            for key in ["Install", "Remove", "Purge"]:
                if key in event:
                    for package in event[key]:
                        self.last_events[package["Name"]] = {
                            "Installed": key == "Install",
                            "Start-Date": event["Start-Date"],
                        }
