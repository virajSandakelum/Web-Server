
# Create a Simple Web Server

## Introduction 

- This is a simpe web server.
- Created by the Python programing language.
- Here not used the built-in HTTPServer module.
- Here used Socket Programing concept.
- What's the Socket Programing - https://realpython.com/python-sockets/

## File Introduction

 - server.py => Server source code 
 - htdocs => Contain web pages
 - readme => Contains instructions to execute the web server


## Installation



Preparing the Environment to Run the Program

1. Clone the Git Repository From the by GitHub or Download the Zip file From my GitHub
```bash
  https://github.com/virajSandakelum/Web-Server.git
```

2. Download & Install the Python on Your Os:
```bash
  - Windows
  - Ubuntu
  - Mac 
```

```bash
  https://www.python.org/downloads/
```

3. Start the Web Server

Run the server.py file, type in the terminal:
```bash
  >> py server.py
```
or
```bash
  >> python server.py
```


4. Open the browser and type URL 

- To visit localhost(default routing path)
```bash
    http://localhost:2728
```
Or

```bash
    http://localhost:2728/
```

- To visit my aboutMe page
```bash
    http://localhost:2728/aboutme
```
- If visit any other pages 
```bash
    404 Not Found
```


## Example


01. 
- Visit localhost - http://localhost:2728
```
C:\Users\ACER\Desktop\Upcoming\Network>C:/Users/ACER/AppData/Local/Programs/Python/Python39/python.exe c:/Users/ACER/Desktop/Upcoming/Network/server.py
Socket successfully created
Socket binded to 2728
Socket is listening
Got connection from ('127.0.0.1', 1196)
Current Path :/
Connected to index.html
Got connection from ('127.0.0.1', 1197)
Current Path :/
Connected to index.html
Got connection from ('127.0.0.1', 1198)
Current Path :/
Connected to index.html
```

02.
- Visit aboutMe page - http://localhost:2728/aboutme
```
C:\Users\ACER\Desktop\Upcoming\Network>C:/Users/ACER/AppData/Local/Programs/Python/Python39/python.exe c:/Users/ACER/Desktop/Upcoming/Network/server.py
Socket successfully created
Socket binded to 2728
Socket is listening
Got connection from ('127.0.0.1', 1686)
Current Path :/aboutme
Connected to aboutMe.html
Got connection from ('127.0.0.1', 1687)
Current Path :/aboutme
Connected to aboutMe.html
```

03.
- Visit any other page - http://localhost:2728/xyz
```
C:\Users\ACER\Desktop\Upcoming\Network>C:/Users/ACER/AppData/Local/Programs/Python/Python39/python.exe c:/Users/ACER/Desktop/Upcoming/Network/server.py
Socket successfully created
Socket binded to 2728
Socket is listening
Got connection from ('127.0.0.1', 1808)
Current Path :/xyz
404 Not Found Error
```



## Authors

- [@virajSandakelumAnawarathna](https://github.com/virajSandakelum/)


## 🚀 Contact me 

Email:
- virajsandakelum8811@gmail.com
- 2020cs011@stu.ucsc.cmb.ac.lk
