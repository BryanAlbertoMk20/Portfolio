import csv

filename = 'employee_data.csv'
fh = open(filename, encoding='utf8')
headers = next(fh)
reader = csv.reader(fh)

full_name = []
employee_id = []
email_address = []

for row in reader:
    full_name.append(row[0]+' '+row[1])
    employee_id.append(int(row[2]))
    email_address.append(row[3])


def employee_name_lookup(id):
    index = employee_id.index(id)
    return full_name[index]

def employee_email_lookup(id):
    index = employee_id.index(id)
    return email_address[index]

def employee_id_and_name_lookup(email):
    index = email_address.index(email)
    return full_name[index], employee_id[index]














