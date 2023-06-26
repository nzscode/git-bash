#!/usr/bin/env python3
import operator
import re
import csv

per_user = {}
error_d = {}
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
                per_user[user_name] = [0, 0]
            else:
                pass
            if user_name in per_user.keys():
                ticket_type = reg_result[1]
                if ticket_type == "INFO":
                    per_user[user_name][0] += 1
                elif ticket_type == "ERROR":
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

error_list = []
error_csv_keys = ["Error", "Count"]
for error in error_d:
    error_list.append([error, error_d[error]])
error_list.sort(key=operator.itemgetter(1), reverse=True)
error_list.insert(0, error_csv_keys)
with open("error_message.csv", 'w', newline="") as error_message_csv:
    writer = csv.writer(error_message_csv)
    writer.writerows(error_list)

user_list = []
user_list_csv_keys = ["Username", "INFO", "ERROR"]
for user in per_user.keys():
    user_list.append([user, per_user[user][0], per_user[user][1]])
    user_list.sort(key=operator.itemgetter(0))
user_list.insert(0, user_list_csv_keys)
with open("user_statistics.csv", 'w', newline="") as user_statistics_csv:
    writer = csv.writer(user_statistics_csv)
    writer.writerows(user_list)
