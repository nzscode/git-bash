#!/usr/bin/env python3
import re
import operator
import csv
from operator import itemgetter

per_user = {
    "test_user": [0, 0],
}
error_d = {
    "test issue": 0,
}
file = "x_syslog.log"
reg = r": ([\w]*) ([\w ']*)\[?(#[\d]*)?\]? \(([\w.]*)\)"

user_name = ""
ticket_type = ""
error_type = ""
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        reg_result = re.search(reg, line)
        if reg_result is not None:
            user_name = reg_result[4]
            if user_name not in per_user.keys():
                # per_user[user_name] = [["INFO", 0], ["ERROR", 0]]
                per_user[user_name] = [0, 0]

            else:
                pass
            if user_name in per_user.keys():
                ticket_type = reg_result[1]
                if ticket_type == "INFO":
                    # per_user[user_name][0][1] += 1
                    per_user[user_name][0] += 1
                elif ticket_type == "ERROR":
                    # per_user[user_name][1][1] += 1
                    per_user[user_name][1] += 1
                    error_type = reg_result[2]
                    if error_type not in error_d.keys():
                        error_d[error_type] = 1
                    else:
                        error_d[error_type] += 1

                else:
                    pass

        else:
            pass
        user_name = ""
        ticket_type = ""
        error_type = ""

print(per_user)
error_list = []
sorted_errors = []
for error in error_d:
    error_list.append([error_d[error], error])
new_error_list = sorted(error_list, reverse=True)
for error in new_error_list:
    sorted_errors.append((error[1], error[0]))
error_list_keys = ["Error", "Count"]
sorted_errors_dict = dict(sorted_errors)
print(sorted_errors_dict)

users_list = []
for user in per_user:
    users_list.append((user, str(per_user[user])))
sorted_users_list = (sorted(users_list))
user_list_keys = ["Username", "INFO", "ERROR"]
sorted_users_dict = dict(sorted_users_list)
print(sorted_users_dict)

with open('user_statistics.csv', 'w') as user_stats:
    writer = csv.DictWriter(user_stats, fieldnames=user_list_keys)
    writer.writeheader()
    writer.writerows(sorted_users_dict)

with open('error_message.csv', 'w') as error_messages:
    writer = csv.DictWriter(error_messages, fieldnames=error_list_keys)
    writer.writeheader()
    writer.writerows(sorted_errors_dict)
