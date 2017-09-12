# coding=utf-8
from pywinauto import Application

if __name__ == '__main__':
    app=Application().start(r"C:\WINDOWS\system32\notepad.exe")
    app.notepad.MenuSelect(u"帮助->关于记事本")
    app[u'关于记事本'][u'确定'].Click()
    app[u'无标题-记事本'].Close()