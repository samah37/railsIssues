import collections
import csv
from matplotlib import pyplot
import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np


def rangeDate(startdate):
    dateDebut = datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%SZ")
    return dateDebut + timedelta(90)


def dateToString(date):
    return date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")



def autolabel(rects):
    
    for rect in rects:
        height = rect.get_height()
        axLabel.annotate('{}'.format(height),
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         xytext=(0, 1),  # 3 points vertical offset
                         textcoords="offset points",
                         ha='center', va='bottom')


def gradientbars(bars):
    grad = np.atleast_2d(np.linspace(0, 1, 256)).T
    ax = bars[0].axes
    lim = ax.get_xlim() + ax.get_ylim()
    for bar in bars:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x, y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent=[x, x + w, y, y + h], aspect="auto", zorder=0)
    ax.axis(lim)


rows = []
label_set = set()
users_list = []
labels_general_list = []
"""
rows = ["nb_issue","id_issue","title", "id_user", "name_labels",
            "nb_comments", "creation_time", "updated_time", "closed_time"]"""
with open('../output_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


"""
Plot the occurency of the set of labels in the last 500 Issues

"""
"""
"""

StratingPeriodDate = rows[len(rows)-1][6]
EndingPeriodDate = dateToString(rangeDate(StratingPeriodDate))
print(EndingPeriodDate)
listoflists = []
subList = []
i = len(rows)-1
counter=0
globalnm=0
dictionnary = dict()
test = 0
while i>=0 or rows[i][6]<EndingPeriodDate :
    list_label = rows[i][4].replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
    users_list.append(rows[i][3])
    for label in list_label:
        if label != '':
            labels_general_list.append(label)
    if rows[i][6]>=StratingPeriodDate and rows[i][6]<EndingPeriodDate:
        counter+=1
        globalnm+=1
        i -= 1
    else:
        test += counter
        print(counter)
        counter =0
        dictionnary[StratingPeriodDate+ "-"+ EndingPeriodDate]= counter
        subList = []
        StratingPeriodDate=rows[i][6]
        print(StratingPeriodDate)
        EndingPeriodDate= dateToString(rangeDate(StratingPeriodDate))


print(test)
print(dictionnary.keys())
occurences = collections.Counter(labels_general_list)
label_set = set(labels_general_list)
occurences_users = collections.Counter(users_list)
set_user = set(users_list)
x = np.arange(len(occurences))  # the label locations
width = 0.35
figLabel, axLabel = pyplot.subplots()
c = ['red', 'yellow', 'black', 'blue', 'orange']
LabelBar = axLabel.bar([j for j in label_set], [occurences[i] for i in (label_set)], color=c)
axLabel.set_ylabel('Occurences')
axLabel.set_title('Occurences by Labels')
axLabel.set_xticks(x)
axLabel.set_xticklabels(list(label_set), rotation=45, ha='right', fontsize=8)
axLabel.legend()
autolabel(LabelBar)
gradientbars(LabelBar)
figLabel.tight_layout()
pyplot.savefig('../dataPlot/OccurencesByLabels.png')
figUsers, axUsers = pyplot.subplots()
UserPlot = axUsers.plot([j for j in set_user], [occurences_users[i] for i in (set_user)], color='#3E7DCC')
axUsers.set_ylabel('Number of issues')
axUsers.set_xlabel('User ID')
axUsers.set_title('Reporting issues By users')
axUsers.set_xticks(np.arange(len(occurences_users)))
axUsers.set_xticklabels(occurences_users, rotation=90, ha='right', fontsize=2)
axUsers.legend()
figUsers.tight_layout()
pyplot.savefig('../dataPlot/NbissuesByUser.png')
pyplot.show()

