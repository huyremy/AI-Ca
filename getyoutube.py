import pytube
url = input("Enter youtube url:")
path = "D:"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
