# ENG: Vowel counter based on Turkish alphabet.
# TR: Girilen cümledeki sesli harfleri sayar.

lang = input("1. Türkçe için TR yazın\n2. Type ENG for English:\n").upper()

# English UI
if (lang == "ENG"):
    s = input("Write something: ").lower()
    counter = 0

    for i in range(len(s)):
        if str(s[i]) == "a" or str(s[i]) == "e" or str(s[i]) == "ı" or str(s[i]) == "i" or str(s[i]) == "o" or str(s[i]) == "ö" or str(s[i]) == "u" or str(s[i]) == "ü":
            counter += 1

    print("You wrote something that has " + str(counter) + " vowels. ")

# Türkçe arayüz
elif (lang == "TR"):
    s = input("Bir cümle girin: ").lower()
    sayac = 0

    for i in range(len(s)):
        if str(s[i]) == "a" or str(s[i]) == "e" or str(s[i]) == "ı" or str(s[i]) == "i" or str(s[i]) == "o" or str(s[i]) == "ö" or str(s[i]) == "u" or str(s[i]) == "ü":
            sayac += 1

    print("Yazdığınız kelimede "+ str(sayac) +" tane sesli harf var. ")

else:
    print("\nGeçersiz bir dil paketi seçtiniz.\n\nYou picked the wrong house fool :)")

