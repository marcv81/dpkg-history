import lib.status


class Installed:
    """Tracks the set of installed packages."""

    def __init__(self):
        self.installed = set(
            [
                package["Package"] + ":" + package["Architecture"]
                for package in lib.status.all_packages()
                if package["Status"] == "install ok installed"
            ]
        )

    def is_installed(self, package):
        """Returns if a package is installed."""

        return package in self.installed

    def is_multiarch_installed(self, package):
        """Returns if the multi-arch variant of a package is installed."""

        name, arch = package.split(":", 1)
        return name + ":all" in self.installed
