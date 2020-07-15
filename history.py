import lib.events
import os


events = list(sorted(lib.events.all_events(), key=lambda e: e["Start-Date"]))

user = "%s (%s)" % (os.getlogin(), os.getuid())
for event in events:
    if "Requested-By" not in event or event["Requested-By"] != user:
        continue
    print("[%s] %s" % (event["Start-Date"], event["Commandline"]))
    for key in "Install", "Update", "Remove", "Purge":
        if key in event:
            print("%s: %s" % (key, " ".join(p["Name"] for p in event[key])))
    print()
