# coding=utf-8
from pywinauto import Application
import time


class Cal(object):
    #path
    path='C:\WINDOWS\system32\calc.exe'

    #name
    window=u'计算器'

    #automation ID
    btn1='num1Button'
    btn2='num2Button'
    btnPlus='plusButton'
    btnEqual='equalButton'
    txtResult='CalculatorResults'


class action(object):
    def __init__(self):
        self.app=Application(backend='uia')

    def run(self,tool):
        self.app.start(tool)
        time.sleep(1)

    def connect(self,window_name):
        self.app.connect(title=window_name)
        time.sleep(1)

    def close(self,window_name):
        self.app[window_name].close()

    def click(self,window_name,btn_id):
        dlg=self.app[window_name]
        btn=dlg.window(auto_id=btn_id)
        btn.click()
        time.sleep(1)

    def text(self,window_name,re):
        dlg = self.app[window_name]
        txt = dlg.window(auto_id=re)
        return txt.texts()[0]


def test_cal():
    app=action()
    cal=Cal()
    app.run(cal.path)
    app.connect(cal.window)
    app.click(cal.window,cal.btn1)
    app.click(cal.window, cal.btnPlus)
    app.click(cal.window,cal.btn2)
    app.click(cal.window, cal.btnEqual)
    result=app.text(cal.window,cal.txtResult)
    app.close(cal.window)

    assert result=='显示为 3'