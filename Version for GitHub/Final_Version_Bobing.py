import sys
import copy
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication # 导入Qt模块
from random import randint

# 导入随机数函数
import picture
import picture_gif
from page1 import Ui_Form_1
from page2 import Ui_Form_2
from page3 import Ui_Form_3
from page4 import Ui_Form_4
from page4_1 import Ui_Form_4_1
from page5 import Ui_Form_5
from page6 import Ui_Form_6
from page_r1 import Ui_Form_r1
from page_r2 import Ui_Form_r2

id_lst=[]
res=[]
res_1=[]
res_2=[]
res_3=[]
res_4=[]
res_5=[]
res_6=[]
res_7=[]
str1=""
str2=""
str3=""
str4=""
str5 = ""

class page1(QWidget, Ui_Form_1):
    # 初始化
    def __init__(self):
        super(page1, self).__init__()
        self.setupUi(self)

    def page1_2(self):
        global ui2
        """我超 在外面并列把几个类都定义完 直接在自己的函数里面互相调用就可以了！！！
        """
        ui2=page2()
        ui2.show()
        ui.close()

    def page1_3(self):
        global ui3
        ui3=page3()
        ui3.show()
        ui.close()

class page2(QWidget, Ui_Form_2):
    # 初始化
    def __init__(self):
        super(page2, self).__init__()
        self.setupUi(self)

    def page2_3(self):
        global ui3
        ui3=page3()
        ui3.show()
        ui2.close()

class page3(QWidget, Ui_Form_3):
    # 初始化
    def __init__(self):
        super(page3, self).__init__()
        self.setupUi(self)

    def page3_4(self):
        global ui4
        ui4=page4()
        ui4.show()
        ui3.close()

    def page3_4_1(self):
        global ui4_1
        ui4_1=page4_1()
        ui4_1.show()
        ui3.close()

class page4(QWidget, Ui_Form_4):
    # 初始化
    def __init__(self):
        super(page4, self).__init__()
        self.setupUi(self)
        # nmd GIF 终于被我搞定啦！！！！！！！！！！
        self.gif_1=QMovie(":image_gif/6.gif")
        self.label_2.setMovie(self.gif_1)
        self.gif_1.start()

    def rand(self):
        global result
        results = []
        for roll_num in range(6):
            result = randint(1, 6)
            results.append(result)  # 将随机数存于列表
        return results

    def page4_r1(self):
        global ui_r1
        ui_r1=page_r1()
        ui_r1.show()
        ui4.close()

class page4_1(QWidget, Ui_Form_4_1):
    # 初始化
    def __init__(self):
        super(page4_1, self).__init__()
        self.setupUi(self)

    def page4_1_5(self):
        global ui5
        global num
        ui5=page5()

        num=int(ui4_1.lineEdit.text()) # 这里 输入的是str类型 需要我们转换成int类型



        ui5.show()
        ui4_1.close()


class page5(QWidget, Ui_Form_5):
    # 初始化
    def __init__(self):
        super(page5, self).__init__()
        self.setupUi(self)

    def page5_6(self):
        global ui6
        global info
        global parts
        global id_lst
        global str5
        str5=""
        info=ui5.lineEdit.text()


        # 这边将输入的数据一组一组的放入一个大列表里面

        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            id_lst = [p for p in parts if p]

        ui6=page6()
        ui6.show()
        ui5.close()

class page6(QWidget, Ui_Form_6):
    # 初始化
    def __init__(self):
        super(page6, self).__init__()
        self.setupUi(self)

        self.gif_2=QMovie(":image_gif/6.gif")
        self.label_2.setMovie(self.gif_2)
        self.gif_2.start()


    def page6_r2(self):
        global ui_r2

        #这里放出结果的程序
        ui_r2=page_r2()
        ui_r2.show()

        for i in range(num):
            global str5
            global a
            global res
            a = handle_message()

            str1 = str(i + 1)
            str2 = " ".join('%s' % a for a in id_lst[i])
            str3 = " ".join('%s' % a for a in res[i])
            str4 = "第" + str1 + "位选手： id 为 " + str2 + " " + str3
            str1 = " "
            str2 = " "
            str3 = " "
            str5=str5+"\n"+str4
            str4 =" "

        res=[]

        ui6.close()


class page_r2(QWidget, Ui_Form_r2):
    # 初始化
    def __init__(self):
        super(page_r2, self).__init__()
        self.setupUi(self)

    def return_to_1(self):
        ui.show()
        ui_r2.close()

    def show_message_2(self):
        global str5
        QMessageBox.about(self,'结果', str5)

class page_r1(QWidget, Ui_Form_r1):

    # 初始化
    def __init__(self):
        super(page_r1, self).__init__()
        self.setupUi(self)

        #这里把每个图片都display一下，离谱，不同函数之间不好传参，所以最好把需要的操作写在同一个函数里面！！！
        """
        2 8
        3 5
        6 7     
        这里写图片的判断！！！
        """
    def show_message_1(self):

        result_d=ui4.rand()
# 深拷贝这一步非常关键
        results=copy.deepcopy(result_d)


        for i in range(6):
            if result_d[i]==1:
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/11.png);")
                break
            elif result_d[i]==2:
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/22.png);")
                break
            elif result_d[i]==3 :
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/33.png);")
                break
            elif result_d[i]==4:
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/44.png);")
                break
            elif result_d[i]==5:
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/55.png);")
                break
            elif result_d[i]==6:
                result_d.pop(i)
                self.listView_2.setStyleSheet("border-image: url(:/image/66.png);")
                break

        for i in range(5):
                if result_d[i]==1:
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/11.png);")
                    break
                elif result_d[i]==2:
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/22.png);")
                    break
                elif result_d[i]==3:
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/33.png);")
                    break
                elif result_d[i]==4:
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/44.png);")
                    break
                elif result_d[i]==5:
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/55.png);")
                    break
                elif result_d[i]==6 :
                    result_d.pop(i)
                    self.listView_8.setStyleSheet("border-image: url(:/image/66.png);")
                    break

        for i in range(4):
            if result_d[i]==1:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/11.png);")
                break
            elif result_d[i]==2:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/22.png);")
                break
            elif result_d[i]==3:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/33.png);")
                break
            elif result_d[i]==4:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/44.png);")
                break
            elif result_d[i]==5:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/55.png);")
                break
            elif result_d[i]==6:
                result_d.pop(i)
                self.listView_3.setStyleSheet("border-image: url(:/image/66.png);")
                break

        for i in range(3):
            if result_d[i]==1:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/11.png);")
                break
            elif result_d[i]==2:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/22.png);")
                break
            elif result_d[i]==3:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/33.png);")
                break
            elif result_d[i]==4:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/44.png);")
                break
            elif result_d[i]==5:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/55.png);")
                break
            elif result_d[i]==6:
                result_d.pop(i)
                self.listView_5.setStyleSheet("border-image: url(:/image/66.png);")
                break

        for i in range(2):
            if result_d[i]==1:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/11.png);")
                break
            elif result_d[i]==2:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/22.png);")
                break
            elif result_d[i]==3:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/33.png);")
                break
            elif result_d[i]==4:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/44.png);")
                break
            elif result_d[i]==5:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/55.png);")
                break
            elif result_d[i]==6:
                result_d.pop(i)
                self.listView_6.setStyleSheet("border-image: url(:/image/66.png);")
                break

        for i in range(1):
            if result_d[i]==1:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/11.png);")
                break
            elif result_d[i]==2:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/22.png);")
                break
            elif result_d[i]==3:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/33.png);")
                break
            elif result_d[i]==4:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/44.png);")
                break
            elif result_d[i]==5:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/55.png);")
                break
            elif result_d[i]==6:
                result_d.pop(i)
                self.listView_7.setStyleSheet("border-image: url(:/image/66.png);")
                break

        sides = [1, 2, 3, 4, 5, 6]
        countDict = {}  # 该字典用于统计和存储每个点数出现次数
        for i in results:
            if i in countDict:
                countDict[i] += 1  # 对于重复出现的，每出现一次，次数增加1
            else:
                countDict[i] = 1
        for j in sides:  # 对于未出现的点数，记为0次
            if j not in results:
                countDict[j] = 0

        # 函数判断结果
        def sixred_or_black():
            for i in range(1, 7):
                if countDict[i] == 6:
                    if i == 4:
                        return '六博红'
                    else:
                        return '六博黑'

        def chajinhua():
            if countDict[4] == 4 and countDict[1] == 2:
                return '状元插金花'

        def duitang():
            if len(set(list(countDict.values()))) == 1:
                return '对堂'

        def wuzidengke():
            if 5 in list(countDict.values()):
                return '五子登科'

        def zhuangyuan():
            if countDict[4] == 4:
                return '状元'

        def sijin():
            for i in range(1, 7):
                if countDict[i] == 4:
                    return '四进'

        def sanhong_erju_yixiu():
            if countDict[4] == 3:
                return '三红'
            elif countDict[4] == 2:
                return '二举'
            elif countDict[4] == 1:
                return '一秀'
            else:
                return '抱歉无奖励'

        count = 7
        while count:
            if sixred_or_black() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{sixred_or_black()}')
                break

            if chajinhua() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{chajinhua()}')
                break

            if duitang() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{duitang()}')
                break

            if wuzidengke() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{wuzidengke()}')
                break

            if zhuangyuan() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{zhuangyuan()}')
                break

            if sijin() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{sijin()}')
                break

            if sanhong_erju_yixiu() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果', f'点数分别为：{results[0]} '
                                                f'{results[1]} '
                                                f'{results[2]} '
                                                f'{results[3]} '
                                                f'{results[4]} '
                                                f'{results[5]}\n'
                                                f'你获得了：{sanhong_erju_yixiu()}')
                break


    def return_to_2(self):
        ui.show()
        ui_r1.close()


#    这边的result_m专门记录多人模式的结果
def handle_message():
    results_m = []
    for roll_num in range(6):
        result = randint(1, 6)
        results_m.append(result)  # 将随机数存于列表

    sides = [1, 2, 3, 4, 5, 6]
    countDict = {}  # 该字典用于统计和存储每个点数出现次数
    for i in results_m:
        if i in countDict:
            countDict[i] += 1  # 对于重复出现的，每出现一次，次数增加1
        else:
            countDict[i] = 1
    for j in sides:  # 对于未出现的点数，记为0次
        if j not in results_m:
            countDict[j] = 0

    # 函数判断结果
    def sixred_or_black():
        for i in range(1, 7):
            if countDict[i] == 6:
                if i == 4:
                    return '六博红'
                else:
                    return '六博黑'

    def chajinhua():
        if countDict[4] == 4 and countDict[1] == 2:
            return '状元插金花'

    def duitang():
        if len(set(list(countDict.values()))) == 1:
            return '对堂'

    def wuzidengke():
        if 5 in list(countDict.values()):
            return '五子登科'

    def zhuangyuan():
        if countDict[4] == 4:
            return '状元'

    def sijin():
        for i in range(1, 7):
            if countDict[i] == 4:
                return '四进'

    def sanhong_erju_yixiu():
        if countDict[4] == 3:
            return '三红'
        elif countDict[4] == 2:
            return '二举'
        elif countDict[4] == 1:
            return '一秀'
        else:
            return '抱歉无奖励'

    count = 7
    while count:   #  用来判断其中情况
        if sixred_or_black() == None:
            count -= 1
        else:
            res_1=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",sixred_or_black()]
            res.append(res_1)
            res_1=[]


            break

        if chajinhua() == None:
            count -= 1
        else:
            res_2=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",chajinhua()]
            res.append(res_2)
            res_2=[]


            break

        if duitang() == None:
            count -= 1
        else:
            res_3=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",duitang()]
            res.append(res_3)
            res_3=[]


            break

        if wuzidengke() == None:
            count -= 1
        else:
            res_4=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",wuzidengke()]
            res.append(res_4)
            res_4=[]


            break

        if zhuangyuan() == None:
            count -= 1
        else:
            res_5=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",zhuangyuan()]
            res.append(res_5)
            res_5=[]


            break

        if sijin() == None:
            count -= 1
        else:
            res_6=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",sijin()]
            res.append(res_6)
            res_6=[]


            break

        if sanhong_erju_yixiu() == None:
            count -= 1
        else:
            res_7=["点数分别为:",results_m[0],results_m[1],results_m[2],results_m[3],
                   results_m[4],results_m[5],"你获得了：",sanhong_erju_yixiu()]
            res.append(res_7)
            res_7=[]


            break
    return  res


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = page1()
    ui.show()
    sys.exit(app.exec_())

