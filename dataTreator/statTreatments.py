import collections
import csv
from matplotlib import pyplot
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
print(occurences["regression"])
#pyplot.figure(figsize=(50, 10))
pyplot.rc('xtick', labelsize=4)
pyplot.bar([j for j in label_set], [occurences[i]for i in (label_set)])
pyplot.xlabel('The labels', )
pyplot.savefig('test.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
pyplot.show()




