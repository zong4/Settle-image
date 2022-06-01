# 介绍

分别需要修改图片源路径，处理图片存放路径，文件的开头以及相关格式。

```python
# Path
imagePath = r"D:\Users\Zong\Desktop\source"
imagePathSettled = r"D:\Code\Blog\source\gallery\travel\Nanjing\Sceneries"
filePath = imagePathSettled + '\\' + 'index.md'
imagePathWritten = "../gallery/travel/Nanjing/Sceneries/" + 'source' + '/'

# The string written
markdownWriteString = "---" + "\n" + "title: 风景" + "\n" + "date: 2022-06-01 20:20:08" + "\n" + "---" + "\n" + "\n"
markdownWriteString = markdownWriteString + "{% gallery %}" + '\n' + '\n'
```

为了统一图片格式，均使用了默认后缀名 **.jpg** 。

```python
# Rename and sort
index = 1
for imageName in os.listdir(imagePath):

    image = cv2.imread(imagePath + '\\' + imageName)

    # All is .jpg
    cv2.imwrite(imagePathSettled + '\\source\\' + '{}.jpg'.format(index), image)
    markdownWriteString = markdownWriteString + "![](" + imagePathWritten + '{}.jpg'.format(index) + ")" + '\n'
    index = index + 1
```

# 操作须知

1. 本代码主要用于 **Hexo** 的 **butterfly** 主题下的 **gallery** 展示，当然其它地方亦可使用。
2. pip install opencv2
3. 如果不需要创建 **index.md** 文件，可以将相关代码注释。
