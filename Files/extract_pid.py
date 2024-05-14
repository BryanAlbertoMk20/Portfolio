import re


def extract_pid(log_line):
    pattern = r"\[(\d+)\]: (\w+) "
    result = re.search(pattern, log_line)
    if result is None:
        return ""
    return f"{result[1]} {result[2]} "



log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"


print(extract_pid(log))


