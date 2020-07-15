import gzip
import os
import re


def all_events():
    """Iterates over all the logged events."""

    dirname = "/var/log/apt"
    for filename in os.listdir(dirname):
        if filename.startswith("history.log"):
            filename = "%s/%s" % (dirname, filename)
            yield from _events(_lines(filename))


def _events(lines):
    """Iterates over the events built from a lines iterator."""

    event = {}
    next(lines)
    for line in lines:
        if len(line) > 0:
            key, value = line.split(": ", 1)
            assert key not in event
            if key in ["Install", "Upgrade", "Remove", "Purge"]:
                value = list(_packages(value))
            event[key] = value
        else:
            assert len(event.keys()) > 0
            yield event
            event = {}
    assert len(event.keys()) > 0
    yield event


def _lines(filename):
    """Iterates over the lines of a plaintext or gzipped file."""

    if filename.endswith(".gz"):
        with gzip.open(filename) as stream:
            for line in stream:
                yield line.decode("utf-8").rstrip()
    else:
        with open(filename) as stream:
            for line in stream:
                yield line.rstrip()


def _packages(value):
    """Iterates over the packages represented by a text string."""

    regex = re.compile("([^ ]+?) \((.+?)\)")
    for match in regex.findall(value):
        yield {"Name": match[0], "Version": match[1]}
