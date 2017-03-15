import time
import re
from os import path
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from catalogapp import models

import csv

class Command(BaseCommand):
    help = "Import a CSV created from the evcc class schedule."

    def add_arguments(self, parser):
        pass
        parser.add_argument('filepath', nargs="+", type=str)

    def handle(self, *args, **options):
        with open(options['filepath'][0]) as infile:
            for row in csv.DictReader(infile):
                outrows = self.mk_db_objects(row)
                for outrow in outrows:
                    if type(outrow) == list:
                        for outrow_2 in outrow:
                            outrow_2.save()
                            print(outrow_2, "saved!")
                    else:
                        outrow.save()
                        print(outrow, "saved!")
                
    def mk_db_objects(self, row_dict):
        """The meat of the import_csv command. Takes a csv and creates usable
        database row objects from it."""
        current_time = time.time()
        course_date = datetime.utcfromtimestamp(current_time)
        cid = '-'.join([str(row_dict["id"]),  str(current_time)])
        course = models.Course(id = cid,
                               course_date=course_date,
                               course_id=row_dict["id"],
                               title=row_dict["title"],
                               description=row_dict["description"],
                               section=row_dict["section"],
                               credits = row_dict["credits"],
                               capacity = row_dict["capacity"],
                               enrolled= row_dict["enrolled"],
                               start_end = row_dict["start_end"],
                               location = row_dict["location"])
        # Create days rows
        days_raw = []
        if row_dict["days"].strip() == "ARRANGED":
            days_raw.append("A")
        else:
            for raw_day in re.findall("[A-Z][a-z]*", row_dict["days"]):
                days_raw.append(raw_day)
        days = []
        for raw_day in days_raw:
            days.append(models.Days(course=course, day=raw_day))

        # Create instructors rows

        instructors_raw = row_dict["instructors"].split(":")
        instructors = []
        for raw_instructor in instructors_raw:
            instructors.append(models.Instructors(course=course, instructor=raw_instructor))

        # Create conditions rows

        conditions_raw = row_dict["icons"].split(":")
        conditions = []
        for raw_condition in conditions_raw:
            conditions.append(models.Conditions(course=course, condition=raw_condition))

        # Create prerequisite rows

        prerequisites_raw = re.findall("[A-Z]+&* [0-9][0-9][0-9]",row_dict["prereqs"])
        prerequisites = []
        for raw_prerequisite in prerequisites_raw:
            prerequisites.append(models.Prerequisites(course=course, prerequisite=raw_prerequisite))

        # Create requirements rows
        requirements = []
        
        if row_dict["credtype"] == "N.A":
            requirements.append(models.Requirements(course=course, requirement=None))
        else:
            requirements_raw = [requirement.strip() for requirement in
                                row_dict["credtype"].split(",")]
            for raw_requirement in requirements_raw:
                if raw_requirement:
                    requirements.append(models.Requirements(course=course,
                                                            requirement=raw_requirement))
            
        return (course, days, instructors, conditions, prerequisites, requirements)
        
        

