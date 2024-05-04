from PIL import Image,ImageFilter

#image = Image.open("fb.jpg") # iamge açar
#image.rotate(77).save("fb2.jpg") # rotate fonksiyonu image ı döndürür belirtilen derecede
#image.save("fb2.jpg")# image kaydeder

#image.convert(mode="L").save("fb3.jpg") # image ı siyah beyaz yapar

#degistir = (300,200) # hangi boyutta ayarlayacağımızı tupple şeklinde objeye atadık
#image.thumbnail(degistir) # objeyi fonksiyona gönderdik ve boyutlar değişti
#image.save("fb3.jpg")

#image.filter(ImageFilter.GaussianBlur(6)).save("fb3.jpg") # image ı blurlaştırdık blur değeri ne kadar artarsa o kadar bulanık olur..

image2= Image.open("ataturk.jpg")

kirpma_alani = (600,0,800,500)
image2.crop(kirpma_alani).save("fb3.jpg")