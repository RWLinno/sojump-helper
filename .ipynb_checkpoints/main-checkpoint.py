## 问卷星社区互填助手 By RWLinno 2023/8/1
## 使用方法：把社区页面的html存到当前目录的read.txt，然后直接按按钮即可。
import sys
import requests
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html
import re
import auto
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextBrowser, QVBoxLayout, QWidget

def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"找不到文件：{filename}")
    except IOError as e:
        print(f"读取文件时出现错误：{str(e)}")

def extract_href_content(html_text):
    pattern = r"href='/vm/([^']*)'"
    matches = re.findall(pattern, html_text)
    return matches

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 主窗口
        self.setWindowTitle("问卷星社区互填助手")
        # 提示标签
        self.url_label = QLabel("请将网站代码保存到当前目录的page.txt，随后点击按钮。")
        # 解析结果
        self.text = QTextBrowser()
        self.text.setText("")
        self.text.resize(200,160)
        # 开始按钮
        self.open_button = QPushButton("开始解析")
        self.open_button.clicked.connect(self.open_page)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.text)
        layout.addWidget(self.open_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_page(self):
        self.text.setPlainText("")
        page_content = read_text_file('page.txt')
        links = extract_href_content(page_content)
        print(links)
        for link in links:
            new_url = 'https://www.wjx.cn/vm/' + link
            result = auto.auto_fillout(new_url)
            if result == True:
                print("成功获取点数:"+new_url)
                self.text.append("已完成:"+new_url)
            else:
                print("未能获取点数:"+new_url)
                self.text.append("已完成:"+new_url)
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())