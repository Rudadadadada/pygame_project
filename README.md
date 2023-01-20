<h1><img align="center" src="https://user-images.githubusercontent.com/57627872/213796048-097be178-94ce-42c0-b944-cbaa1da320f0.png" height="30" width="33"" alt="rudadadadada" height="30" width="40" /> Mortal Combat by Ruda</h1>

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11-brightgreen"></a>
<a href="https://www.pygame.org/"><img src="https://img.shields.io/badge/Powered%20by-Pygame-yellow"/></a>

## ✒ Project description

- This is a ***desktop game*** similar to ***Mortal Kombat*** for two players. Two characters fight with each other through fireballs. The one who runs out of lives loses.

- It is an ***educational project*** made within the framework of ***Yandex.Lyceum***.

## 🎬 Demo
![gif of working](https://user-images.githubusercontent.com/57627872/213806720-d773cd0f-2c2e-40eb-86ce-529538a0d3d6.gif)

## 🧩 Functionality

### 1️⃣ Game movements

Each character moves by pressing buttons on the keyboard. 

***Movement buttons for the characters:***
- ***Jump*** for the ***right*** character is ***the up arrow key*** and ***the W key*** for the ***left***. 
- ***Sit*** for the ***right*** character is ***the down arrow key*** and ***the S key*** for the ***left***.
- ***Go left*** for the ***right*** character is ***the left arrow key*** and ***the A key*** for the ***left***.
- ***Go right*** for the ***right*** character is ***the right arrow key*** and ***the D key*** for the ***left***.
- ***Throw a fireball*** for the ***right*** character is ***the right ctrl*** and ***the F key*** for the ***left***.

### 2️⃣ Collision of fireballs

When fireballs collide, they are destroyed.
  
  
## 🛠️ Tools
- <a href="https://www.postgresql.org/">Database PostgreSQL <img src="https://user-images.githubusercontent.com/57627872/213761059-d18cd77b-29b9-4e20-8f14-3efb384594de.png" height="20" width="20"></a>
- <a href="https://pypi.org/project/pyTelegramBotAPI/">Library telebot <img src="https://user-images.githubusercontent.com/57627872/213766820-75929ee4-6ec0-449e-9d6a-93615fbadb52.png" height="20" width="20"></a>
- <a href="https://www.sqlalchemy.org/">SQLAlchemy <img src="https://user-images.githubusercontent.com/57627872/213767906-ed3861b2-dd7b-4fa4-b626-4808e3b67a13.png" height= "20" width="20"></a>

## 🧮 How data is stored in the database?
***Here are two data storage schemes and the relationships between the models.***

### 📊 First scheme:

There is an admin at the top of everything, he can view information about clients. ***Let's take some client, he has lots of accounts, accounts have lots of cards, cards have lots of transactions.***

<img src="https://user-images.githubusercontent.com/57627872/212759769-a12e421f-786b-4426-a3fb-6176452d8265.png" height="350" width="500">


### 📊 Second scheme:

***The transaction stores information about how much money was spent, at what time and date, the id of the card number and the id of the store where the purchase was made.*** 

The store has a parameter ***merchant category code***, by which we determine which category this store belongs to.

<img src="https://user-images.githubusercontent.com/57627872/212759935-a8ffbf1b-a6e2-475b-8c5f-fbaab46a546f.png" height="150" width="400">

## 📄 What development patterns were used?

### 👀 The observer pattern.

A chatbot is ***a state tree*** where each ***button click is a transition between these states***. The ***administrator*** of the bank in this case ***is an observer***.

### 🪧 The query builder.

When transitions between states are made, ***parameters are also selected to form a query*** to the database.

## ⚙️ Contributors
There are two contributors:

<a href = "https://github.com/rudadadadada/bank_transactions/graphs/contributors">
<img src = "https://contrib.rocks/image?repo=rudadadadada/bank_transactions"/>
</a>
