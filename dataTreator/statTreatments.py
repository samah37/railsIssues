import collections
import csv
import numpy as np
from matplotlib import pyplot
import pandas as pd


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
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


#def BarPlot(X, Y):


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
    for row in rows:
        list_label = row[4].replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
        users_list.append(row[3])
        for label in list_label:
            if label != '':
                labels_general_list.append(label)
occurences = collections.Counter(labels_general_list)
label_set = set(labels_general_list)
print(len(label_set))
print(len(labels_general_list))
occurences_users = collections.Counter(users_list)
print(len(occurences_users))
set_user = set(users_list)
# pyplot.figure(figsize=(50, 10))
# pyplot.rc('xtick', labelsize=6)
x = np.arange(len(occurences))  # the label locations
width = 0.35  # the width of the bars
fig, ax = pyplot.subplots()
fig1, ax1 = pyplot.subplots()
c = ['red', 'yellow', 'black', 'blue', 'orange']
rects1 = ax.bar([j for j in label_set], [occurences[i] for i in (label_set)], color=c)
rects2 = ax1.plot([j for j in set_user], [occurences_users[i] for i in (set_user)], color='#3E7DCC')
ax.set_ylabel('Occurences')
ax.set_title('Occurences by Labels')
ax.set_xticks(x)
ax.set_xticklabels(list(label_set), rotation=45, ha='right', fontsize=6)
ax.legend()
autolabel(rects1)
gradientbars(rects1)
fig.tight_layout()
ax1.set_ylabel('Occurences')
ax1.set_title('Occurences by Labels')
ax1.set_xticks(np.arange(len(occurences_users)))
ax1.set_xticklabels(occurences_users, rotation=90, ha='right', fontsize=3)
ax1.legend()
fig1.tight_layout()
pyplot.savefig('../dataPlot/OccurencesByLabels.png')
pyplot.show()
