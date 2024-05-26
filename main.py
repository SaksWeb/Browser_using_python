import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize the browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar
        navbar = QToolBar("Navigation")
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction(QIcon('icons/back.png'), 'Back', self)
        back_btn.setStatusTip('Go back to the previous page')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction(QIcon('icons/forward.jpg'), 'Forward', self)
        forward_btn.setStatusTip('Go forward to the next page')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction(QIcon('icons/reload.png'), 'Reload', self)
        reload_btn.setStatusTip('Reload the current page')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Stop button
        stop_btn = QAction(QIcon('icons/stop.png'), 'Stop', self)
        stop_btn.setStatusTip('Stop loading the current page')
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Home button
        home_btn = QAction(QIcon('icons/home.jpg'), 'Home', self)
        home_btn.setStatusTip('Go to the home page')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setStatusTip('Enter URL')
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update URL bar when URL changes
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        """Navigate to the home page"""
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        """Navigate to the URL entered in the URL bar"""
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        """Update the URL bar to display the current URL"""
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Saksham's Browser")
    window = MainWindow()
    app.exec_()
