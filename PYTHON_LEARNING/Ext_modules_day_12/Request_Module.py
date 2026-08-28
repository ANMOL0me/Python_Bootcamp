import requests
r = requests.get('https://api.github.com/users/ANMOL0me')
print(r.text)
with open("Anmol0me.txt","w") as f :
    f.write(r.text)