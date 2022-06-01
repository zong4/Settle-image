# -*- coding : utf-8 -*-
# @Time      : 2022/6/1 19:50
# @Author    : Zong
# @File      : main.py
# @Software  : PyCharm
# @Function  :
# @ChangeLog :


import os
import cv2

# Path
imagePath = r"D:\Users\Zong\Desktop\source"
imagePathSettled = r"D:\Code\Blog\source\gallery\travel\Nanjing\Sceneries"
filePath = imagePathSettled + '\\' + 'index.md'
imagePathWritten = "../gallery/travel/Nanjing/Sceneries/" + 'source' + '/'

# The string written
markdownWriteString = "---" + "\n" + "title: 风景" + "\n" + "date: 2022-06-01 20:20:08" + "\n" + "---" + "\n" + "\n"
markdownWriteString = markdownWriteString + "{% gallery %}" + '\n' + '\n'

# Rename and sort
index = 1
for imageName in os.listdir(imagePath):

    image = cv2.imread(imagePath + '\\' + imageName)

    # All is .jpg
    cv2.imwrite(imagePathSettled + '\\source\\' + '{}.jpg'.format(index), image)
    markdownWriteString = markdownWriteString + "![](" + imagePathWritten + '{}.jpg'.format(index) + ")" + '\n'
    index = index + 1

markdownWriteString = markdownWriteString + '\n' + '{% endgallery %}'

# Write file in line 6
markdown = open(filePath, 'w', encoding= 'utf-8')
markdown.write(markdownWriteString)
