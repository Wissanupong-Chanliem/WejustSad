from cryptography.fernet import Fernet
import random
def add_klong():
    key = b'Viu6qE2q84D2mexxSwBQc_Fsj-_OMXGcGQXjeo2k9XI='
    f = Fernet(key)
    data = open("achievement\\achievement_k.txt","r",encoding="utf-8").readline()
    decrypt = f.decrypt(data).decode()
    space = []
    for i,v in enumerate(decrypt):
        if v==" ":
            space.append(i)
    space = random.choice(space)
    decrypt = decrypt[:space+1]+"กล้องเองฮะ "+decrypt[space+1:]
    file = open("achievement\\achievement_k.txt","r+",encoding="utf-8")
    file.truncate(0)
    file.writelines(f.encrypt(decrypt.encode()).decode())
    file.close()

def check_klong():
    key = b'Viu6qE2q84D2mexxSwBQc_Fsj-_OMXGcGQXjeo2k9XI='
    f = Fernet(key)
    data = open("achievement\\achievement_k.txt","r",encoding="utf-8").readline()
    decrypt = f.decrypt(data).decode()
    if " กล้องเองฮะ " in decrypt:
        return 1
    return 0
