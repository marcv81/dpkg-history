green = "\x1b[92m"
red = "\x1b[91m"
end = "\x1b[0m"

def print_event(event, installed):
    print("[%s] %s" % (event["Start-Date"], event["Commandline"]))
    for key in "Install", "Update", "Remove", "Purge":
        if key in event:
            packages = []
            for package in event[key]:
                name = package["Name"]
                text = (green if name in installed else red) + name + end
                packages.append(text)
            print("%s: %s" % (key, " ".join(packages)))
    print()
