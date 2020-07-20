from struct import *
import os


class creaet_port():
    def __init__(self):
        self.NetRedirect = None


    def create_new_dll(self,port):
        Prot_Bytes = pack('h', port)
        dll = list(self.NetRedirect)
        dll[3115:3117] = Prot_Bytes[0],Prot_Bytes[1]
        with open(f"Net/NetRedirect_{port}.dll", 'wb') as w:
            w.write(bytes(dll))
            print(f"สร้างไฟล์ NetRedirect_{port}.dll สำเร็จ")

    def pull_port(self):
        while True:
            Port = input(" ใส่ Port ที่คุณต้องการ : ")
            if "-" in Port:
                start, end = Port.split("-")
                try:
                    if int(start) > int(end):
                        print(f" เริ่มจาก Port เริ่มต้นต้องมีค่าน้อยกว่า Port สุดท้าย เช่น {end} - {start}")
                    elif len(start) and len(end) < 4:
                        print(f" Port ต้องมีความยาวเท่ากับ 4 ")
                    else:
                        for i in range(int(start), int(end)):
                            self.create_new_dll(i)
                except:
                    print(" port ต้องมีค่าเป็นตัวเลขเท่านั้น")
            else:
                if len(Port) == 4:
                    try:
                        self.create_new_dll(int(Port))
                    except:
                        print(" port ต้องมีค่าเป็นตัวเลขเท่านั้น")
                else:
                    print(" Port ต้องมีความยาวเท่ากับ 4")


