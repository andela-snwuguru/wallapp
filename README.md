# wallapp
Express yourself on the wall

# How to use

To install and run this application locally, you need to have python and postgres installed on your machine.

## Installation

To install the build locally. Create and activate a virtual environment.

- $ git clone https://github.com/andela-snwuguru/wallapp.git
- $ cd wallapp
- $ pip install -r requirements.txt

## Setting up the configurations

rename .env.example to .env and change the values to your local database credentials

## Available endpoints

- https://wallapi.herokuapp.com/api/login/ POST
- https://wallapi.herokuapp.com/api/register/ POST
- https://wallapi.herokuapp.com/api/walls/ POST, GET
- https://wallapi.herokuapp.com/api/walls/1/likes/ POST, GET
