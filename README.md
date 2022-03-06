#railsIssues
##I. Data collection module (dataCollector)

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
## Usage

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

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


