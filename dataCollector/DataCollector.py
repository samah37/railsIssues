import base64
from github import Github
from pprint import pprint
import requests
import json
import csv

# Github username
number = 500
nb_page =1
i = 0
list=[]
with open('output_data.csv', 'w', newline='') as output:
    write = csv.writer(output)
    rows = ["nb_issue","id_issue","title", "id_user", "name_labels",
            "nb_comments", "creation_time", "updated_time", "closed_time"]
    write.writerow(rows)
    counter = 0
    while i < 500:
        url = f"https://api.github.com/repos/rails/rails/issues?page=" + str(nb_page)
        # pygithub object
        g = Github()
        # get that user by username
        user_data = requests.get(url).json()
        i += len(user_data)
        nb_page += 1

        for user in range(len(user_data)):
            list_label = []
            for label in user_data[user]["labels"]:
                list_label.append(label["name"])
            print(list_label)
            if counter<500:
                write.writerow(
                    [user_data[user]["id"], user_data[user]["number"], user_data[user]["user"]["id"], list_label,
                     user_data[user]["comments"], user_data[user]["created_at"], user_data[user]["updated_at"],
                     user_data[user]["closed_at"]])
                counter += 1
print(i)
print(counter)
