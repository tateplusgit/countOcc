import csv

import collections

def generate_summary_for_web(csvfile, html_filename):
    table = ""
    tr = ""

    csvfile = "diabetes_data.csv"



    with open(csvfile) as file:

        ctr = 0
        for record in csvfile:
            if record[1] == 'Yes':
                ctr += 1
        #print(ctr)

        table += "<table border=1 cellpadding=1><tr><th></th><th>Class</th><th></th><th></th><th></th></tr><tr><th></th><th>Positive</th><th></th><th>Negative</th><th></th></tr><tr><th>Attribute</th><th>Yes</th><th>No</th><th>Yes</th><th>No</th></tr>"
        csv_reader_object = csv.reader(file)
        next(csv_reader_object)

        for line in csv_reader_object:
            Polyuria = line[2]
            Class = line[16]

    """
    age = line[4]
    name = line[5]
    salary = line[6]
    age = line[7]
    name = line[8]
    salary = line[9]
    age = line[10]
    name = line[11]
    salary = line[12]
    age = line[13]
    name = line[14]
    salary = line[15]
    name = line[0]
    age = line[16]
    """

    tr += "<tr>"

    tr += "<td>Polyuria</td>"

    tr += "<td>Class</td>"

    tr += "<td>Class</td>"

    tr += "<td>Class</td>"

    tr += "<td>Class</td>"

    # tr += "<td>%s</td>" % age

    tr += "</tr>"

    end = "</table>"
    html = table + tr + end
    print(ctr)
    html_filename = open("output.html", "w+")
    html_filename.write(html)
    html_filename.close()

generate_summary_for_web('csvfile', 'html_filename')