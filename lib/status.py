def all_packages():
    """Iterates over all the known packages."""

    filename = "/var/lib/dpkg/status"
    yield from _packages(_lines(filename))


def _packages(lines):
    """Iterates over the packages built from a lines iterator."""

    package = {}
    for line in lines:
        if len(line) > 0:
            for key in ["Package", "Architecture", "Version", "Status"]:
                if line.startswith(key + ": "):
                    assert key not in package
                    package[key] = line[len(key) + 2 :]
        else:
            assert len(package.keys()) == 4
            yield package
            package = {}


def _lines(filename):
    """Iterates over the lines of a plaintext file."""

    with open(filename) as stream:
        for line in stream:
            yield line.rstrip()
