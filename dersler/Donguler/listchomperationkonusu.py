#Bu konuda listeleri üretmek ve oluşturmak Pythonda çok pratik bir yöntem olan "List Comprehension" konusunu öğreneceğiz

liste1 = [1,2,3,4,5] # Örnek 1 

liste2 = [i for i in liste1] # List Comprehension

print(liste2)

liste1 = [(1,2),(3,4),(5,6)] # Örnek 3

liste2 = [i*j for (i,j) in liste1] # List Comprehension

print(liste2)

liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4

liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension

print(liste2)

s = "Python"  # Örnek 5

liste = [i * 3 for i in s] # List Comprehension

print(liste)

# List Comprehension 

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık
print(liste2) 