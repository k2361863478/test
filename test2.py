from PIL import Image
img=Image.open('./imgs/1.png')
w=img.size[0]
h=img.size[1]
result=img.crop((0,0,w*0.5,h*0.5))
result.save('p.png')