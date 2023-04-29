# @File run_demo_main PY.
# @Software:PyCharm
# Created by Dr. Jinjun Bian Email: jinjunbicu@163.com
# @time: 1:08 2023/4/28

import sys
import mainwinmenutoolbar

from PyQt6.QtWidgets import QApplication, QMainWindow

if __name__ =="__main__":
    app =  QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui= mainwinmenutoolbar.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())