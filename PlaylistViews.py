from urllib.request import urlopen
from bs4 import BeautifulSoup

def getViews(url):
	html=urlopen(url)
	bsObj = BeautifulSoup(html,"lxml")

	a=bsObj.find("div",{"class":"watch-view-count"}).get_text()
	viewsStr=""
	for i in range(0,len(a)-5):
		if a[i]!=',':
			viewsStr=viewsStr+a[i]
	views=int(viewsStr)
	return views

baseUrl="http://www.youtube.com"

html = urlopen("Your YouTube Playlist URL here in double quotes")
bsObj = BeautifulSoup(html,"lxml")
a=bsObj.findAll("tr",{"class":"pl-video yt-uix-tile "})

url = []
for i in range(0,len(a)):
	y=str(a[i])
	temp = baseUrl
	for j in range(0,len(y)):
		if y[j] == 'h' and y[j+1] == 'r' and y[j+2] == 'e' and y[j+3] == 'f':
			x=j+6
			break
	while y[x]!='&':
		temp = temp + y[x]
		x+=1
	url.append(temp)

	
totalViews=0
for i in range(0,len(url)):
        x=getViews(url[i])
        print("Views of Video "+str(i+1)+":"+str(x))
        totalViews+=x
print("Total Views:"+str(totalViews))

