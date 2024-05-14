import re

def show_time_of_pid(log_line):
    pattern = r"(\w+ \d+ \d+:\d+:\d+).+\[(\d+)\]:"
    result = re.search(pattern, log_line)
    if result is None:
        return ""
    return f"{result[1]} pid:{result[2]}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440