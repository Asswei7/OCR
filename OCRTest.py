import os
#  pytesseract准确率太差
# import pytesseract
# from PIL import Image
#
# tesseract_cmd = r'D:\Download\Tesseract\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd =tesseract_cmd
#
# os.environ['TESSDATA_PREFIX'] = 'D:\\Download\\tessdata'
#
# text = pytesseract.image_to_string(Image.open(r"E:\Habei\TestImport\video\merge\e_27300.jpg"), lang='chi_sim')
# print(text)

from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory


# 选择你要识别的图片路径
def get_files():
    for filepath, dirnames, filenames in os.walk(r'/video/merge'):
        for filename in filenames:
            print(os.path.join(filepath, filename))
            f = os.path.join(filepath, filename)
            result = ocr.ocr(f, cls=True)
            for line in result[0]:
                print(line[1][0])
                print()


def singlePic(img_path):
    result = ocr.ocr(img_path, cls=True)
    for line in result[0]:
        print(line[1][0])


# 输入是一张图片，输出文字
singlePic("/video/merge/e_53850.jpg")
