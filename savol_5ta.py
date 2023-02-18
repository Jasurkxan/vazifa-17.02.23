from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QRadioButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vMainLay = QVBoxLayout()
        self.Question1()



    
    def Question1(self):
        self.natija=0
        self.savol=QLabel("Qaysi qushning kozlari miyasidan kattaroq boladi?")
        self.savol.setStyleSheet("color:red;font-size:15px")

        self.v1 = QRadioButton("Butgut")
        self.v2 = QRadioButton('Lochin')
        self.v3 = QRadioButton('Tuyaqush')
        self.v4 = QRadioButton('Kabutar')

        self.lst=[self.v1,self.v2,self.v3,self.v4]

        self.Nextbtn = QPushButton("Next")

        self.Nextbtn.clicked.connect(self.Question2)


        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.Nextbtn)
        self.setLayout(self.vMainLay)


      

    def Question2(self):
        if self.v3.isChecked(): 
            self.natija=1
        for i in self.lst:
            i.hide()
            i.setChecked(False)
        self.savol.hide()
        self.Nextbtn.hide()


        self.savol=QLabel("Eng kop haqorat eshitadigan kishilar kimlar?")
        self.savol.setStyleSheet("color:red;font-size:15px")

        self.v1 = QRadioButton("Hackerlar")
        self.v2 = QRadioButton('Futbol hakamlari')
        self.v3 = QRadioButton("Futbolchilar")
        self.v4 = QRadioButton("Lolilar")

        self.lst=[self.v1,self.v2,self.v3,self.v4]

        self.Nextbtn = QPushButton("Next")
        self.Nextbtn.clicked.connect(self.Question3)

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.Nextbtn)
        self.setLayout(self.vMainLay)


    def Question3(self):
        if self.v2.isChecked(): 
            self.natija+=1
        for i in self.lst:
            i.hide()
            i.setChecked(False)
        self.savol.hide()
        self.Nextbtn.hide()


        self.savol=QLabel("Nima uchun inson orqasiga qaraydi?")
        self.savol.setStyleSheet("color:red;font-size:15px")

        self.v1 = QRadioButton("Kiyimini togrilash uchun")
        self.v2 = QRadioButton("Orqasida kim borligini bilish uchuin")
        self.v3 = QRadioButton("Chunki orqasida kozi yoq")
        self.v4 = QRadioButton("Kimdur chaqirgani uchun")

        self.lst=[self.v1,self.v2,self.v3,self.v4]

        self.Nextbtn = QPushButton("Next")
        self.Nextbtn.clicked.connect(self.Question4)

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.Nextbtn)
        self.setLayout(self.vMainLay)


    def Question4(self):
        if self.v3.isChecked(): 
            self.natija=3
        for i in self.lst:
            i.hide()
            i.setChecked(False)
        self.savol.hide()
        self.Nextbtn.hide()


        self.savol=QLabel("Tizza bogimlari 4 ta bolgan yagona sutemizuvchi hayvon qaysi?")
        self.savol.setStyleSheet("color:red;font-size:15px")

        self.v1 = QRadioButton("OT")
        self.v2 = QRadioButton("Tuya")
        self.v3 = QRadioButton("Karkidon")
        self.v4 = QRadioButton("Fil")

        self.lst=[self.v1,self.v2,self.v3,self.v4]

        self.Nextbtn = QPushButton("Next")
        self.Nextbtn.clicked.connect(self.Question5)

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.Nextbtn)
        self.setLayout(self.vMainLay)


    def Question5(self):
        if self.v4.isChecked(): 
            self.natija=4
        for i in self.lst:
            i.hide()
            i.setChecked(False)
        self.savol.hide()
        self.Nextbtn.hide()


        self.savol=QLabel("Diyego, Manfrid va Sid qaysi “davrda” dostlashadi?")
        self.savol.setStyleSheet("color:red;font-size:15px")

        self.v1 = QRadioButton("Tosh davrida")
        self.v2 = QRadioButton("Muzlik davrida")
        self.v3 = QRadioButton("Ular dostlashishmagan")
        self.v4 = QRadioButton("Bilmayman")

        self.lst=[self.v1,self.v2,self.v3,self.v4]

        self.Result = QPushButton("RESULT")
        self.Result.clicked.connect(self.result)

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.Result)
        self.setLayout(self.vMainLay)


    def result(self):
        if self.v2.isChecked(): 
           self.natija=5
        for i in self.lst:
            i.hide()
            i.setChecked(False)
        self.savol.hide()
        self.Result.hide()
 
        self.resultt=QLabel(f"Siz {self.natija} ball topladingiz!")
        self.resultt.setStyleSheet("font-size:45px;")
        
        self.vMainLay.addWidget(self.resultt)

app = QApplication([])
obj = Window()
obj.show()
app.exec_()