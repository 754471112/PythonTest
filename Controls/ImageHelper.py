from PIL import Image,ImageFilter

class ImageHelper(object):
    def __init__(self):
        pass

    def StartImgTest1(self):
        im=Image.open("ori1.jpg")
        im2=im.filter(ImageFilter.BLUR)
        im2.save("change.jpg",'jpeg')
