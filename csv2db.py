import sqlite3
import csv
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("courses_csv", help="Filepath of CSV file to read data from.")
parser.add_argument("sqloutfile", help="Filepath to write sqlite file to.")

arguments = parser.parse_args()

infile = open(arguments.courses_csv)

database = sqlite3.connect(arguments.sqloutfile)

cursor = database.cursor()

statement = """CREATE TABLE courses (title text, description text, credtype text, prereqs text, icons text, id integer,
section text, credits float, capacity integer, enrolled integer, instructors text, start_end text, days text, location text)"""

cursor.execute(statement)

inreader = csv.reader(infile)

for row in inreader:
    cursor.execute("insert into courses values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)

cursor.close()
database.commit()
