# Intro

I do not know how to automatically remove an apt package and all its unused dependencies. This tool allows me to to see what dependencies were installed at the time I installed a package, and which ones are still installed. I use it to identify and remove the unused dependencies.

# Setup

This tool relies on the dpkg logs. Edit `/etc/logrotate.d/dpkg` and set rotate to 60 to keep the logs for 5 years.

# Usage

Show only the installation events that were not reverted.

    python3 installed.py

Show all the events.

    python3 history.py

## Colors

- Green: the package is still installed.
- Yellow: the multi-arch variant of the package is still installed.
- Red: the package is no longer installed.
