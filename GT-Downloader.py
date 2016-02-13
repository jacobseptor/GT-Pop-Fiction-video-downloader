import urllib.request
import bs4
import json
import os


#IDs for the embeded videos
VideoID = ["2949499", "2955240", "2946123", "2951380", "2945776", "2950960",
           "2953555", "2954678", "2954302", "2954236", "2950130", "2944217",
           "2955558", "2949392", "2951626", "2946665", "2952640", "2945128",
           "2947859", "2951947", "2945669", "2953917", "2956585", "2947442", 
           "2948253", "2953534", "2952238", "2951929", "2947037", "2947627"]

#base URL VideoIDs get added on end
url = "http://embed.gametrailers.com/embed/" 

for i in range(len(VideoID)):
    #takes the curent VideoID and adds to url to form temp url
    tempURL = url+VideoID[i]
    
    #loads the url
    page = urllib.request.urlopen(tempURL)
    
    #IDK turns page into a dict
    soup = bs4.BeautifulSoup(page.read(), "lxml")
    data  = soup.find_all("script")[0].string
    jsonValue = '{%s}' % (data.split('{', 1)[1].rsplit('}', 1)[0],)
    value = json.loads(jsonValue)

    #TELLS WHAT IS DOWNLOADING
    print("Downloading: "+value["contentName"])
    
    #removes the ':' from the name and adds a '-'
    fileName = value["contentName"].replace(':', '-')

    #sets the download path and creates if non existent
    path = os.path.join(os.path.expanduser('~'), "Downloads", "Pop Fiction")
    if not os.path.exists(path):
        os.makedirs(path)
    
    file = os.path.join(path, fileName+".mp4")
    print(file)

    #downloads the video
    #urllib.request.urlretrieve(value['media'][2]['uri'], file)
    try:
        urllib.request.urlretrieve(value['media'][2]['uri'], file)
    except urllib.request.URLError:
        print("URLError")
