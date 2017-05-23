from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import manga
import urllib2
from bs4 import BeautifulSoup as bs
from download_threads import MDownloadThread
from elements import DownloadChaptersStatus, DownloadChapterPageStatus
import sqlite3
import re

con = sqlite3.connect('MangaLife.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM MangaList")



hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

sc = []


class ChapterItem(QListWidgetItem):
    def __init__(self):
        super(ChapterItem, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
        self.setCheckState(Qt.Unchecked)




class GetChaptersThread(QThread):

    def __init__(self, link):
        QThread.__init__(self)
        self.link = link

    def __del__(self):
        self.wait()

    def SIExtraxct(self):
        chap=[]
        site=str(self.link)
        req = urllib2.Request(site, headers=hdr)
        page = urllib2.urlopen(req)
        content = page.read()
        soup = bs(content, 'lxml')
        chapters_list = soup.find_all('div', class_='list chapter-list')
        k=chapters_list[0]
        for a in k.find_all('a'):
            c=a.text
            chap.append(c[0:len(c)-10])
        return chap

    def run(self):
        p= self.SIExtraxct()
        self.emit(SIGNAL('ChaptersCollected'), p)




class MangaApp(QMainWindow, manga.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mangaLinks = []
        self.MangaModel = QStandardItemModel(self)
        self.FilterModel = QSortFilterProxyModel(self)
        self.FilterModel.setFilterCaseSensitivity(0)
        self.FilterModel.setSourceModel(self.MangaModel)

        self.DownloadTable.setColumnCount(3)
        self.DownloadTable.setHorizontalHeaderLabels(['Manga', 'Manga Status', 'Chapter Status'])
        self.DownloadTable.horizontalHeader().setStretchLastSection(True)
        self.SearchButton.clicked.connect(self.searchChapters)
        self.CheckAll.stateChanged.connect(self.checkAllChapters)
        self.CheckSelected.stateChanged.connect(self.checkSelectedChapters)
        self.DownloadButton.clicked.connect(self.startDownload)
        self.updateMangaList()
        self.MangaList.setModel(self.FilterModel)
        self.MangaSearchInput.textChanged.connect(self.FilterModel.setFilterRegExp)
        self.MangaList.doubleClicked.connect(self.mangaClicked)

    def updateMangaList(self):
        while True:
            row = cur.fetchone()
            if row == None:
                break
            idx = self.MangaModel.rowCount()
            item = QStandardItem(row[0])
            self.MangaModel.setItem(idx, item)
            self.mangaLinks.append(row[1])

    def mangaClicked(self):
        i = self.MangaList.selectedIndexes()[0].row()
        self.LinkInput.setText(self.mangaLinks[i])
        self.searchChapters()


    def searchChapters(self):
        if self.LinkInput.text()!='':
            self.ChapterLinks.clear()
            self.getChapters = GetChaptersThread(self.LinkInput.text())
            self.getChapters.start()
            status.setIcon(QIcon('./img/processing.png'))
            status.setText('Searching...')
            self.connect(self.getChapters, SIGNAL('ChaptersCollected'), self.updateList)

    def updateList(self, y):
        for e in y:
            item = ChapterItem()
            item.setText(e)
            self.ChapterLinks.addItem(item)
        status.setText('Chapters Collected!!!')
        status.setIcon(QIcon('./img/completed.png'))
        self.getChapters.terminate()


    def checkAllChapters(self):
        if self.CheckAll.checkState()==2:
            self.CheckSelected.setChecked(False)
            c = self.ChapterLinks.count()
            for n in xrange(c):
                item = self.ChapterLinks.item(n)
                item.setCheckState(2)

        elif self.CheckAll.checkState()==0:
            self.CheckSelected.setChecked(False)
            c = self.ChapterLinks.count()
            for n in xrange(c):
                item = self.ChapterLinks.item(n)
                item.setCheckState(0)


    def checkSelectedChapters(self):
        if self.CheckSelected.checkState()==2:
            self.CheckAll.setChecked(False)
            l = form.ChapterLinks.selectedItems()
            for item in l:
                item.setCheckState(2)

        elif self.CheckSelected.checkState()==0:
            l = form.ChapterLinks.selectedItems()
            for item in l:
                item.setCheckState(0)

    def startDownload(self):
        sc = []
        self.CheckAll.setCheckState(0)
        self.CheckSelected.setCheckState(0)
        c = self.ChapterLinks.count()
        for y in xrange(c):
            item = self.ChapterLinks.item(y)
            if item.checkState()==2:
                t = str(item.text())
                v = re.findall(r'\d+', t)
                sc.append(v[0])

        sc.reverse()

        s = self.LinkInput.text().split('/')
        s = s[-1]
        r = self.DownloadTable.rowCount()

        if sc !=[]:
            self.dc = MDownloadThread(sc, str(s))
            item = QTableWidgetItem(s)
            self.DownloadTable.insertRow(r)
            self.DownloadTable.setItem(r , 0, item)
            self.dc.start()
            self.o = DownloadChaptersStatus( 0, len(sc))
            self.p = DownloadChapterPageStatus()
            self.DownloadTable.setCellWidget(r, 1, self.o)
            self.DownloadTable.setCellWidget(r, 2, self.p)
            self.o.connect(self.dc, SIGNAL('ChapterDownloaded'), self.o.updateLabel)
            self.p.connect(self.dc, SIGNAL('ChapterLoaded'), self.p.updateTotal)
            self.p.connect(self.dc, SIGNAL('ChapterPageDownloaded'), self.p.updatePage)
            self.p.connect(self.dc, SIGNAL('ChapterDownloadCompleted'), self.p.updateAgain)
            self.MainWidget.setCurrentIndex(1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MangaApp()
    status = QPushButton()
    status.setFlat(True)
    status.setIcon(QIcon('./img/completed.png'))
    status.setText('Ready')
    form.StatusBar.addWidget(status)
    form.ChapterLinks.setSelectionMode(QAbstractItemView.ExtendedSelection)
    form.show()
    app.exec_()