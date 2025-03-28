"""
-Məhsul - id, kateqoriya, ad, qiymət, say
-Alıcı - id, ad
-Tranzaksiya - id, məhsul id, say, qiymət, cəm, tarix, ədv
-Hesabat
-Loq
"""
import datetime
#kateqoriya = {{"id":1,"ad":"meyve","edv":0},}
mehsul = {1:{"kateqoriya":"meyve","ad":"alma","qiymet":3,"say":50,"edv":0},2:{"kateqoriya":"meyve","ad":"armud","qiymet":4,"say":40,"edv":0},3:{"kateqoriya":"ichki","ad":"kola","qiymet":5,"say":25,"edv":18}}
alici_kart = {1:{"ad":"Ali"},2:{"ad":"Hasan"}}
qebz = []
print("Mehsulu sechin, alish-verishi bitirmek uchun 0 yazin")
for i in mehsul:

    print(f"{i}-{mehsul[i]["ad"]}-{mehsul[i]["qiymet"]} azn")

while True:
    sechim = int(input("Mehsulu sechin:"))
    say = int(input("Miqdarini sechin:"))
    mehsullar = []
    mehsullar.append(sechim)
    mehsullar.append(say)
    if sechim == 0:
        break
    qebz.append(mehsullar)
    say = 0
    for i in qebz:
        print(f"{mehsul[i[0]]["ad"]} - {mehsul[i[0]]["qiymet"]} AZN, {qebz[say][1]}, CEM:{mehsul[i[0]]["qiymet"]*qebz[say][1]} AZN")
        say+=1
mehsul_sayi = 0
cem = 0
for i in qebz:
    print(f"{mehsul[i[0]]["ad"]} - {mehsul[i[0]]["qiymet"]} AZN, {qebz[say][1]}, CEM:{mehsul[i[0]]["qiymet"]*qebz[mehsul_sayi][1]} AZN")
    cem+=mehsul[i[0]]["qiymet"]*qebz[mehsul_sayi][1]
    mehsul_sayi+=1
print("Yekun odenish: ", cem, " AZN")

zaman = datetime.datetime.now()
qebz_to_string = ''.join(map(str,qebz))
tranzaksiya = str(zaman)+"***"+qebz_to_string+"***"+str(cem)+" AZN ***"+"\n"
with open("c:/Users/HP/Documents/Projects/Lessons/Django/store/tranzaksiya.txt",'a') as file:
    file.write(tranzaksiya)


with open("c:/Users/HP/Documents/Projects/Lessons/Django/store/tranzaksiya.txt","r") as file:
    loglar = file.readline()

print(loglar)