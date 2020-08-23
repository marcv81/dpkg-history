import lib.events


class History:
    """Reads and analyses the log events which resulted from user commands."""

    def __init__(self):
        self._read_events()
        self._find_last_installs()

    def _read_events(self):
        """Reads and chronologically sorts the log events."""

        events = [
            event
            for event in lib.events.all_events()
            if "Commandline" in event and "Requested-By" in event
        ]
        self.events = list(sorted(events, key=lambda event: event["Start-Date"]))

    def _find_last_installs(self):
        """Finds the last installation date for each package."""

        self.last_installs = {}
        for event in self.events:
            if "Install" in event:
                for package in event["Install"]:
                    self.last_installs[package["Name"]] = event["Start-Date"]

    def last_installed(self, package):
        """Returns the date the package was last installed."""

        if package in self.last_installs:
            return self.last_installs[package]

    def last_multiarch_installed(self, package):
        """Returns the date a package or its multi-arch variant was last installed."""

        dates = []
        if package in self.last_installs:
            dates.append(self.last_installs[package])
        name, arch = package.split(":", 1)
        if name + ":all" in self.last_installs:
            self.append(self.last_installs[name + ":all"])
        if len(dates) > 0:
            return max(dates)
