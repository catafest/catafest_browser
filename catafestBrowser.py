import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Simple catafest browser')
        self.setWindowIcon(QIcon('catafest_logo.png'))
        
        self.resize(900, 600)
        self.show()
        
        
        self.browser = QWebEngineView()
        url = 'http://google.com'
        
        self.browser.setUrl(QUrl(url))
        
        self.setCentralWidget(self.browser)
        
        navigation_bar = QToolBar('Navigation')
        
        navigation_bar.setIconSize(QSize(32, 32))
        
        self.addToolBar(navigation_bar)      
        
        back_button = QAction(QIcon('back.png'), 'Back', self)
        next_button = QAction(QIcon('next.png'), 'Forward', self)
        stop_button = QAction(QIcon('stop.png'), 'Stop', self)
        reload_button = QAction(QIcon('refresh.png'), 'Reload', self)
        about_button = QAction(QIcon('catafestBrowser.png'), 'About', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)
        about_button.triggered.connect(self.about)
        
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)
        navigation_bar.addAction(about_button)
        
        self.urlbar = QLineEdit()
        
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def about(self):
        about_dialog = QDialog(self)
        about_dialog.resize(100, 76)
        about_dialog.setWindowTitle("About catafest browser!")
        about_layout = QVBoxLayout()
        message_one = QLabel("This is a simple browser created by catafest!")
        message_two = QLabel("This browser has low security!")
        about_layout.addWidget(message_one)
        about_layout.addWidget(message_two)
        about_dialog.setLayout(about_layout)
        about_dialog.exec()

if __name__ == '__main__':  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()