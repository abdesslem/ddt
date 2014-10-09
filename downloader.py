from urllib.request import urlopen
from urllib.request import Request
#import urllib
#import urllib2
class FileDownloader(object):
      
     def __init__(self):
        self.url = None
        self.progress = None
        self.status = None # {0:"Downloading", 1:"Completed", 2:"Paused", 3:"Error"}
        self.fileName = None
        self.u = None #urllib
        self.fileSize = None
        self.szDownloaded = 0
        self.isPaused = False
     def startDownload(self, url, start=None):
        self.isPaused = False
        self.url = url
        self.fileName = url.split("/")[-1]
        if start is not None: #if you are resuming
            req = Request(url) #create a request
            req.headers["Range"] = "bytes=%s-%s" %(start, self.fileSize) #set where you want to start downloading
            self.u = urlopen(req) #create the connection
        else:
            self.u = urlopen(url) #create the connection
        f = open(self.fileName, "ab") #create or append the file
        self.fileSize = int(self.u.getheader("Content-Length")) #set the file size
        self.szDownloaded = 0
        if start is not None: #if resuming
            self.szDownloaded = start #downloaded = where you started
        block_sz = 8192 #how many bytes do you want to download per interaction
        while True: #download block_sz bytes per interaction
            buffer = self.u.read(block_sz) #download the bytes
            if not buffer: #if there is nothing, download ok
                self.status = 1 # value 1 = "Download complete"
                break
            self.szDownloaded += len(buffer) #append the downloaded
            f.write(buffer) #write bytes on file
            self.status = 0 #value 0 = "Downloading
            print(self.szDownloaded) #show how many bytes were downloaded
            if self.isPaused is True: #if is pause, go away
                break
        f.close()
     def puseDownload(self):
        self.isPaused = True
        #save a file with the download status, then I'll be able to resume it Make a backup copy of existing rules
     def resumeDownload(self):
        #load information in status file, like how much were downloaded, ...
        #if you are in the same instance that the download were started, everything is already loaded
        self.isPaused = False
        self.startDownload(self.url, self.szDownloaded) #start the download with initial buffer

#test our  code

f = FileDownloader() 
f.startDownload("https://github.com/aron-bordin/Tyrant-Sql/archive/master.zip")
print("ok")
