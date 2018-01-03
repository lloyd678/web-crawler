from bs4 import BeautifulSoup
import re
import requests
import csv

def fetch(address):
    url = address
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    links = soup.find_all('a')
    return links


def process(links):
    pairs=[]
    for link in links:

        regex = r'.*/requiredtag/\d\d/.*'
        process = re.search(regex , link.get('href'))
        if process:

            href = link.get('href')

            pairs.append(["href", href])
    return pairs


def filewritelist(stringoutput, name):
    filename = 'spideroutput/' + name + '.txt'
    file = open(filename, 'w')
    file.write(stringoutput)

def create(pairs):
    stringoutput =""
    for pair in pairs:
        string = pair[0] + '---' + pair[1]
        stringoutput = stringoutput + string +"\n"
    return stringoutput


def main():
    with open('downloadtags.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            address = row[0]
            name = row[1]
            links= fetch(address)
            pairs = process(links)
            stringoutput = create(pairs)
            filewritelist(stringoutput, name)




main()
