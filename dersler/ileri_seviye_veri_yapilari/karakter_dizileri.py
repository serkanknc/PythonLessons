
#?upper() ve lower()

#* upper() metodu stringin tüm karakterlerini büyük harfe çevirir.
#* lower() metodu stringin tüm karakterlerini küçük harfe çevirir.

"python".upper()

"PYTHON".lower()

#? replace()

#* replace(x,y) : Stringteki x değerlerini y ile değiştirir.

"Herkes ana baba bacı gardaş".replace("a","o")

#? startswith() ve endswith()

#* startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.
#* endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.

"Python".startswith("py")#false
"Python".startswith("Py")#true

"Python".endswith("on")#true
"Python".endswith("az")#false


#? split()

#* split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.

liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.

liste2 = "Python-Php-Java-C-Javascript".split("-")


#? strip() , lstrip() ve rstrip()

#* strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.
#* lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.
#* rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

"                   python                          ".strip() # değer göndermezsek varsayılan olarak boşluk karakteri silinir.
">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")
"                            python      ".lstrip()
"                            python      ".rstrip()


#? join()

#* Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.

liste = ["21","02","2014"]
"/".join(liste)

liste = ["T","B","M","M"]
".".join(liste)

#? count()

#* count(x): Stringin içindeki x değerlerini sayar.
#* count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.

"ada kapısı yandan çarklı".count("a")
"ada kapısı yandan çarklı".count("a",2)

#? find() ve rfind()

#* find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
#* rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

"araba".find("a")
"araba".find("s")

"araba".rfind("a")
"araba".rfind("s")