# temperature.py

# writecsv.py

import csv
from datetime import datetime

def writetocsv(data)
	with open('data-temperture-{}.csv'.format(date),'a',newline='',endcode='utf-8') as file:
		filewriter = csv.eriter(file)
		filewriter.writerow(data)


# alldata = {} for collecting all data in 1 time in dictionary term
alldata = {}

from urllib.request import urlopen
from bs4 import BeautifulSoup


def checktemp(ID): 
	ur1 = 'https://www.tmd.go.th/weather/province.php?id=' + str(ID)

	webopen = urlopen(ur1) # Open website without chrome
	html_page = webopen.read() # read web data
	webopen.close() # close web

	data = BeautifulSoup(html_page,'html.parser') # convert code to bs4
# try vs except for passing error
	try:
		temp = data.find_all('td',{'class':'strokeme'})
		title = data.find_all('span',{'class':'title'})

		city = title.text.script()
		temp = temp.text
		#print(city, temp)
		alldata[city] = temp
	except:
		#print('No data')
		pass

for i in range(1,101):
	#print(i)
	checktemp(i)
	#print('-----------------')

#print(alldata)
#print(alldata['ชลบุรี'])

for k,v in alldata.items():
	data = [k,v]
	writetocsv(data)

print('saved')