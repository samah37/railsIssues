import collections
import csv

import numpy as np
from matplotlib import pyplot
import pandas as pd
rows = []
label_set= set()
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
        list_label = row[4].replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
        for label in list_label:
            if label != '':
                label_set.add(label)
                labels_general_list.append(label)
occurences = collections.Counter(labels_general_list)
print(len(label_set))
print(len(labels_general_list))
#pyplot.figure(figsize=(50, 10))
pyplot.rc('xtick', labelsize=6)

x = np.arange(len(occurences))  # the label locations
width = 0.35  # the width of the bars

fig, ax = pyplot.subplots()
rects1 = ax.bar([j for j in label_set], [occurences[i]for i in (label_set)], color = '#3E7DCC')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Occurences')
ax.set_title('Occurences by Labels')
ax.set_xticks(x)
ax.set_xticklabels(list(label_set),  rotation=45, ha='right')
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)


fig.tight_layout()
pyplot.savefig('../dataPlot/OccurencesByLabels.png')
pyplot.show()




