import csv


def read_html():
    content = {}
    csvfile = open('html.csv', 'r+')
    reader = csv.reader(csvfile)
    for html in reader:
        content[html[0]] = html[1]
    csvfile.close()
    return content


if __name__ == '__main__':
    c = read_html()
    print(c)
