from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import hr_design
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QTimer
from itertools import zip_longest
from datetime import *
import webbrowser
from itertools import zip_longest
from Loding_window import Ui_mainWindow
from bs4 import BeautifulSoup
import requests
from files import window



def web2():
    try:
        list20=[]
        r1=requests.get('https://Hrapp.m0221.repl.co')
        s1=r1.content
        s2=BeautifulSoup(s1,"lxml")
        x1=s2.find_all('h1',{"class":"p"})
        for i in range(len(x1)):
            list20.append(x1[i].text)

        if list20[0]=='0':
            m20=QtWidgets.QMessageBox.warning(program,'Hr app','هناك تحديث للتطبيق')
        else:
            pass
    except:
        m21=QtWidgets.QMessageBox.warning(program,'Hr app','حدث خطأ')



def reports():
    window.show()


def t20():
    c2=c1.currentText()
    time_now=datetime.now()
    time_now2=time_now.strftime("%H:%M:%S %p")
    l20.setText("الوقت : "+time_now2)
    if c2=='العربية':
        l4.setText("الصفحة الرئيسية")
        b3.setText("موظف جديد")
        b4.setText("تسجيل حضور")
        b5.setText("تسجيل غياب")
        b6.setText("قائمة الموظفين")
        b7.setText("المرتبات")
        b8.setText("مساعدة")
        b9.setText("تغيير الاسم")
        b10.setText("تغيير كلمة المرور")
        b20.setText("التقارير")
        b2.setText("خروج")
        b5.resize(200,50)
    else:
        l4.setText("home page")
        b3.setText("new user")
        b4.setText("Record Absence")
        b5.setText("Attendance Registration")
        b5.resize(230,50)
        b5.setIconSize(QtCore.QSize(30,30))
        b6.setText("list of users")
        b7.setText("salaries")
        b8.setText("help")
        b9.setText("Name change")
        b10.setText("Change Password")
        b20.setText("reports")
        b2.setText("exit")

def users11():
    def users5():
        Time2=datetime.now()
        users10=users00.currentItem()
        with open("Time","a") as save_time1:
            save_time1.write(users10.text()+'\n')
            save_time1.close()
        with open("Time1","a") as save_time10:
            save_time10.write("%s %s\%s \n"%(users10.text(),Time2.month,Time2.day))
            save_time10.close()
        m11=QtWidgets.QMessageBox.about(d6,'Hr app','تم تسجيل غياب بنجاح ل '+users10.text())
    d6=QtWidgets.QDialog(program)
    d6.setFixedHeight(600)
    d6.setFixedWidth(600)
    d6.setStyleSheet(hr_design.d0)
    d6.setWindowTitle('تسجيل غياب')
    users00=QtWidgets.QListWidget(d6)
    users00.resize(580,580)
    users00.move(10,1)
    users00.setStyleSheet(hr_design.i0)
    users0=[]
    with open('users','r') as read_users1:
        users0=read_users1.read().rstrip('\n').split('\n')
        read_users1.close()
    number10=0
    for read_users3 in users0:
        users00.insertItem(0,users0[int(number10)])
        number10+=1
    users00.clicked.connect(users5)
    d6.show()

def users1():
    def users4():
        Time1=datetime.now()
        users0=users3.currentItem()
        with open("Time","a") as save_time:
            save_time.write(users0.text()+'\n')
            save_time.close()
        with open("Time1","a") as save_time00:
            save_time00.write("%s %s\%s\n"%(users0,Time1.month,Time1.day))
            save_time00.close()
        m10=QtWidgets.QMessageBox.about(d5,'Hr app','تم تسجيل حضور بنجاح ل '+users0.text())
    d5=QtWidgets.QDialog(program)
    d5.setFixedHeight(600)
    d5.setFixedWidth(600)
    d5.setStyleSheet(hr_design.d0)
    d5.setWindowTitle('تسجيل حضور')
    users3=QtWidgets.QListWidget(d5)
    users3.resize(580,580)
    users3.move(10,1)
    users3.setStyleSheet(hr_design.i0)
    users2=[]
    with open('users','r') as read_users:
        users2=read_users.read().rstrip('\n').split('\n')
        read_users.close()
    number9=0
    for read_users2 in users2:
        users3.insertItem(0,users2[int(number9)])
        number9+=1
    users3.clicked.connect(users4)
    d5.show()
def username():
    def save_username():
        username1=e7.text()
        password1=e2.text()
        with open('username','w') as file5:
            file5.write(username1+'\n')
            file5.write(password1+'\n')
        m9=QtWidgets.QMessageBox.about(d3,'Hr app','تم تغيير اسم المستخدم بنجاح')
    d3=QtWidgets.QDialog(program)
    d3.setStyleSheet(hr_design.d00)
    d3.setWindowTitle('تغيير اسم المستخدم الحالي')
    d3.setFixedHeight(150)
    d3.setFixedWidth(300)
    e7=QtWidgets.QLineEdit(d3)
    e7.resize(200,30)
    e7.move(60,30)
    e7.setStyleSheet(hr_design.e00)
    e7.setPlaceholderText('اسم المستخدم الجديد')
    e7.show()
    b12=QtWidgets.QPushButton('تغيير الاسم',d3)
    b12.setStyleSheet(hr_design.buttons4)
    b12.move(80,80)
    b12.resize(150,30)
    b12.clicked.connect(save_username)
    b12.show()
    d3.show()
def password0():
    def save_password():
        username2=e1.text()
        password3=e2.text()
        password4=e8.text()
        password5=e9.text()
        if password3==password4:
            with open("username",'w') as file6:
                file6.write(username2+'\n')
                file6.write(password5+'\n')
            m10=QtWidgets.QMessageBox.about(d4,'Hr app','تم تغيير كلمة المرور بنجاح')
        else:
            m8=QtWidgets.QMessageBox.warning(d4,'Hr app','كلمة المرور خطأ')
    d4=QtWidgets.QDialog(program)
    d4.setStyleSheet(hr_design.d00)
    d4.setWindowTitle('تغيير اسم المستخدم الحالي')
    d4.setFixedHeight(200)
    d4.setFixedWidth(300)
    e8=QtWidgets.QLineEdit(d4)
    e8.resize(200,30)
    e8.move(60,30)
    e8.setStyleSheet(hr_design.e00)
    e8.setPlaceholderText('كلمة المرور القديمه')
    e8.setEchoMode(QtWidgets.QLineEdit.Password)
    e8.show()
    e9=QtWidgets.QLineEdit(d4)
    e9.resize(200,30)
    e9.move(60,90)
    e9.setStyleSheet(hr_design.e00)
    e9.setPlaceholderText("كلمة المرور الجديدة")
    e9.setEchoMode(QtWidgets.QLineEdit.Password)
    e9.show()
    b13=QtWidgets.QPushButton('تغيير كلمة المرور',d4)
    b13.setStyleSheet(hr_design.buttons4)
    b13.move(120,150)
    b13.resize(150,30)
    b13.clicked.connect(save_password)
    b13.show()
    d4.show()
def web():
    webbrowser.open('Hr_web\\Hr.html')
def x():
    m1=QtWidgets.QMessageBox.question(program,'Hr app','هل تريد الخروج؟')
    if m1==QtWidgets.QMessageBox.Yes:
        exit()
def program2():
    def s1():
        def show1():
            names1=l0.currentItem()
            m2=QtWidgets.QMessageBox.about(d1,'Hr app','اسم الموظف هو '+names1.text())
        d1=QtWidgets.QDialog(program)
        d1.setFixedHeight(600)
        d1.setFixedWidth(600)
        d1.setStyleSheet(hr_design.d0)
        d1.setWindowTitle('قائمه الموظفين')
        l0=QtWidgets.QListWidget(d1)
        l0.resize(580,580)
        l0.move(10,1)
        list1=[]
        try:
            with open('data','r') as f3:
                list1=f3.read().rstrip('\n').split('\n')
                number00=0
                for file0 in list1:
                    l0.insertItem(1,str(list1[int(number00)]))
                    number00+=1
        except Exception as r:
            m3=QtWidgets.QMessageBox.warning(d1,'Hr app','حدث خطأ حاول مره اخري')
            print(r)
        l0.clicked.connect(show1)
        l0.show()
        l0.setStyleSheet(hr_design.i0)
        d1.show()
    def save():
        def save1():
            name1=e3.text()
            number=e4.text()
            number2=e5.text()
            number3=e6.text()
            with open('data','a') as file1:
                file1.write(name1+'\n')
                file1.write(number+'\n')
                file1.write(number2+'\n')
                file1.write(number3+'\n')
            with open('users','a') as file9:
                file9.write(name1+'\n')
                file9.close()
            m2=QtWidgets.QMessageBox.about(program,'Hr app','تم اضافه الموظف بنجاح')
        d2=QtWidgets.QDialog(program)
        d2.setFixedHeight(170)
        d2.setFixedWidth(450)
        d2.setStyleSheet(hr_design.d0)
        d2.setWindowTitle('موظف جديد')
        e3=QtWidgets.QLineEdit(d2)
        e3.resize(200,30)
        e3.move(240,30)
        e3.setStyleSheet(hr_design.e0)
        e3.setPlaceholderText('اسم الموظف')
        e3.show()
        e4=QtWidgets.QLineEdit(d2)
        e4.resize(200,30)
        e4.move(240,70)
        e4.setStyleSheet(hr_design.e0)
        e4.setPlaceholderText('رقم التيلفون')
        e4.show()
        e5=QtWidgets.QLineEdit(d2)
        e5.resize(200,30)
        e5.move(20,30)
        e5.setStyleSheet(hr_design.e0)
        e5.setPlaceholderText('الرقم القومي')
        e5.show()
        e6=QtWidgets.QLineEdit(d2)
        e6.resize(200,30)
        e6.move(20,70)
        e6.setStyleSheet(hr_design.e0)
        e6.setPlaceholderText('الرقم التأميني')
        e6.show()
        b11=QtWidgets.QPushButton('اضافه الموظف',d2)
        b11.setStyleSheet(hr_design.buttons3)
        b11.move(140,130)
        b11.resize(200,30)
        b11.clicked.connect(save1)
        b11.show()
        d2.show()
    name=e1.text()
    password=e2.text()
    list2=[]
    def Money():
        def screen():
            t1.hide()
            b000.hide()
            l3.show()
            l4.show()
            l5.show()
            b3.show()
            b4.show()
            b5.show()
            b6.show()
            b7.show()
            b8.show()
            b9.show()
            b10.show()
        l3.hide()
        l4.hide()
        l5.hide()
        b3.hide()
        b4.hide()
        b5.hide()
        b6.hide()
        b7.hide()
        b8.hide()
        b9.hide()
        b10.hide()
        t1=QtWidgets.QTableWidget(program)
        t1.setColumnCount(31)
        t1.setRowCount(1000000)
        t1.resize(1310,590)
        t1.move(30,1)
        t1.setStyleSheet(hr_design.t)
        t1.show()
        time7=datetime.now()
        time8="%s\%s"%(time7.month,1)
        time9="%s\%s"%(time7.month,2)
        time10="%s\%s"%(time7.month,3)
        time11="%s\%s"%(time7.month,4)
        time12="%s\%s"%(time7.month,5)
        time13="%s\%s"%(time7.month,6)
        time14="%s\%s"%(time7.month,7)
        time15="%s\%s"%(time7.month,8)
        time16="%s\%s"%(time7.month,9)
        time17="%s\%s"%(time7.month,10)
        time18="%s\%s"%(time7.month,11)
        time19="%s\%s"%(time7.month,12)
        time20="%s\%s"%(time7.month,13)
        time21="%s\%s"%(time7.month,14)
        time22="%s\%s"%(time7.month,15)
        time23="%s\%s"%(time7.month,16)
        time24="%s\%s"%(time7.month,17)
        time25="%s\%s"%(time7.month,18)
        time26="%s\%s"%(time7.month,19)
        time27="%s\%s"%(time7.month,20)
        time28="%s\%s"%(time7.month,21)
        time29="%s\%s"%(time7.month,22)
        time30="%s\%s"%(time7.month,23)
        time31="%s\%s"%(time7.month,24)
        time32="%s\%s"%(time7.month,25)
        time33="%s\%s"%(time7.month,26)
        time34="%s\%s"%(time7.month,27)
        time35="%s\%s"%(time7.month,28)
        time36="%s\%s"%(time7.month,29)
        time37="%s\%s"%(time7.month,30)
        list4=[]
        with open("Time",'r') as readfile:
            list4=readfile.read().rstrip('\n').split('\n')
        list5=[]
        with open("Time1",'r') as readfile1:
            list5=readfile1.read().rstrip('\n').split('\n')
        number_1=0
        for users0000 in list4:
            for time_5 in list5:
                if time_5==users0000+' '+time8:
                    t1.setItem(number_1,1, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time9:
                    t1.setItem(number_1,2, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time10:
                    t1.setItem(number_1,3, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time11:
                    t1.setItem(number_1,4, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time12:
                    t1.setItem(number_1,5, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time13:
                    t1.setItem(number_1,6, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time14:
                    t1.setItem(number_1,7, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time15:
                    t1.setItem(number_1,8, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time16:
                    t1.setItem(number_1,9, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time17:
                    t1.setItem(number_1,10, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time18:
                    t1.setItem(number_1,11, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time19:
                    t1.setItem(number_1,12, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time20:
                    t1.setItem(number_1,13, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time21:
                    t1.setItem(number_1,14, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time22:
                    t1.setItem(number_1,15, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time23:
                    t1.setItem(number_1,16, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time24:
                    t1.setItem(number_1,17, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time25:
                    t1.setItem(number_1,18, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time26:
                    t1.setItem(number_1,19, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time27:
                    t1.setItem(number_1,20, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time28:
                    t1.setItem(number_1,21, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time29:
                    t1.setItem(number_1,22, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time30:
                    t1.setItem(number_1,23, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time31:
                    t1.setItem(number_1,24, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time32:
                    t1.setItem(number_1,25, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time33:
                    t1.setItem(number_1,26, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time34:
                    t1.setItem(number_1,27, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time35:
                    t1.setItem(number_1,28, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time36:
                    t1.setItem(number_1,29, QTableWidgetItem('حاضر'))
                elif time_5==users0000+' '+time37:
                    t1.setItem(number_1,30, QTableWidgetItem('حاضر'))
            ####################################################################################
                elif time_5==users0000+' '+time8+' ':
                    t1.setItem(number_1,1, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time9+' ':
                    t1.setItem(number_1,2, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time10+' ':
                    t1.setItem(number_1,3, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time11+' ':
                    t1.setItem(number_1,4, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time12+' ':
                    t1.setItem(number_1,5, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time13+' ':
                    t1.setItem(number_1,6, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time14+' ':
                    t1.setItem(number_1,7, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time15+' ':
                    t1.setItem(number_1,8, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time16+' ':
                    t1.setItem(number_1,9, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time17+' ':
                    t1.setItem(number_1,10, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time18+' ':
                    t1.setItem(number_1,11, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time19+' ':
                    t1.setItem(number_1,12, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time20+' ':
                    t1.setItem(number_1,13, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time21+' ':
                    t1.setItem(number_1,14, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time22+' ':
                    t1.setItem(number_1,15, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time23+' ':
                    t1.setItem(number_1,16, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time24+' ':
                    t1.setItem(number_1,17, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time25+' ':
                    t1.setItem(number_1,18, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time26+' ':
                    t1.setItem(number_1,19, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time27+' ':
                    t1.setItem(number_1,20, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time28+' ':
                    t1.setItem(number_1,21, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time29+' ':
                    t1.setItem(number_1,22, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time30+' ':
                    t1.setItem(number_1,23, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time31+' ':
                    t1.setItem(number_1,24, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time32+' ':
                    t1.setItem(number_1,25, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time33+' ':
                    t1.setItem(number_1,26, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time34+' ':
                    t1.setItem(number_1,27, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time35+' ':
                    t1.setItem(number_1,28, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time36+' ':
                    t1.setItem(number_1,29, QTableWidgetItem('غائب'))
                elif time_5==users0000+' '+time37+' ':
                    t1.setItem(number_1,30, QTableWidgetItem('غائب'))
            t1.setItem(number_1,0, QTableWidgetItem(users0000))
            number_1+=1
        number_1=1
        time_4=datetime.now()
        t1.setItem(0,0, QTableWidgetItem("اسم الموظف"))
        t1.setItem(0,1, QTableWidgetItem("%s\%s"%(time_4.month,1)))
        t1.setItem(0,2, QTableWidgetItem("%s\%s"%(time_4.month,2)))
        t1.setItem(0,3, QTableWidgetItem("%s\%s"%(time_4.month,3)))
        t1.setItem(0,4, QTableWidgetItem("%s\%s"%(time_4.month,4)))
        t1.setItem(0,5, QTableWidgetItem("%s\%s"%(time_4.month,5)))
        t1.setItem(0,6, QTableWidgetItem("%s\%s"%(time_4.month,6)))
        t1.setItem(0,7, QTableWidgetItem("%s\%s"%(time_4.month,7)))
        t1.setItem(0,8, QTableWidgetItem("%s\%s"%(time_4.month,8)))
        t1.setItem(0,9, QTableWidgetItem("%s\%s"%(time_4.month,9)))
        t1.setItem(0,10, QTableWidgetItem("%s\%s"%(time_4.month,10)))
        t1.setItem(0,11, QTableWidgetItem("%s\%s"%(time_4.month,11)))
        t1.setItem(0,12, QTableWidgetItem("%s\%s"%(time_4.month,12)))
        t1.setItem(0,13, QTableWidgetItem("%s\%s"%(time_4.month,13)))
        t1.setItem(0,14, QTableWidgetItem("%s\%s"%(time_4.month,14)))
        t1.setItem(0,15, QTableWidgetItem("%s\%s"%(time_4.month,15)))
        t1.setItem(0,16, QTableWidgetItem("%s\%s"%(time_4.month,16)))
        t1.setItem(0,17, QTableWidgetItem("%s\%s"%(time_4.month,17)))
        t1.setItem(0,18, QTableWidgetItem("%s\%s"%(time_4.month,18)))
        t1.setItem(0,19, QTableWidgetItem("%s\%s"%(time_4.month,19)))
        t1.setItem(0,20, QTableWidgetItem("%s\%s"%(time_4.month,20)))
        t1.setItem(0,21, QTableWidgetItem("%s\%s"%(time_4.month,21)))
        t1.setItem(0,22, QTableWidgetItem("%s\%s"%(time_4.month,22)))
        t1.setItem(0,23, QTableWidgetItem("%s\%s"%(time_4.month,23)))
        t1.setItem(0,24, QTableWidgetItem("%s\%s"%(time_4.month,24)))
        t1.setItem(0,25, QTableWidgetItem("%s\%s"%(time_4.month,25)))
        t1.setItem(0,26, QTableWidgetItem("%s\%s"%(time_4.month,26)))
        t1.setItem(0,27, QTableWidgetItem("%s\%s"%(time_4.month,27)))
        t1.setItem(0,28, QTableWidgetItem("%s\%s"%(time_4.month,28)))
        t1.setItem(0,29, QTableWidgetItem("%s\%s"%(time_4.month,29)))
        t1.setItem(0,30, QTableWidgetItem("%s\%s"%(time_4.month,30)))
        b000=QtWidgets.QPushButton('رجوع',program)
        b000.setStyleSheet(hr_design.buttons2)
        b000.move(50,650)
        b000.resize(150,40)
        b000.setIconSize(QtCore.QSize(50,50))
        b000.clicked.connect(screen)
        b000.show()
        if c1.currentText()=="English":
            b000.setText("back")
        else:
            pass
    with open('username','r') as f6:
        list2=f6.read().rstrip('\n').split('\n')
    if name==list2[0] and password==list2[1]:
        l1.hide()
        e1.hide()
        e2.hide()
        b1.hide()
        l2.hide()
        program.setStyleSheet(hr_design.window2)
        l3=QtWidgets.QLabel(program)
        l3.move(1,1)
        l3.resize(1399,100)
        l3.setStyleSheet(hr_design.ll)
        l3.show()
        global l4
        l4=QtWidgets.QLabel('الصفحة الرئيسية',program)
        l4.move(550,1)
        l4.resize(250,100)
        l4.setStyleSheet(hr_design.lll)
        l4.show()
        list3=[]
        with open('username','r') as f7:
            list3=f7.read().rstrip('\n').split('\n')
        global l5
        l5=QtWidgets.QLabel('اسم المستخدم :'+list3[0],program)
        l5.move(670,150)
        l5.resize(500,100)
        l5.setStyleSheet(hr_design.lll)
        l5.show()
        global b3
        b3=QtWidgets.QPushButton('موظف جديد',program)
        b3.setStyleSheet(hr_design.buttons2)
        b3.move(100,350)
        b3.resize(200,50)
        b3.setIcon(QIcon('icons\\user3.png'))
        b3.setIconSize(QtCore.QSize(50,50))
        b3.clicked.connect(save)
        b3.show()
        global b4
        b4=QtWidgets.QPushButton('تسجيل غياب',program)
        b4.setStyleSheet(hr_design.buttons2)
        b4.move(100,450)
        b4.resize(200,50)
        b4.setIcon(QIcon('icons\\user2.png'))
        b4.setIconSize(QtCore.QSize(50,50))
        b4.clicked.connect(users11)
        b4.show()
        global b5
        b5=QtWidgets.QPushButton('تسجيل حضور',program)
        b5.setStyleSheet(hr_design.buttons2)
        b5.move(600,450)
        b5.resize(200,50)
        b5.setIcon(QIcon('icons\\true.png'))
        b5.setIconSize(QtCore.QSize(40,40))
        b5.clicked.connect(users1)
        b5.show()
        global b6
        b6=QtWidgets.QPushButton('قائمه الموظفين',program)
        b6.setStyleSheet(hr_design.buttons2)
        b6.move(350,350)
        b6.resize(200,50)
        b6.setIcon(QIcon('icons\\list.png'))
        b6.setIconSize(QtCore.QSize(40,40))
        b6.clicked.connect(s1)
        b6.show()
        global b7
        b7=QtWidgets.QPushButton('المرتبات',program)
        b7.setStyleSheet(hr_design.buttons2)
        b7.move(350,450)
        b7.resize(200,50)
        b7.setIcon(QIcon('icons\\money.png'))
        b7.setIconSize(QtCore.QSize(50,50))
        b7.clicked.connect(Money)
        b7.show()
        global b8
        b8=QtWidgets.QPushButton('مساعده',program)
        b8.setStyleSheet(hr_design.buttons2)
        b8.move(600,350)
        b8.clicked.connect(web)
        b8.resize(200,50)
        b8.setIcon(QIcon('icons\\help.png'))
        b8.setIconSize(QtCore.QSize(40,40))
        b8.show()
        global b9
        b9=QtWidgets.QPushButton('تغيير الاسم',program)
        b9.setStyleSheet(hr_design.buttons2)
        b9.move(850,350)
        b9.clicked.connect(username)
        b9.resize(200,50)
        b9.setIcon(QIcon('icons\\name.png'))
        b9.setIconSize(QtCore.QSize(40,40))
        b9.show()
        global b10
        b10=QtWidgets.QPushButton('تغيير كلمه المرور',program)
        b10.setStyleSheet(hr_design.buttons2)
        b10.move(850,450)
        b10.clicked.connect(password0)
        b10.setIcon(QIcon('icons\\password.png'))
        b10.setIconSize(QtCore.QSize(40,40))
        b10.resize(200,50)
        b10.show()
        global b20
        b20=QtWidgets.QPushButton('التقارير',program)
        b20.setStyleSheet(hr_design.buttons2)
        b20.move(1100,450)
        b20.clicked.connect(reports)
        b20.setIcon(QIcon('icons\\report.png'))
        b20.setIconSize(QtCore.QSize(40,40))
        b20.resize(200,50)
        b20.show()
        global timer
        timer=QTimer()
        timer.timeout.connect(t20)
        timer.start(1000)
        global l20
        l20=QtWidgets.QLabel(program)
        l20.move(900,610)
        l20.resize(270,100)
        l20.setStyleSheet(hr_design.lll)
        l20.show()
        global c1
        c1=QtWidgets.QComboBox(program)
        c1.move(600,190)
        c1.addItem('العربية')
        c1.addItem('English')
        c1.setItemIcon(0,QIcon("icons\\egypt.png"))
        c1.setItemIcon(1,QIcon("icons\\usa.png"))
        c1.setStyleSheet(hr_design.c)
        c1.resize(200,50)
        c1.setIconSize(QtCore.QSize(50,50))
        c1.show()
    else:
        l2.setText('حاول مره اخري')
app=QtWidgets.QApplication(sys.argv)
program=QtWidgets.QMainWindow()
program.setWindowTitle('Hr app')
program.setStyleSheet(hr_design.window)
program.resize(800,600)
program.setWindowIcon(QIcon("icons\\settings.ico"))
l1=QtWidgets.QLabel(program)
i1=QPixmap('icons\\user1.png').scaled(150,150)
l1.setPixmap(i1)
l1.setStyleSheet(hr_design.i)
l1.resize(200,200)
l1.move(610,1)
l2=QtWidgets.QLabel(program)
l2.resize(200,70)
l2.move(600,380)
l2.setStyleSheet(hr_design.l)
l2.show()
e1=QtWidgets.QLineEdit(program)
e1.move(600,300)
e1.resize(200,40)
e1.setStyleSheet(hr_design.e)
e1.setToolTip('الاسم')
e1.setPlaceholderText('اسم المستخدم')
e2=QtWidgets.QLineEdit(program)
e2.move(600,350)
e2.resize(200,40)
e2.setEchoMode(QtWidgets.QLineEdit.Password)
e2.setStyleSheet(hr_design.e)
e2.setPlaceholderText('كلمه المرور')
e2.setToolTip('كلمة المرور')
b1=QtWidgets.QPushButton('تسجيل دخول',program)
b1.resize(200,40)
b1.move(600,450)
b1.clicked.connect(program2)
b1.setStyleSheet(hr_design.buttons)
b1.setToolTip('تسجيل دخول')
b2=QtWidgets.QPushButton('خروج',program)
b2.resize(100,40)
b2.move(1260,650)
b2.setStyleSheet(hr_design.buttons1)
b2.setToolTip('الخروج من البرنامج')
b2.clicked.connect(x)
web2()
program.showMaximized()
app.exec_()