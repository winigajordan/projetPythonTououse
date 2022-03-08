import base64
import os
databaseFilePath = "./database/users.txt"

#fonction de verification du chemin vers le fichier de rauvegarde (renvoi un boolean)
def checkPath():
    if os.path.exists(databaseFilePath):
        return True
    else:
        return False


#fonction pour donner un nouvel id à un nouvel utilisateur  (renvoi un entier)
def newId():
    return len(getAllUsers())+1


#fonction de recuperation de tous les joueurs (renvois un tableau de tableau d'utilisateurs)
def getAllUsers():
    usersData = open(databaseFilePath, 'r')
    users = usersData.readlines()
    userTab = []
    for user in users:
        userTab.append(user.split("|"))
    usersData.close()
    return userTab


#fonction de creation de compte qui renvoie True en cas d'enregistrement effectué et false dans le cas contraire
def createAccount(nom, prenom, age, login, password):
    if (checkPath):
        id = newId()
        pwd = base64.b64encode(password.encode("utf-8")) #fonction d'encodage du mot de passe (pour pas afficher le mot de passe en cair dans le fichier de sauvegarde)
        db = open(databaseFilePath, "a")
        db.write(f"{id}|{nom}|{prenom}|{age}|{login}|{pwd}|0 \n")
        db.close() 
        return True
    else : 
        print('le chemin vers le fichier de sauvegarde n\'existe pas')
        return False



#fonction de login(renvoie un tableau avec les information de l'utilisateur si la connexion est établie sinon, renvoie un tableau vide)
def login(login, password):
    if (checkPath):
        users = getAllUsers()
        for user in users : 
            if (user[4]==login and user[5] == str(base64.b64encode(password.encode("utf-8")))):
                return user
        return []
    

#fonction de mise à jour des données de l'utilisateur
def updateUserData(newUser):
    allUsers = getAllUsers()
    db = open(databaseFilePath, 'w+')
    for user in allUsers:
        if user[0] == newUser[0]:
            user = newUser
        db.write('|'.join(user))
    db.close()
    

    
#userTest = ['3', 'xxx', 'haaa', '15', 'steph', "b'bGl6'", '0 \n']
#updateUserData(userTest)
#createAccount('xxx', 'yyy', 15, 'light', 'liz')
#print(login('light', 'liz'))

"""
 [
    ['1', 'xxx', 'yyy', '15', 'light', "b'bGl6'", '0 \n'], 
    ['2', 'xxx', 'yyy', '55', 'light', "b'bGl6'", '0 \n'], 
    ['3', 'xxx', 'yyy', '15', 'light', "b'bGl6'", '0 \n']
] 
"""