#******** Single Video Download********
from pytube import YouTube
link = "https://www.youtube.com/watch?v=JXQ_lFGM0bg"
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()  #Single Video
#videos = youtube_1.streams.filter(only_audio=True) #Only Audio
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter :"))
videos[strm].download()
print('Successfully')

#********Playlist********
#from pytube import Playlist
#py = Playlist("https://www.youtube.com/playlist?list=PLdHIF9NW4IWotEB-5UWCHa6jsykp4Vsfm ")
#print(f'Downloading : {py.title}')
#for video in py.videos:
    #video.streams.first().download()

