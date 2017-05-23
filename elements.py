from PyQt4.QtGui import QLabel, QProgressBar


class DownloadChaptersStatus(QLabel):
    def __init__(self, i, n):
        super(DownloadChaptersStatus, self).__init__()
        self.n = n
        self.i = i
        self.initUI()

    def initUI(self):
        self.setText('%s/%s'%(self.i, self.n))


    def updateLabel(self, k):
        self.setText('%s/%s' % (k, self.n))


class DownloadChapterPageStatus(QProgressBar):
    def __init__(self):
        super(DownloadChapterPageStatus, self).__init__()
        self.initUI()

    def initUI(self):
        self.setMaximum(1)
        self.setValue(0)

    def updateTotal(self, k):
        self.setMaximum(k)

    def updatePage(self, k):
        self.setValue(k)

    def updateAgain(self, k):
        self.setValue(k)




