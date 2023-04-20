import sys,os,cv2
# 导入图形组件库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image
import numpy as np
from model import FillHole, delete
#导入做好的界面库
from gui import Ui_MainWindow

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.patches import PathPatch

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MainWindow,self).__init__()
        #初始化界面组件
        self.setupUi(self)
        self.pushButton.setIcon(QApplication.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.pushButton.clicked.connect(self.load)
        self.pushButton_1.clicked.connect(self.lasso)
        self.pushButton_2.clicked.connect(self.test)
        # Render the SVG image to a QPixmap
        pixmap = QPixmap("C:\\WorkSpace_M-Dell\\roughness_calculator\\icon.png")

        # Set the window icon to the logo
        self.setWindowIcon(QIcon(pixmap))
        self.changed = False

    def load(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "SELECT FILE",
                                                                "./",  # 起始路径
                                                                "All Files (*)")  # 设置文件扩展名过滤,用双分号间隔
        
        if fileName_choose != "":
            self.pic = fileName_choose
            pixmap = QPixmap(fileName_choose)

            self.label.setPixmap(pixmap.scaled(491,341))
            QMessageBox.warning(self,"Prompt","Successfully selected！",QMessageBox.Yes,QMessageBox.Yes)

            print(fileName_choose)

            # setup xy grid and read in img
            
            # self.img = mpimg.imread(self.pic) 

            self.origin = np.array(Image.open(self.pic))
            self.img = np.array(Image.open(self.pic))# rows of cols of [R, G, B]
            
            height, width, channels = self.img.shape
            self.frame_pxs = []
            for i in np.arange(width):
                for j in np.arange(height):
                    self.frame_pxs.append([i,j])

    def lasso(self):
        fig, ax = plt.subplots()
        self.showing = plt.imshow(self.img)

        # show canny at the begging
        self.disp_path(self.canny1,'r',"Line1")
        self.disp_path(self.canny2,'b',"Line2")
        # print(c1_path)
        # print("count: ", len(c1_path))
        plt.legend()
        plt.show() 

        self.lasso = LassoSelector(ax, onselect=self.onselect)        

    def disp_path(self, canny, c,label):
        path = []
        row_c = 0
        for row in canny:
            col_c = 0
            for cell in row:
                if cell != 0:
                    path.append([row_c,col_c])    
                col_c += 1
            row_c += 1
        path = np.asarray(path)
        plt.scatter(path[:,1],path[:,0], c=c, s = 0.1,label = label)

    def to_gray(self, rgb) :
        R, G, B = rgb[0], rgb[1], rgb[2]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        return Y

    def deselect_canny(self, canny, out_pxs):
        for px in out_pxs:
            canny[px[1], px[0]] = 0
        return canny

    # lasso mathod
    def onselect(self, verts):
        



        path = Path(verts)

        bools = path.contains_points(self.frame_pxs)

        # creating empty arrays for pxs in selection area and out
        in_pxs, out_pxs = [],[]

        for i in range(len(self.frame_pxs)):
            if bools[i]:
                in_pxs.append(self.frame_pxs[i])
            else:
                out_pxs.append(self.frame_pxs[i])

        print("\n---- Stats: ----")
        print("all pxs len: ", len(self.frame_pxs))
        print(" in pxs len: ", len(in_pxs))
        print("out pxs len: ", len(out_pxs))
        

        # change local canny 1 and 2
        canny1 = self.canny1.copy()
        canny2 = self.canny2.copy()

        canny1 = self.deselect_canny(canny1, out_pxs)
        canny2 = self.deselect_canny(canny2, out_pxs)
        
        # self.view_canny(canny1)

        self.lineEdit_3.setText(str(len(canny1[canny1 == 255])))
        self.lineEdit_4.setText(str(len(canny2[canny2 == 255])))
        self.lineEdit_5.setText('%4f' % (len(canny1[canny1 == 255]) / len(canny2[canny2 == 255])))

        

        # self.fc[:, -1] = self.alpha_other
        # self.fc[self.ind, -1] = 1
        # self.collection.set_facecolors(self.fc)
        # self.canvas.draw_idle()


    # debug view_canny
    def view_canny(self, canny):
        print(canny.shape)
        # line = []
        # for i in range(canny.shape[0]):
        #     for j in range(canny.shape[1]):
        #         line.append([i,j])
        # plt.plot(*zip(*line),  marker='o', color='r', ls='')
        
        self.showing.set_data(canny)
        plt.draw()

    # lasso mathod
    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()


    def test(self):
        img = cv2.imread(self.pic)
        GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(GrayImage, 180, 255, cv2.THRESH_BINARY)
        thresh1 = delete(255 - thresh1)  # 0
        thresh1 = FillHole(thresh1)
        thresh1 = delete(thresh1)
        thresh1 = 255 - thresh1
        A = thresh1
        B = thresh1
        kernel = np.ones((20, 20))
        erodeImg = cv2.erode(B, kernel)
        img1 = cv2.GaussianBlur(erodeImg, (3, 3), 0)
        ret, thresh1 = cv2.threshold(img1, 0, 255, cv2.THRESH_OTSU)
        ret, thresh2 = cv2.threshold(A, 0, 255, cv2.THRESH_OTSU)
        self.lineEdit.setText(str(len(thresh2[thresh2 == 0])))
        self.lineEdit_2.setText(str(len(thresh1[thresh1 == 0])))
        
        # Canny algo then apply selected Path as filter
        canny1 = cv2.Canny(thresh1, 50, 150)
        canny2 = cv2.Canny(thresh2, 50, 150)
        
        self.canny1 = canny1
        self.canny2 = canny2

        np.set_printoptions(threshold=sys.maxsize)
        
        self.lineEdit_3.setText(str(len(canny1[canny1 == 255])))
        self.lineEdit_4.setText(str(len(canny2[canny2 == 255])))
        self.lineEdit_5.setText('%4f' % (len(canny1[canny1 == 255]) / len(canny2[canny2 == 255])))


if __name__ == "__main__":
    #创建QApplication 固定写法
    app = QApplication(sys.argv)
    # 实例化界面
    window = MainWindow()
    #显示界面
    window.show()
    #阻塞，固定写法
    
    sys.exit(app.exec_())