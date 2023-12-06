def encrypteer(tekst):
    versleuteld = ""
    for karakter in tekst:
        if karakter.isalpha():
            basis = ord('a') if karakter.islower() else ord('A')
            verschoven = (ord(karakter) - basis + 5) % 26 + basis
            versleuteld += chr(verschoven)
        else:
            versleuteld += karakter
    return versleuteld

def decrypteer(versleuteld):
    ontsleuteld = ""
    for karakter in versleuteld:
        if karakter.isalpha():
            basis = ord('a') if karakter.islower() else ord('A')
            verschoven = (ord(karakter) - basis - 5) % 26 + basis
            ontsleuteld += chr(verschoven)
        else:
            ontsleuteld += karakter
    return ontsleuteld

te_encrypteren_tekst = input("Geef de tekst die je wilt encrypten:\n")

versleutelde_tekst = encrypteer(te_encrypteren_tekst)
print(f"Versleutelde tekst: {versleutelde_tekst}")

ontsleutelde_tekst = decrypteer(versleutelde_tekst)
print(f"Ontsleutelde tekst: {ontsleutelde_tekst}")
