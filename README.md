# Intro

This tool helps to track the `.deb` packages installed/removed on a system. It displays the `apt` events history, and uses colors to show which packages are still installed.

# Setup

This tool relies on the `/var/log/apt/history.log` logs. Edit `/etc/logrotate.d/apt` and set rotate to 60 to keep the logs for 5 years.

# Usage

Show only the installation events that were not completely reverted.

    python3 installed.py

Show all the events.

    python3 history.py

## Colors

- Green: the package is still installed.
- Yellow: the multi-arch variant of the package is still installed.
- Red: the package is no longer installed.
