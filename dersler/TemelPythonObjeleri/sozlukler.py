# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
sözlük1 = {"sıfır":0,"bir":1,"iki":2,"üç":3}

# Boş bir sözlük
sözlük2 = {}

# Boş bir sözlük - dict() ile 
sözlük2 = dict()

# "bir" anahtarına karşılık gelen değeri buluyoruz.
sözlük1["bir"]

a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}

# İçiçe listeleri biliyoruz.
a["iki"][1][1]

a["dört"] = 4 

# İç içe sözlük
a = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
a["sayılar"]["bir"]

yeni_sözlük = {"bir":1,"iki":2,"üç":3}

# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
yeni_sözlük.values()

# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
yeni_sözlük.keys()

# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
yeni_sözlük.items()