green = "\x1b[92m"
yellow = "\x1b[93m"
red = "\x1b[91m"
end = "\x1b[0m"


def print_event(event, installed):
    """Prints a log event.

    Green packages are still installed. Yellow packages have their multi-arch
    variant still installed. Red packages are no longer installed."""

    date = " ".join(event["Start-Date"].split())
    print("[%s | %s] %s" % (date, event["Requested-By"], event["Commandline"]))
    for key in "Install", "Update", "Remove", "Purge":
        if key in event:
            packages = []
            for package in event[key]:
                packages.append(colorize_package(package["Name"], installed))
            print("%s: %s" % (key, " ".join(packages)))
    print()


def colorize_package(package, installed):
    """Colorize a package according to its installation status."""

    color = (
        green
        if installed.is_installed(package)
        else (yellow if installed.is_multiarch_installed(package) else red)
    )
    return color + package + end
