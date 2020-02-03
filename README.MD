<p align="center">
    <img src="https://jenkins.io/images/logos/worldwide/worldwide.png"
        height="130">
   <h1 align="center"> ETI Game </h1>
</p>

<p align="center">
    <a href="https://hub.docker.com/repository/docker/bchewy/eti_game/">
  <img src="https://img.shields.io/docker/pulls/bchewy/eti_game?style=for-the-badge" />
    </a>
  <a href="https://hub.docker.com/repository/docker/bchewy/eti_game/">
      <img src="https://img.shields.io/docker/cloud/build/bchewy/eti_game?style=for-the-badge"/>
  </a>
    <img src="http://bchewy.me:8080/buildStatus/icon?job=eti_game"/>
</p>

<p align="center">
    <img align="center" src="https://media.giphy.com/media/fYlCJWTzTyZypIMvmk/giphy.gif"/>
</p>


#### Technologies:
- Docker 
- Jenkins
- Github
- Python

#### Devops Setup:
![Image of Workflow](https://i.imgur.com/jfo4Jlt.png)
The above image shows our team's devops setup. As you'll see, the red sections are automated to faciliate a swift and sound development-to-final product process. A full explaination can be found in the assignment report.


#### Installation Setup:
As part of one of our many deliverables, we chose to deliver & "deploy" our final product as a docker image. Each version of the software can be picked out through our docker image tags. You may pull different versions of the software at any time. 

1. Clone this repository, or use docker. (Currently v0)
``` 
# Use this method if you don't want to clone.
$ docker pull bchewy/eti_game:v0
v0: Pulling from bchewy/eti_game
Digest: sha256:488b857f7310ff25341cd23f4a6f3b664efca9e1717649425cd1c642089bb091
Status: Image is up to date for bchewy/eti_game:v0
docker.io/bchewy/eti_game:v0

# Build image directly 
$ docker build . --tag bchewy/eti_game             
Successfully built 5ab833710fae
Successfully tagged bchewy/eti_game:latest
```
2. Extract source code from within the docker image, and run the game in the container
```
$ docker run -it --entrypoint sh bchewy/eti_game:v0
# ls
Dockerfile  Jenkinsfile  README.MD  __pycache__  game.py  maze.csv  py_compileCheck.py	requirements.txt  tests
# python3 game.py

Main Menu
===================================
[1]	Read and load maze from file
[2]	View maze
[3]	Play maze game
[4]	Configure current maze

[0]	Exit
Enter your option:
```
3. You're set. You have full access to the source codes from a stable branch, and the appropriate docker environment to run it on.

#### Contributors
- Shin - Technical Lead
- Jia Wei - QA Lead
- Brian - Project Manager/Developer
- Darren - QA Engineer
- Wei Xiang - Developer
