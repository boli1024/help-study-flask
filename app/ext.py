import csv


def read_course():
    courses = []
    csvfile = open('app/data/data.csv', 'r+')
    reader = csv.reader(csvfile)
    for row in reader:
        courses.append([row[0], row[1]])
    csvfile.close()
    return courses


def read_html():
    content = {}
    csvfile = open('app/data/html.csv', 'r+')
    reader = csv.reader(csvfile)
    for html in reader:
        content[html[0]] = html[1]
    csvfile.close()
    return content


if __name__ == '__main__':
    courses = read_course()
    print(courses)
