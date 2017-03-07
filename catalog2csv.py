import sys
import csv
from argparse import ArgumentParser
from bs4 import BeautifulSoup

parser = ArgumentParser()

parser.add_argument("catalog", help="Filepath to parseable catalog.")
parser.add_argument("--elective", "-e", help="Elective string to search for.")
parser.add_argument("--elist", help="Print a list of elective types and exit.")

arguments = parser.parse_args()

infile = open(arguments.catalog)

soup = BeautifulSoup(infile, "html.parser")

courses = soup.find_all("table", id="tableOfMainCourses")[0]

course_rows_raw = courses.find_all("tr", style="display:none;")

course_row_pairs = []

for i in tuple(range(len(course_rows_raw)))[1:-1:2]:
    pair = [course_rows_raw[i], course_rows_raw[i+1]]
    course_row_pairs.append(pair)

course_outrows = []
    
for pair in enumerate(course_row_pairs):
    course_info_hdiv = pair[1][1]
    course_info_tbody = course_info_hdiv.find_all("tbody")[0]
    course_info_header = course_info_tbody.find_next("tr")
    course_info_table = course_info_header.find_next("tr")


    course_title = course_info_header.find_all("h3")[0].string.split("-")[1]
    course_icons_raw = course_info_header.find_all("span")
    course_icons = []
    for icon in course_icons_raw:
        course_icons.append(icon.string)

    course_credit_description = course_info_table.find_next("p")
    try:
        course_credit_type = course_credit_description.string.split(") ")[0][1:]
    except AttributeError:
        course_credit_type = course_credit_description.contents[0].split(") ")[0][1:]
    if len(course_credit_type) > 30:
        course_credit_type="N.A"

    course_prereqs_raw = course_credit_description.find_next("p")
    course_prereqs = course_prereqs_raw.contents

    course_details = course_info_table.find_next("tbody")
    course_id = course_details.find_next("td")
    course_section = course_id.find_next("td")
    course_credits = course_section.find_next("td")
    course_capacity = course_credits.find_next("td")
    course_enrolled = course_capacity.find_next("td")
    course_instructors = course_enrolled.find_next("td")
    course_start_end = course_instructors.find_next("td")
    course_days = course_start_end.find_next("td")
    course_location = course_days.find_next("td")
    
    course_outrows.append([course_title,
                           course_credit_description,
                           course_credit_type,
                           course_prereqs,
                           ':'.join(course_icons),
                           course_id.string,
                           course_section.string,
                           course_credits.string,
                           course_capacity.string,
                           course_enrolled.string,
                           course_instructors.string,
                           course_start_end.string,
                           course_days.string,
                           course_location.string])


coursewriter = csv.writer(sys.stdout)
coursewriter.writerow(["title",
                       "description",
                       "credtype",
                       "prereqs",
                       "icons",
                       "id",
                       "section",
                       "credits",
                       "capacity",
                       "enrolled",
                       "instructors",
                       "start_end",
                       "days",
                       "location"])
for row in course_outrows:
    coursewriter.writerow(row)
