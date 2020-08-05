s = input("Write something: ").lower()
sayac = 0

for i in range(len(s)):
    if str(s[i]) == "a" or str(s[i]) == "e" or str(s[i]) == "ı" or str(s[i]) == "i" or str(s[i]) == "o" or str(s[i]) == "ö" or str(s[i]) == "u" or str(s[i]) == "ü":
        sayac += 1

print("Yazdığınız kelimede "+ str(sayac) +" tane sesli harf var. ")

