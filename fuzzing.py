import requests
dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()
header={"Cookie": "security=low; PHPSESSID=a0bert32564er2wers213512321"}
for i in icerik.split("\n"):
    print(i)
    url="http://10.10.10.10"+str(i)
    sonuc=requests.get(url=url,headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var:", i)
    else:
        print("Dosya veya dizin yok:",i)