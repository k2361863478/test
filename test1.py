import datetime
import os

import fitz


def pyMuPDF_fitz(pdfPath, imagePath):
    print('开始处理')
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        zoom_x = 5
        zoom_y = 5
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        
        pix = page.getPixmap(matrix=mat,alpha=False)

        if not os.path.exists(imagePath):  
            os.makedirs(imagePath)  

        pix.writePNG(imagePath + '/' + str(pg)+'.png') 
    print('结束处理')    

if __name__ == "__main__":
    pdfPath = 'example.pdf'
    imagePath = './imgs'
    pyMuPDF_fitz(pdfPath, imagePath)