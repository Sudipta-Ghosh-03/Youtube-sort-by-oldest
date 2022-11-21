import scrapetube
from tabulate import tabulate

channelurl = input("Channel url: ")

videos = scrapetube.get_channel(channel_url= channelurl)

url = "https://www.youtube.com/watch?v="

vidlist = []
vidTitle = []
vidUploadTime = []

for video in videos:
    vidlist.append(url + str(video['videoId']))    
    
    vidTitle.append(video['title']['runs'][0]['text'])

    vidUploadTime.append(video['publishedTimeText']['simpleText'])
    

vidlist = vidlist[::-1]
vidTitle = vidTitle[::-1]
vidUploadTime = vidUploadTime[::-1]

numVids = ''
 
while numVids not in range(len(vidlist)): 
    numVids = int(input(f"How many old videos do you want to see? \nThe channel has total {len(vidlist)} videos(excluding shorts) \nBe sensible with your choice \nChoosing a number too high might disrupt the output: "))
    if numVids not in range(len(vidlist)):
        print("Invalid choice")

data = {'Title' : vidTitle[:numVids], 'Uploaded' : vidUploadTime[:numVids], 'Url': vidlist[:numVids]}

print(tabulate(data, headers='keys', tablefmt='double_grid',  maxcolwidths=[55,10,55], showindex = "always"))

input("Press any key to exit...")
