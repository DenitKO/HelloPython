import sys
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from ui import Ui_MainWindow
from pytube import YouTube

class DownloadYouTube(QtWidgets.QMainWindow):
    def __init__(self):
        super(DownloadYouTube, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.progress(0)
        self.url = ''
        self.setWindowTitle('YouTube Скачивалка')
        self.setWindowIcon(QIcon('img/icon.png'))
        self.ui.input_folder_btn.clicked.connect(self.select)
        self.ui.save_in_Btn.clicked.connect(self.download_video)
        self.ui.check_btn.clicked.connect(self.check)


    def download_video(self):
        try:
            self.url = self.ui.input_url.text()
            my_video = YouTube(self.url)
            video_quality = my_video.streams.get_highest_resolution()
            video_quality.download(self.ui.input_folder.text())
            self.progress(100)
        except Exception:
            pass

    
    def download_image(self):
        link = self.url[int(self.url.find('?'))+3:]
        if link.find('=') > 11:
            link = link[:11]
        image_bytes = requests.get(f'https://i.ytimg.com/vi/{link}/maxresdefault.jpg').content
        with open(f'{__file__[:-7]}img\sddefault.jpg', 'wb') as file:
            file.write(image_bytes)
    
    def check(self):
        try:
            self.url = self.ui.input_url.text()
            my_video = YouTube(self.url)
            self.ui.video_title.setPlaceholderText(my_video.title)
            self.download_image()
            self.ui.video_capture.setPixmap(QtGui.QPixmap(f'{__file__[:-7]}img\sddefault.jpg'))
            self.ui.video_capture.setScaledContents(True)
        except Exception as error:
            print(error)
                

    def select(self):
        self.file = QtWidgets.QFileDialog.getExistingDirectory(self, "Select file")
        if self.file != "":
            self.ui.input_folder.setText(self.file)
        else:
            pass 

    def progress(self, size):
        self.ui.progressBar.setValue(size)

def main():
        app = QtWidgets.QApplication([])
        application = DownloadYouTube()
        application.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    main()