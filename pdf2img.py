import os
from pathlib import Path
import fitz
import time

file_dir = 'D:\pdf2img'


def conver2jpg(filename):
    # print(filename)
    doc = fitz.open(filename)
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # pm.writePNG('%s.png' % pg)
        pm.writePNG(f'{str(filename).split(".")[0]}_'+str(pg)+'.jpg')

count = 0
# 用来打开所有的文件,并对每一个文件调用比对方法
def open_file(file_path, count=None):
    for demo in file_path.iterdir():
        if demo.is_file():
            if demo.name.endswith(".pdf"):
                count +=1
                print(Path(demo))
                conver2jpg(demo)
        if demo.is_dir():
            dir_demo=Path(demo)
            count = open_file(dir_demo,count)
    return count

def show_message():
    print("---------------Welcome to pdf2img--------------")
    print("Base_folder is :D\\pdf2img")
    print("     Remove your PDFs into the folder")
    print("     When U R Ready,please enter :1  Enter 0 to EXIT.")
    print("     When U R Ready,please enter :1  Enter 0 to EXIT.")
    print("     When U R Ready,please enter :1  Enter 0 to EXIT.")
    print("Enter your choice here:")


if __name__ == '__main__':
    # filenames = get_file_name(file_dir)
    show_message()
    choice = input()
    choice = int(choice)
    while(1):
        if choice == 1:
            file_num = 0
            counts = open_file(Path(file_dir), file_num)
            print("Completed Successfully! ")
            print("Converted Num of FILES:", counts)
            print("按下任意键回车退出本程序！")
            input()
            exit(0)
        elif choice ==0:
            print("    bye~   ")
            time.sleep(1)
            exit(0)
        else:
            show_message()
            choice = input()
            choice = int(choice)


