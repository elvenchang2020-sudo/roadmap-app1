## Basic docker structure (with single container)
### 1. Dockerfile
A Dockerfile is a plain text file containing commands and instrcitons for what the app needs. It has to be the exact name with the capitalzied D, no space, no underscore, and no extension. Because the system will automatically look for it.  

The structure is as follows:  

**`FROM python:3.14-slim`**  
This line specifies the base image. Docker has prepared many offical images, such as Python, Ubuntu and Node.js.  
**`WORKDIR /app0`**   
This sets the working directory inside the container. All subsequent commands are executed relative to this directory.  
**`COPY . .`**  
This copies all files from the current project directory on the host machine into the current working directory inside the container.   
**`RUN pip3 install -r requirements.txt`**   
Installs all Python dependencies listed in requirements.txt.  
**`CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]`**   
Specifies the default command that runs when the container starts. For a Streamlit application, this launches the Streamlit server.

### 2. Image
An Image created with the instruction in Dockerfile bundled source code, base opertaing system layer, the required libaries and the default startup command into a single read-only package.

**(In terminal) `docker build -t app_name .`**  
Docker follows the instructions in the Dockerfile step by step and creates the image. directory (.), follow its instructions step-by-step, and bake everything into a tagged (-t) Image named "app_name".

### 3. Container
A Container is a live, running, isolated instance of an Image where the app is actively executing.

**(In terminal) `docker run -p 8501:8501 -d app_name .`**   
This command takes your static Image and spins it up into a running container in the background (-d), mapping port 8501 on the local machine to port 8501 inside the container (-p).
