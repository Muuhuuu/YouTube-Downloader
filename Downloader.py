from pytube import YouTube


def selection_function():
    list_size = int(input("Enter the number of videos you want to download:")) # How many videos you want to download
    # yt=input('Youtube URL:')
    final_list = [[int(input('Enter one URL at a time: ')) for _ in range(list_size)] for _ in range(list_size)] # How many videos to download based on number of URLs asked for
    video = YouTube(final_list)

    print("Downloading:", final_list)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    print('')
    print(video.title)
    print('')
    print('by', video.author)
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def download_function():
    video = video.streams.get_highest_resolution()
    video.download()


#print('Is ' , yt.title , 'by' , yt.author + 'correct?') 
# print(('Is' , yt , ' by' , yt.author , 'correct?')) # ' correct?'https://www.youtube.com/watch?v=xHT0ywb2XL0