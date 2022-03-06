# Project : railsIssues

-----
This project collect the last N (500 actually) from rails project and analyse the obtained results
## I. Data collection module (dataCollector)

This module is to collect data which is the issues related to the [rails](https://github.com/rails/rails/issues) project we have used the GitHub REST API.
The module have been separated because of the lower limit range access of the API.

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install those libraries.

```bash
pip install PyGithub
```
```bash
pip install requests
```
```bash
pip install csv
```
### Usage

```python
from github import Github
import requests
import csv
# Nb of issues to get
NB_ISSUES= 500
# GitHub username
USER= ""
# Repo username
REPO= ""
# create and open a csv file to save data
with open('CsvFILE', 'w', newline='') as output:
    ...
    # Initialize rows to save
    rows = ["id_issue","nb_issue","title", "id_user", "name_labels",
            "nb_comments", "creation_time", "updated_time", "closed_time"]
    ...
    counter = 0
    # control the number of read issues 
    while i < NB_ISSUES:
        url = f"https://api.github.com/repos/"+USER+"/"+REPO+"/issues?page=" + str(nb_page)
        # pygithub object
        g = Github()
        # get the nb_page of issues
        user_data = requests.get(url).json()
        ...
    #write rows one by one in the csv file
    write.writerow(...)

```
The results of this module will be a CSV File(output_data.csv) in the project root which contains only the wanted rows.

Below a file sample:

|id_issue  |nb_issue|title                                                                                 |id_user |name_labels                         |nb_comments|creation_time       |updated_time        |closed_time|
|----------|--------|--------------------------------------------------------------------------------------|--------|------------------------------------|-----------|--------------------|--------------------|-----------|
|1160222691|44619   |Upgrading Rails from 6.0 --> 6.1 breaks this query                                    |46462767|[]                                  |0          |2022-03-05T04:09:01Z|2022-03-05T04:11:16Z|           |
|1160014635|44617   |Add `active_record.destroy_association_async_batch_size` configuration                |7942714 |['activerecord', 'railties', 'docs']|0          |2022-03-04T20:13:41Z|2022-03-04T22:08:27Z|           |
|1159903813|44616   |Always preload if using proc with multifetch cache                                    |509837  |['actionview']                      |0          |2022-03-04T17:55:29Z|2022-03-04T17:56:38Z|           |
|1159838401|44614   |Add :renderable to the list of rendering keys supported by ActionView::Renderer#render|922012  |['actionview']                      |0          |2022-03-04T16:42:49Z|2022-03-04T16:42:52Z|           |
|1159832478|44613   |Fix eager loading of ActionDispatch::Routing                                          |19192189|['actionpack']                      |0          |2022-03-04T16:35:59Z|2022-03-04T16:41:46Z|           |

## II. Data processing module (dataProcessor)
This module is to analyse and plot data from csv file generated previously
### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install those libraries.

```bash
pip install collections
```
```bash
pip install matplotlib
```
```bash
pip install datetime
```
```bash
pip install numpy
```
### Usage
```python
import collections
import csv
from matplotlib import pyplot
from datetime import datetime
from datetime import timedelta
import numpy as np

# Add a range of X day to the current day in format string
def rangeDate(startdate)

# Convert date type to string
def dateToString(date)

# Add labels on the graphs elements
def autolabel(rects)

# Add gradient to the bar 
def gradientbars(bars)

# Declare variables
...

# Read csv
with open('../output_data.csv', newline='') as csvfile:
    ...
# Initialize variables
...

#Parse data and collect the necessary informations
while i >= 0:
    # If the current date is in the actual date range
     if StratingPeriodDate <= rows[i][6] < EndingPeriodDate:
        #Add informations to the actual variables set
    ...

    else:
        # If not: initialize variable and have a new date range
    ...    


# Retreive informations from the obtained data
...
# Plot using matplotlib library,and save the graphs in dataPlot file
...
pyplot.show()

```
## III. Data plots (dataPlot)
The graphs obtained when running this module are saved in dataPlot folder.

![Alt text](dataPlot/NbissuesByUser.png?raw=true "Plot")


## VI. Web page
In order to analyse the obtained result a simple [WebPage](https://samah37.github.io/railsIssues/) has been created.

The Html code is in index file.

The res file contains css and fonts.\

-----
-----
#### Developper: [Samah KANSAB](https://github.com/samah37)


