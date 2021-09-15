#导入库+包
import re
import os
import fitz
import xlwings as xw
# from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class file_conducter:
    def __init__(self,filename):
        self.path=filename
        # print(self.path)
        self.num=0
        self.xlwbook=xw.Book()
        self.sheet=self.xlwbook.sheets['Sheet1']
        self.pic_path = r"E:\study\Experiments\python_calu\indvl_ex\images" #导出图片
        if not os.path.exists(self.pic_path):
            os.mkdir(self.pic_path)
        # else:
        #     print("文件夹已存在，不必重建！")
        self.doc = fitz.open(self.path) #打开pdf文件
        self.lenXREF = self.doc.xrefLength()-1 #获取对象数量长度
        print(f"文件名:{self.path}, 页数: {self.doc.pageCount}, 对象: {self.lenXREF}") # 打印PDF的信息
    
    def doisearch(self):
        text=self.doc[0].getText()
        doimbr=re.search('10[.][0-9]{4,}/[A-Z,a-z,.,0-9,-,|, ]{,}',text)
        self.sheet.range('A1').value="DOI"
        self.sheet.range('B1').value=doimbr.group()

    def extractimages(self):
        checkIM = r"/Subtype(?= */Image)" # 使用正则表达式来查找图片
        for i in range(1,self.lenXREF):
            text = self.doc.xrefObject(i) # 定义对象字符串       
            is   = re.search(checkIM, text) # 查看是否是image
            if not isImage: # 如果不是图片，则进行下一个判断
                continue 
            pix = fitz.Pixmap(self.doc, i) # 生成图像对象    
            print(pix)
            if min(pix.width, pix.height) <= 600:  # 获取图片像素过小
                continue
            try:
                if pix.n<5:
                    self.num += 1 #图片计数
                    new_name = f"图片{self.num}.png" # 生成图片的名称
                    pix.writePNG(os.path.join(self.pic_path, new_name))
                    print(new_name)
                    pix = None
                else:
                    self.num += 1 #图片计数
                    pixno = fitz.Pixmap(fitz.csRGB, pix) 
                    new_name = f"图片{self.num }.png" # 生成图片的名称
                    pixno.writePNG(os.path.join(self.pic_path, new_name))
                    print(new_name)
                    pixno = None
            except RuntimeError:
                #异常处理，跳过错误段继续提取之后的图片
                print("Error:extract image fail")
                os.remove(os.path.join(self.pic_path, new_name))
                self.num -=1
                continue
    
    def xlssetting(self):
        self.sheet.range('A2').value="图号"
        self.sheet.range('B2').value="图片"
        self.sheet.range('C2').value="描述"
        self.sheet.range('D2').value="正文相关"

    #将图片放入到sheet中
    def add_center(self, target, match=False, width=None, height=None, column_width=None, row_height=None):
        unit_width = 6.107  # Excel默认列宽与像素的比
        rng = self.sheet.range(target)  # 目标单元格
        name = os.path.basename(self.filePath)  # 文件名
        _width, _height = Image.open(self.filePath).size  # 原图片宽高
        NOT_SET = True  # 未设置单元格宽高
        # match
        if match:  # 绝对匹配图像
            width, height = _width, _height
        else:  # 不绝对匹配图像
            # width & height
            if width or height:
                if not height:  # 指定了宽，等比计算高
                    height = width / _width * _height
                if not width:  # 指定了高，等比计算宽
                    width = height / _height * _width
            else:
                # column_width & row_height
                if column_width and row_height:  # 同时指定单元格最大宽高
                    width = row_height / _height * _width  # 根据单元格最大高度假设宽
                    height = column_width / _width * _height  # 根据单元格最大宽度假设高
                    area_width = column_width * height  # 假设宽优先的面积
                    area_height = row_height * width  # 假设高优先的面积
                    if area_width > area_height:
                        width = column_width
                    else:
                        height = row_height
                elif not column_width and not row_height:  # 均无指定单元格最大宽高
                    column_width = 100
                    row_height = 75
                    rng.column_width = column_width / unit_width  # 更新当前宽度
                    rng.row_height = row_height  # 更新当前高度
                    NOT_SET = False
                    width = row_height / _height * _width  # 根据单元格最大高度假设宽
                    height = column_width / _width * _height  # 根据单元格最大宽度假设高
                    area_width = column_width * height  # 假设宽优先的面积
                    area_height = row_height * width  # 假设高优先的面积
                    if area_width > area_height:
                        height = row_height
                    else:
                        width = column_width
                else:
                    width = row_height / _height * _width if row_height else column_width  # 仅设了单元格最大宽度
                    height = column_width / _width * _height if column_width else row_height  # 仅设了单元格最大高度
        assert 0 <= width / unit_width <= 255
        assert 0 <= height <= 409.5
        if NOT_SET:
            rng.column_width = width / unit_width  # 更新当前宽度
            rng.row_height = height  # 更新当前高度
        left = rng.left + (rng.width - width) / 2  # 居中
        top = rng.top + (rng.height - height) / 2
        try:
            self.sheet.pictures.add(self.filePath, left=left, top=top, width=width, height=height, scale=None, name=name)
        except Exception:  # 已有同名图片，采用默认命名
            pass

    #从文件中逐页提取图片标签进入表中
    def FIGsearch1(self):
        line=2
        for page in self.doc:
            text=page.getText()
            #匹配图片标签正则式
            fig=re.findall('[\n,\t]fig\. [0-9]{1,}\. .{1,300}\n',text,re.I|re.S) 
            #逐个提取匹配图片标签与图片
            for i in fig:
                print(i)
                self.sheet.range('C%s'%(line+1)).value=i
                line+=1

    #从文件中逐页提取文中图片描述进入表中
    def FIGsearch2(self):
        for i in range(1,self.num,1):
            for page in self.doc:
                text=page.getText()
                #匹配文中图片描述正则式
                fig=re.findall('.{1,200}fig\. %s.{1,200}\n'%(i),text,re.I|re.S)
                #逐个将匹配图片标签与图片放入表内
                self.sheet.range('D%s'%(i+2)).value=fig
                continue

def select_file(filename):
    filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
    )

    filename[0] = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

# open button


# if __name__=='__main__'():
#     print('please use it as a module!')