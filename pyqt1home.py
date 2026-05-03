from PyQt5.QtWidgets import QApplication, QWidget , QLineEdit ,QLabel ,QHBoxLayout,QVBoxLayout ,QPushButton

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.gwin = QVBoxLayout()
        self.main = QVBoxLayout()
        self.bwin1 = QHBoxLayout()
        self.bwin2 = QHBoxLayout()
        self.bwin3 = QHBoxLayout()
        self.bwin4 = QHBoxLayout()
        self.data = str()
        self.tenglik = 0




        self.natija = QLabel()

        self.b1 = QPushButton("1")
        self.b1.clicked.connect(self.click1)
        self.b2 = QPushButton("2")
        self.b2.clicked.connect(self.click2)
        self.b3 = QPushButton("3")
        self.b3.clicked.connect(self.click3)
        self.bc = QPushButton("c")
        self.bc.clicked.connect(self.clickc)
        
        self.bwin1.addWidget(self.b1)
        self.bwin1.addWidget(self.b2)
        self.bwin1.addWidget(self.b3)
        self.bwin1.addWidget(self.bc)


        
        self.b4 = QPushButton("4")
        self.b4.clicked.connect(self.click4)
        self.b5 = QPushButton("5")
        self.b5.clicked.connect(self.click5)
        self.b6 = QPushButton("6")
        self.b6.clicked.connect(self.click6)
        self.bminus = QPushButton("-")
        self.bminus.clicked.connect(self.clickminus)
        self.bwin2.addWidget(self.b4)
        self.bwin2.addWidget(self.b5)
        self.bwin2.addWidget(self.b6)
        self.bwin2.addWidget(self.bminus)



        self.b7 = QPushButton("7")
        self.b7.clicked.connect(self.click7)
        self.b8 = QPushButton("8")
        self.b8.clicked.connect(self.click8)
        self.b9 = QPushButton("9")
        self.b9.clicked.connect(self.click9)
        self.bplus = QPushButton("+")
        self.bplus.clicked.connect(self.clickplus)

        self.bwin3.addWidget(self.b7)
        self.bwin3.addWidget(self.b8)
        self.bwin3.addWidget(self.b9)
        self.bwin3.addWidget(self.bplus)


        self.bbolish = QPushButton("/")
        self.bbolish.clicked.connect(self.clickboluv)
        self.b0 = QPushButton("0")
        self.b0.clicked.connect(self.click0)
        self.bkopaytirish = QPushButton("*")
        self.bkopaytirish.clicked.connect(self.clickkopaytirish)
        self.bteng = QPushButton("=")
        self.bteng.clicked.connect(self.clickteng)

        self.bwin4.addWidget(self.bbolish)
        self.bwin4.addWidget(self.b0)
        self.bwin4.addWidget(self.bkopaytirish)
        self.bwin4.addWidget(self.bteng)


        self.gwin.addWidget(self.natija)
        self.main.addLayout(self.gwin)
        self.main.addLayout(self.bwin1)
        self.main.addLayout(self.bwin2)
        self.main.addLayout(self.bwin3)
        self.main.addLayout(self.bwin4)
        self.setLayout(self.main)

    def click1(self):
        self.data += "1"
        self.natija.setText(f"{self.data}")
    def click2(self):
        self.data += "2"
        self.natija.setText(f"{self.data}")
    def click3(self):
        self.data += "3"
        self.natija.setText(f"{self.data}")
    def clickc(self):
        self.data = ""
        self.natija.setText(f"{self.data}")



    def click4(self):
        self.data += "4"
        self.natija.setText(f"{self.data}")        
    def click5(self):
        self.data += "5"
        self.natija.setText(f"{self.data}")
    def click6(self):
        self.data += "6"
        self.natija.setText(f"{self.data}")
    def clickminus(self):
        self.data += "-"
        self.natija.setText(f"{self.data}")



    def click7(self):
        self.data += "7"
        self.natija.setText(f"{self.data}")
    def click8(self):
        self.data += "8"
        self.natija.setText(f"{self.data}")
    def click9(self):
        self.data += "9"
        self.natija.setText(f"{self.data}")
    def clickplus(self):
        self.data += "+"
        self.natija.setText(f"{self.data}")



    def clickboluv(self):
        self.data += "/"
        self.natija.setText(f"{self.data}")
    def click0(self):
        self.data += "0"
        self.natija.setText(f"{self.data}")
    def clickkopaytirish(self):
        self.data += "*"
        self.natija.setText(f"{self.data}")
    
    
    def clickteng(self):
        self.tenglik = eval(self.data)
        self.natija.setText(f"{self.tenglik}")


app = QApplication([])
win = window()

win.show()
app.exec_()