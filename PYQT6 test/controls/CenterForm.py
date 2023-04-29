# @File CenterForm PY.
# @Software:PyCharm
# Created by Dr. Jinjun Bian Email: jinjunbicu@163.com
# @time: 11:26 2023/4/29
# QDesktopWidget

import sys
from PyQt6.QtWidgets import  QMainWindow, QApplication
from PyQt6.QtGui import QDesktopWidget


class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super(CenterForm,self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        #设置窗口的尺寸
        self.resize(400,300)

    def center(self):



if __name__ =="__main__":
    app=QApplication(sys.argv)
    main = CenterForm()
    main.show()

    sys.exit(app.exec())
