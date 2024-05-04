import os



for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/monster/Desktop"):
    for i in klasör_isimleri:
        if (i.startswith("kr")):
            print(i)



# print(dir(os))

#print(os.getcwd())

# os.chdir("C:/Users/user/Desktop/")


#print(os.getcwd())


#print(os.listdir())

#os.mkdir("Deneme1")

#os.makedirs("Deneme2/Deneme3")

#os.rmdir("Deneme2/Deneme3")

#os.rename("dersler/Deneme32332322","Deneme333333333")
#os.removedirs("Deneme1/sadasd32")

# os.rename("test.txt","test2.txt")

# print(os.stat("test2.txt"))

# degistirilme = os.stat("test2.txt").st_mtime

# print(datetime.fromtimestamp(degistirilme))


for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/monster/Desktop"):

    print("Klasör yolu: ",klasör_yolu)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")





