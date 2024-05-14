import re
import csv
import operator

users = {}
error = {}
info = {}

logfile = "log.txt"
pattern = r"ticky: ERROR ([\w' ]+)"

with open(logfile) as loglines:
    for lines in loglines:
        if "ERROR" in lines:
            pattern = r"ticky: ERROR ([\w' ]+)"
            result = re.search(pattern, lines)
            error_names = result[1]
            error[error_names] = error.get(error_names, 0) + 1

header = ["Error", "Count"]

with open('../some_code/error_message.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for err, count in error.items():
        writer.writerow({"Error": err, "Count": count})
print("Csv file has been successfully created.")

user = {}
user_errors = {}
user_info = {}

with open("log.txt") as logfiles:
    for line in logfiles.readlines():

        user_pattern = r"\((\w+)\)$"
        user_result = re.search(user_pattern, line)
        name = user_result[1]
        user_errors[name] = user_errors.get(name, 0)
        user_info[name] = user_info.get(name, 0)

        if "ERROR" in line:
            user_errors[name] += 1

        if "INFO" in line:
            user_info[name] += 1

user_errors = sorted(user_errors.items(), key=operator.itemgetter(0))
user_info = sorted(user_info.items(), key=operator.itemgetter(0))

user_stats = {}
info_stats = {}
for key, value in user_errors:
    user_stats[key] = value

for k, v in user_info:
    info_stats[k] = v

with open('../some_code/user_statistics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Username", "INFO", "ERROR"])

    names = []
    infs = []
    errs = []

    for k in user_stats.keys():
        names.append(k)
    for val1 in info_stats.values():
        infs.append(val1)
    for val2 in user_stats.values():
        errs.append(val2)
    count = 0
    for row in names:
        writer.writerow((names[count], infs[count], errs[count]))
        count += 1





















