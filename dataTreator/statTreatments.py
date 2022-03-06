import collections
import csv
from matplotlib import pyplot
from datetime import datetime
from datetime import timedelta
import numpy as np


def rangeDate(startdate):
    startingDate = datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%SZ")
    return startingDate + timedelta(90)


def dateToString(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")


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
with open('../output_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
    for row in csvreader:
        rows.append(row)
StratingPeriodDate = rows[len(rows) - 1][6]
EndingPeriodDate = dateToString(rangeDate(StratingPeriodDate))
i = len(rows) - 1
globalnm = 0
dictionnary = dict()
dict_update = dict()
dict_closed = dict()
dict_comment = dict()
nb_comment = dict()
counter = 0
counter_update = 0
counter_closed = 0
k = len(rows) - 1
h = len(rows) - 1
nb_comment = 0
while i >= 0:

    if StratingPeriodDate <= rows[i][6] < EndingPeriodDate:
        i -= 1
        counter += 1
        globalnm += 1
        nb_comment += int(rows[i][5])
        if rows[i][7] != '':
            counter_update += 1
        if rows[i][8] != '':
            counter_closed += 1
        list_label = rows[i][4].replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')
        users_list.append(rows[i][3])
        for label in list_label:
            if label != '':
                labels_general_list.append(label)

    else:
        dictionnary[StratingPeriodDate[0:7] + "-" + EndingPeriodDate[0:7]] = counter
        dict_update[StratingPeriodDate[0:7] + "-" + EndingPeriodDate[0:7]] = counter_update
        dict_closed[StratingPeriodDate[0:7] + "-" + EndingPeriodDate[0:7]] = counter_closed
        dict_comment[StratingPeriodDate[0:7] + "-" + EndingPeriodDate[0:7]] = nb_comment
        counter = 0
        counter_update = 0
        counter_closed = 0
        nb_comment = 0
        StratingPeriodDate = EndingPeriodDate
        EndingPeriodDate = dateToString(rangeDate(StratingPeriodDate))

dictionnary[
    StratingPeriodDate[0:7] + "-" + dateToString(datetime.strptime(rows[0][6], "%Y-%m-%dT%H:%M:%SZ"))[0:7]] = counter
dict_update[StratingPeriodDate[0:7] + "-" + dateToString(datetime.strptime(rows[0][6], "%Y-%m-%dT%H:%M:%SZ"))[
                                            0:7]] = counter_update
dict_closed[StratingPeriodDate[0:7] + "-" + dateToString(datetime.strptime(rows[0][6], "%Y-%m-%dT%H:%M:%SZ"))[
                                            0:7]] = counter_closed
dict_comment[
    StratingPeriodDate[0:7] + "-" + dateToString(datetime.strptime(rows[0][6], "%Y-%m-%dT%H:%M:%SZ"))[0:7]] = nb_comment
occurences = collections.Counter(labels_general_list)
label_set = set(labels_general_list)
occurences_users = collections.Counter(users_list)
set_user = set(users_list)
x = np.arange(len(occurences))
id_user =0
max = 0
nb_one = 0
for i in (set_user):
    if occurences_users[i]>max:
        max = occurences_users[i]
        id_user = i
    if occurences_users[i]== 1:
        nb_one+=1
nb_one= float(nb_one/len(set_user))
print(id_user)
print(max)
print(nb_one)
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
UserPlot = axUsers.plot([j for j in set_user], [occurences_users[i] for i in (set_user)], color='#3E7DCC', label = 'Nb users: '+str(len(set_user))+'\nThe user "'+ str(id_user)+'" have reported '+str(max)+ ' issues \n % users with only one issue :'+str(nb_one))
axUsers.set_ylabel('Number of issues')
axUsers.set_xlabel('User ID')
axUsers.set_title('Reporting issues By users')
axUsers.set_xticks(np.arange(len(occurences_users)))
axUsers.set_xticklabels(occurences_users, rotation=90, ha='right', fontsize=2)
axUsers.legend()
figUsers.tight_layout()
pyplot.savefig('../dataPlot/NbissuesByUser.png')
figTime, axTime = pyplot.subplots()
TimePlot = axTime.plot([j for j in dictionnary.keys()], [dictionnary[i] for i in dictionnary.keys()], color='#3E7DCC')
axTime.set_ylabel('Number of issues')
axTime.set_xlabel('Time')
axTime.set_title('Reporting issues across time')
axTime.set_xticks(np.arange(len(dictionnary)))
axTime.set_xticklabels(dictionnary.keys(), rotation=90, ha='right', fontsize=8)
axTime.legend()
figTime.tight_layout()
pyplot.savefig('../dataPlot/NbIssuesPerTime.png')

figTimeSU, axTimeSU = pyplot.subplots()
axTimeSU.plot([j for j in dictionnary.keys()], [dictionnary[i] for i in dictionnary.keys()], color='#3E7DCC',
              label='created issues')
axTimeSU.plot([j for j in dict_update.keys()], [dictionnary[i] for i in dict_update.keys()], color='yellow',
              linestyle='-.', label="updated issues")
axTimeSU.plot([j for j in dict_closed.keys()], [dict_closed[i] for i in dict_closed.keys()], color='red',
              label="closed issues")
axTimeSU.plot([j for j in dict_comment.keys()], [dict_comment[i] for i in dict_comment.keys()], color='green',
              label="comment number")
axTimeSU.set_ylabel('Number of issues')
axTimeSU.set_xlabel('Time')
axTimeSU.set_title('Reporting issues across time')
axTimeSU.set_xticks(np.arange(len(dictionnary)))
axTimeSU.set_xticklabels(dictionnary.keys(), rotation=90, ha='right', fontsize=8)
axTimeSU.legend()
figTimeSU.tight_layout()
pyplot.savefig('../dataPlot/NbIssuesPerTimeSU.png')
pyplot.show()
