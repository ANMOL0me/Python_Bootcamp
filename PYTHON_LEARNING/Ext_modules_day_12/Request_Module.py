#get request

import requests
r = requests.post('https://api.github.com/users/ANMOL0me',data ={"login":"ANMOL0me"})
print(r.text)
with open("Anmol0meupdated.txt","w") as f :
    f.write(r.text)