import hashlib
import json
from turtle import pd
import pandas as pd


nombre_archivo = "secures-user.json"

def hashPswd(password):
    hasedPswd = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hasedPswd
def leerYescribir():
    with open("users.json", "r") as j:
        usuarios = json.load(j)
        print(usuarios)

    with open(nombre_archivo, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

        for usuario in usuarios:
            password = usuario['password']

    passwordHas = hashPswd(password)
    print(passwordHas)

leerYescribir()

def crearExcel():
    with open(nombre_archivo, "r") as j:
        usuarios = json.load(j)

    for usuario in usuarios:
        userId = usuario['userId']
        print(userId)
        password = usuario['password']
        print(password)
        userName = usuario['userName']
        print(userName)
        userSurname = usuario['userSurname']
        print(userSurname)


        userId = [entry["userId"] for entry in usuarios]
        userName = [entry["userName"] for entry in usuarios]
        password = [entry["password"] for entry in usuarios]
        userSurname = [entry["userSurname"] for entry in usuarios]
        # relacionar la data
        df = pd.DataFrame({'userId': userId,
                           'userName': userName,
                           'password': password,
                           'userSurname': userSurname,
                           })

        nombre_excel = f"libros.xlsx"
        df.to_excel(nombre_excel, index=False)

        print(f"Archivo Excel '{nombre_excel}' creado exitosamente.")

crearExcel()