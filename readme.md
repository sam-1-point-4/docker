# Project Overview

This project is a deployment of a dynamic website which also uses navigation bars for a page called Titanic that has a basic chart visual from the titanic dataset. Below is an overview of the structure:

- **`docker-compose.yml`**: Defines multi-container Docker applications.
- **`Dockerfile`**: Specifies the environment and dependencies for the application.
- **`.dockerignore and .gitignore`**: Specifies the files from the local project directory that are ignored by docker and git respectively.
- **`app.py`**: The lightweight flask application that is the basis for the webpage
- **`templates`**: A folder with the templates for the two created webpages with styles and so on.
- **`computation.py`**: A file that was used to display some basic for loop based calculations.
