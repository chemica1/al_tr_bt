from pywinauto import application, timings
import os, time

# 실전투자 여부
REAL_TRADING = False

app = application.Application()
app.start('C:/KiwoomFlash3/bin/nkministarter.exe')

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

id_ctrl = dlg.Edit0
id_ctrl.SetFocus()
id_ctrl.TypeKeys('chemica1')

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('eogh2647')

if REAL_TRADING:
    # 공인인증서 암호 저장창
    cert_ctrl = dlg.Edit3
    cert_ctrl.SetFocus()
    cert_ctrl.TypeKeys('chemica!1e1180')

    btn_ctrl = dlg.Button0
    btn_ctrl.Click()
else:
    btn_ctrl = dlg.Button0
    btn_ctrl.Click()

    time.sleep(1)

    dlg2 = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title='번개3'))
    btn_ctrl2 = dlg2.Button1
    btn_ctrl2.Click()

time.sleep(60)
os.system("taskkill /im NKmini.exe /f")