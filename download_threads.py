from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib2
import urllib
from bs4 import BeautifulSoup as bs
import os


path = './downloads/'
rsite = 'http://mangalife.us/read-online/'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


class MDownloadThread(QThread):

    def __init__(self, list, sname):
        QThread.__init__(self)
        self.list = list
        self.sname = sname

    '''
    def __del__(self):
        self.wait()
    '''

    def downloadChapters(self):
        for i in self.list:
            site = rsite + self.sname + '-chapter-' + i + '-page-1.html'
            req = urllib2.Request(site, headers=hdr)
            page = urllib2.urlopen(req)
            content = page.read()
            soup = bs(content, 'lxml')
            k = soup.find_all('select', class_='input-xs hidden-xs PageSelect')
            y = k[0].find_all('option')

            z = path + self.sname + '/' + i

            if os.path.isdir(z)==False:
                os.makedirs(z)
            self.emit(SIGNAL('ChapterLoaded'), len(y))
            for u in xrange(1, len(y) + 1):
                site1 = rsite + self.sname + '-chapter-' + i + '-page-' + str(u) + '.html'
                req1 = urllib2.Request(site1, headers=hdr)
                page1 = urllib2.urlopen(req1)
                content1 = page1.read()
                soup1 = bs(content1, 'lxml')

                k = soup1.find_all('img', class_='CurImage', src=True)

                fullfilename = os.path.join(path + self.sname + '/' + i + '/', str(u) + '.jpg')

                if os.path.exists(fullfilename)==False:
                    urllib.urlretrieve(k[0]['src'], fullfilename)
                self.emit(SIGNAL('ChapterPageDownloaded'),u)
            print('Downloading '+i+' completed!!!')
            self.emit(SIGNAL('ChapterDownloaded'), self.list.index(i)+1)

            if self.list.index(i)+1 != len(self.list):
                self.emit(SIGNAL('ChapterDownloadCompleted'), 0)



    def run(self):
        self.downloadChapters()
        print('Download Completed!!!')


