from black import diff
import requests
from bs4 import BeautifulSoup

districts = {'Wlochy': '357', 'Ochota': '355', 'Mokotow': '353'}

class Flats:
    def __init__(self, district):
        self.district = district
        self.url = 'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bdistrict_id%5D={}&search%5Bfilter_float_price:to%5D=2500'.format(districts[self.district])
        self.resp = requests.get(self.url)
        self.soup = BeautifulSoup(self.resp.text, 'html.parser')
        self.txtName = "numberOfFlats" + self.district + ".txt"

    def getNumberOfFlats(self):
        a = self.soup.find("div", {"data-testid": "total-count"}).get_text()
        numberOfFlats = int(a[11:16].strip())
        return numberOfFlats

    def checkNewFlats(self):
        with open(self.txtName) as f:
            numberOfFlats = int(f.readline())
        return numberOfFlats
        
    def isThereNewFlats(self):
        newvalue = self.getNumberOfFlats()
        oldvalue = self.checkNewFlats()
        if newvalue > oldvalue:
            f = open(self.txtName, "w")
            f.write(str(newvalue))
            f.close()
            difference = newvalue - oldvalue
            text = "Zostalo dodanych " + str(difference) + " nowych mieszkan na " + self.district + " " + self.url
            return text
        else:
            f = open(self.txtName, "w")
            f.write(str(newvalue))
            f.close()
            text = "Nie ma nowych mieszkan na " + self.district
            return text

    def numberOfFLats(self):
        number = str(self.getNumberOfFlats())
        text = "Jest " + number + " mieszkan na " + self.district
        return text 

