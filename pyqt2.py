from PyQt5.QtWidgets import QApplication , QWidget, QMessageBox , QComboBox , QRadioButton , QLineEdit,QVBoxLayout,QHBoxLayout,QLabel,QPushButton
import json



class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.v_main = QVBoxLayout()
        self.jins_h = QHBoxLayout()
        self.shaxar = QHBoxLayout()
        self.btn_h = QHBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name....")

        self.second_edit = QLineEdit()
        self.second_edit.setPlaceholderText("Second....")

        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Age....")


        self.jins_lbl = QLabel("Jins")
        self.male_r = QRadioButton('male')
        self.male_r.setChecked(True)
        self.female_r = QRadioButton('female')



        self.shaxar_lbl = QLabel("shaxar")
        self.shaxar_combo = QComboBox()
        self.tuman_combo = QComboBox()


        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.ok)
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(exit)
    

        self.jins_h.addWidget(self.jins_lbl)
        self.jins_h.addWidget(self.male_r)
        self.jins_h.addWidget(self.female_r)

        self.shaxar.addWidget(self.shaxar_lbl)
        self.shaxar.addWidget(self.shaxar_combo)
        self.shaxar_combo.addItems(["Toshkent","Jizzah","Samarqand"])
        self.shaxar_combo.activated[str].connect(self.clicked_city)





        self.btn_h.addWidget(self.btn_ok)
        self.btn_h.addWidget(self.btn_exit)


        self.v_main.addWidget(self.name_edit)
        self.v_main.addWidget(self.second_edit)
        self.v_main.addWidget(self.age_edit)
        self.v_main.addLayout(self.jins_h)
        self.v_main.addLayout(self.shaxar)
        self.v_main.addWidget(self.tuman_combo)
        self.v_main.addLayout(self.btn_h)
        
        self.setLayout(self.v_main)


    def clicked_city(self, city):
        if city == "Toshkent":
            self.tuman_combo.clear()
            self.tuman_combo.addItems(["Sergeli tumani","Chilonzor tumani","Yunusobod tumani"])
        elif city=="Jizzah":
            self.tuman_combo.clear()
            self.tuman_combo.addItems(["Zomin tumani","Zarbdor tumani","Yangiobod tumani"])            

        elif city=="Samarqand":
            self.tuman_combo.clear()
            self.tuman_combo.addItems(["Nurobod tumani","Oqdaryo tumani","Jomboy tumani"])    


    def ok(self):
        data = {}
        name = self.name_edit.text()
        second = self.second_edit.text()
        age = self.age_edit.text()

        if self.male_r.isChecked():
            jins = "male"
        else:
            jins = "female"

        shaxar = self.shaxar_combo.currentText()
        tuman = self.tuman_combo.currentText()
        
        if name and second and age and jins and tuman:

            data = {'name': name,'second':second,'age':age,'jins':jins,'shaxar':shaxar,'tuman':tuman}
            
            f = open("test.json", "r")
            loaded = json.load(f)
            loaded.append(data)
            f.close()
            f = open("test.json", "w")
            json.dump(loaded, f, indent=4)
            f.close()
            self.msgc = QMessageBox()
            self.msgc.setText("Muvaffaqiyatli!")
            self.msgc.setIcon(QMessageBox.Information)
            self.name_edit.clear()
            self.second_edit.clear()
            self.age_edit.clear()
            self.tuman_combo.clear()
            self.msgc.exec_()

        else:
            self.msg = QMessageBox()
            self.msg.setText("Barchasini toldirishingiz kerak")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()
app = QApplication([])
win = widget()

win.show()
app.exec_()



        