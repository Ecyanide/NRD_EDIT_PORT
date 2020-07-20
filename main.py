import sys , os
sys.path.insert(0, "src/")
from NetRedirect_Creaet_Port import*

if __name__ == '__main__':
    try:
        NetRedirect = open("NetRedirect.dll", "rb").read()
        _ = creaet_port()
        _.NetRedirect = NetRedirect
        _.pull_port()
    except:
        print(" ไม่พบไฟล์ NetRedirect.dll ใน folder นี้ ")
        input(" Press enter and exit")
        os._exit()
