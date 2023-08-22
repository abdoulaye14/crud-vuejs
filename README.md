# crud-vuejs

Cette application est conçue avec le framework Vuejs en Frontend et le framework python flask en Backend
I. Backend
1ére etape : installer python sur votre machine
2ème étape : installer un module de gestion de variables d'environnement python
  - commande : pip install venv
 3ème etape : créer une variable d'environnement python
  - commande : python -m venv env
4ème étape : activer la variables d'environnement
  - commande : env\Scripts\activate
5ème étape : installer le contenu du requirement 
  - commande : pip install -r requirements.txt

Dans notre cas une variable d'environnement est déjà disponible, elle est nommée env avec déja installé les paquets pour éxécuter le programme python
6ème étape : installer mysql
7ième étape : créer une base de données mysql
8ième étape : configurer la connexion à la base mysql depuis le fichier app
9ième étape : lancer la commande python : flask run

Permission admin
J'ai défini une variable python isAdmin (isAdmin = False) pour simuler l'authentification

II. Frontend
Il s'agit d'un petit programme en Vue qui permet de créer, modifier, lire et suppimer des données.
L'interface est disponible avec le fichier index.html
![image](https://github.com/abdoulaye14/crud-vuejs/assets/110430189/8ef49f16-1845-483f-9536-051808fdab0a)

Create/Update
![image](https://github.com/abdoulaye14/crud-vuejs/assets/110430189/04f3003d-f860-4074-8642-95897da701c9)

Validation
![image](https://github.com/abdoulaye14/crud-vuejs/assets/110430189/a052d246-c634-4dab-99eb-f38611406dc8)

Delete
![image](https://github.com/abdoulaye14/crud-vuejs/assets/110430189/d03b73ec-0715-47a7-9f4d-110317df474a)



