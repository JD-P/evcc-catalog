# Introduction #

This is a project to take the information on [EvCC's Class Schedule search](https://www.everettcc.edu/classes/) and make a mirror of the information.

## Rationale ##

The original is missing key features, such as the ability to search classes by what
credits they satisfy, how many credits a class offers, etc. Longer term I would
like to create a automatic scheduler which is given a set of constraints and uses
constraint satisfaction algorithms to determine a set of schedules which would work
for the user.

# Scraping #

## Dependencies ##

Right now the only dependency required for the scraper is BeautifulSoup4, however
your installation of python needs to have sqlite3 support.

## Use ##

To use the scraping kit included in this repository, go to the [Class Schedule search](https://www.everettcc.edu/classes/)
and search the quarter you want for classes in all departments, this will return
a list of all offered classes. Save this page and then use it with catalog2csv.py.
The resulting CSV file will be written to stdout, so you'll need to redirect it
using the shell to a file. Take that file and convert it to a sqlite database
with csv2db.py. This will give you a functional mirror of the class schedule.