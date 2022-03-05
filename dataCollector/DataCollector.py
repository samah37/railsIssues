import base64
from github import Github
from pprint import pprint
import requests
import json
import csv
NB_ISSUES= 500
USER= "rails"
REPO= "rails"
# Github username
nb_page =1
i = 0
with open('output_data.csv', 'w', newline='') as output:
    write = csv.writer(output)
    rows = ["id_issue","nb_issue","title", "id_user", "name_labels",
            "nb_comments", "creation_time", "updated_time", "closed_time"]
    write.writerow(rows)
    counter = 0
    while i < NB_ISSUES:
        url = f"https://api.github.com/repos/"+USER+"/"+REPO+"/issues?page=" + str(nb_page)
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
            if counter < NB_ISSUES:
                write.writerow(
                    [user_data[user]["id"], user_data[user]["number"], user_data[user]["title"],user_data[user]["user"]["id"], list_label,
                     user_data[user]["comments"], user_data[user]["created_at"], user_data[user]["updated_at"],
                     user_data[user]["closed_at"]])
                counter += 1
print(i)
print(counter)
