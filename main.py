#%%
import os
# import re
import sys

# import pandas as pd
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtWebKit import *
# from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QAction, QMainWindow
from qgis.core import *
from qgis.gui import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtGui import QColor


# from ui_echarts import Ui_Form
#%%
class MyWnd(QWidget):
    def __init__(self):
        # QMainWindow.__init__(self)
        # 图层及图布的初始化
        # os.chdir(r"C:\Users\zhangyz\OneDrive\2.科研工作\2021-12_Qt_Project\PyQt_Pyecharts_Test")
        os.chdir(r"D:/Onedrive/2.科研工作/2021-12_Qt_Project/PyQt_Pyecharts_Test")
        super(MyWnd, self).__init__()
        # self.resize(1200,1000)
        # self.maximumWidth()
        # self.maximumHeight()
        # self.showMaximized()
        self.setupUi()

    def setupUi(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")


        self.spilter_1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.project = QgsProject.instance()
        self.canvas = QgsMapCanvas() #QWebEngineView()
        self.canvas.setCanvasColor(QtCore.Qt.white)

        self.crs = QgsCoordinateReferenceSystem("EPSG:3857")
        self.canvas.setDestinationCrs(self.crs)
        self.bridge = QgsLayerTreeMapCanvasBridge(self.project.layerTreeRoot(), self.canvas)
        
        self.urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
        self.osm_lyr = QgsRasterLayer("type=xyz&url=" + self.urlWithParams, 'OSM', "wms")
        self.bing_virtual_earth = "http://ecn.t3.tiles.virtualearth.net/tiles/a%7Bq%7D.jpeg?g%3D1&zmax=19&zmin=1"
        self.bingLyr = QgsRasterLayer("type=xyz&url=" + self.bing_virtual_earth, 'BING', "wms")
        
        self.rlayer = QgsRasterLayer(r"D:\OneDrive\2.科研工作\2021-08_广西地质灾害\公路滑坡风险监测预警系统示范平台\After-Preprocessed\Antecedent_Rainfall_20220328_30arcsec.cut.tif")
        self.project.addMapLayer(self.osm_lyr, True)

        self.canvas.refresh()
        self.canvas.show()
        self.spilter_1.addWidget(self.canvas)

        # self.map = QWebEngineView()
        # self.map.load(QtCore.QUrl("https://map.baidu.com"))
        # self.spilter_1.addWidget(self.map)
        self.verticalLayout.addWidget(self.canvas)

        self.spilter_h = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.echart_2 = QWebEngineView()

        # df = pd.read_csv(r"C:\Users\zhangyz\OneDrive\2.科研工作\2021-08_广西地质灾害\Data\Guangxi\arf_stats_city.csv")
        # df_day = df[df.datetime == df.datetime[0]]
        #
        # bar = Bar()
        # bar.add_xaxis(df_day.city.to_list())
        # bar.add_yaxis("Cell Counts", df_day.average.to_list())
        # # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
        # # 也可以传入路径参数，如 bar.render("mycharts.html")
        # bar.render(r'RR_bar.html')
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
                .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
                .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
                .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
            # 或者直接使用字典参数
            # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
        )
        bar.render(r'RR_bar.html')
        # self.resize_html(r'RR_bar.html')
        self.echart_2.load(QtCore.QUrl("file:///RR_bar.html"))

        self.echart_3 = QWebEngineView()
        self.echart_3.load(QtCore.QUrl("file:///RR_bar.html"))

        self.spilter_h.addWidget(self.echart_3)
        self.spilter_h.addWidget(self.echart_2)
        self.verticalLayout.addWidget(self.spilter_h)

        self.echart_1 = QWebEngineView()
        self.echart_1.load(QtCore.QUrl("file:///RR_bar.html"))
        self.spilter_1.addWidget(self.echart_1)
    def resize_html(self,html0):
        with open(html0, "r+", encoding='utf-8') as html:
            html_bf = BeautifulSoup(html, 'html.parser')
            meta = html_bf.find('meta')
            meta['name'] = "viewport"
            meta['content'] = "width=device-width, initial-scale=1"
            divs = html_bf.select('.chart-container')
            divs[0]["style"] = "width:100%;height:100%;position:absolute;top:0%;left:0%;border-style:solid;border-color:#444444;border-width:1%;"
            # divs[1]['style'] = "width:30%;height:80%;position:absolute;top:5%;left:65%;border-style:solid;border-color:#444444;border-width:1%;"
            body = html_bf.find("body")
            body["style"] = "background-color:#333333;"
            div_title = "<div align=\"center\" style=\"width:100%;\">\n<span style=\"font-size:150%;font face=\'黑体\';color:#FFFFFF\"><b>测试0129</b></div>"
            # 修改页面背景色、追加标题
            body.insert(0, BeautifulSoup(div_title, "html.parser").div)
            html_new = str(html_bf)
            html.seek(0, 0)
            html.truncate()
            html.write(html_new)
            html.close()
#%%
if __name__ == '__main__':
    # qgs = QgsApplication([], True)
    # qgs.setPrefixPath('qgis', True)
    # qgs.initQgis()
    app = QApplication(sys.argv)
    window = MyWnd()
    # window.resize(1500, 800)
    window.show()
    sys.exit(app.exec_())
    #
    # exit_code = qgs.exec_()
    # qgs.exitQgis()
    # sys.exit(exit_code)

# %%
