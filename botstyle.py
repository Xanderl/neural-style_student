import os


img = input("content enter hal9000.png:")
pic = input("style enter bob.jpg:")
name = input("name enter name of new file .png:")

os.system("python neural_style.py --content " + img +" --styles " + pic +" --output " + name +" --width 500")


