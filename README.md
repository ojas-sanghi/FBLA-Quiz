# FBLA Quiz

Quiz about various aspects of FBLA!

It randomly generates a 5 question quiz based off a 50 question database which it retrieves from a remote server.
There are 6 different types of questions, and once you finish the quiz, it will tell you the results of the quiz and also present the option to open a PDF file with detailed information, which you can print.

## Server-side Code

This app interacts with a server to retrieve the questions. The GitHub repo for the server can be found [here](https://github.com/ojas-sanghi/FBLA-Quiz-Server)

## Features

- 6 different types of questions; 50 question database
  - choose all that apply
  - matching
  - multiple choice
  - fill in the blank
  - short answer (multiple words; like a person's name)
  - true/false

- progress bar and text tells you how far along you are in the quiz
- interactively tells you if you got a question right/wrong after each, and gives you an overview at the end
- typed answers are case-insensitive
- can restart quiz
- can generate a printable report by the press of a button

- questions are guaranteed to be unique when you run it

- time-dependent light/dark mode
  - switches between light mode and dark mode based on local time
  - uncomment and change line 74 in `FBLAQuizApp.py` to manually override

- securely retrieves questions from a remote server, and are backed up on GitHub

## Design Choices

- Kivy was completely new for me, but it looked like a good platform to make an app.
  - popular, lots of resources online, cross-platform, uses Python which I already was familiar with, etc
- The design and logic are separated; they are split into `.kv` and `.py` files, respectfully. That way, one could work on the design without messing up, or even having to know, the logic, or vice versa.

## Tools Used

### 3rd party licenses used in code

- I used [Kivy](https://kivy.org/#home), a cross-platform python library to make the GUI for my app
  - It is released under the [MIT License](https://github.com/kivy/kivy/blob/master/LICENSE)  
- Although Kivy provided the base for the GUI, I primarily used [KivyMD](https://github.com/kivymd/KivyMD), a library of Google's [Material Design](https://material.io/design)-adherent Kivy widgets
  - This is also licensed under the [MIT License](https://github.com/kivymd/KivyMD/blob/master/LICENSE)
  - I also used some widgets from [akivymd](https://github.com/quitegreensky/akivymd), a library containing customized widgets utilizing the KivyMD library
    - This, too, is under the [MIT License](https://github.com/quitegreensky/akivymd/blob/master/LICENSE)

Kivy(MD) was the primary 3rd party library I used throughout the app, but for the printing functionality I used another:

- [Dominate](https://github.com/Knio/dominate/), which I used to programmatically generate a HTML document
  - Released under the [GNU LGPL v3 License](https://github.com/Knio/dominate/blob/master/LICENSE.txt)
- [Materialize CSS framework](https://materializecss.com/) (similar to bootstrap) to style the HTML document and make it look good
  - Released under the [MIT License](https://github.com/Dogfalo/materialize/blob/v1-dev/LICENSE)

For the encryption functionality between this app an the server, these libraries were used:
- [pycryptodome](https://github.com/Legrandin/pycryptodome/), used to construct an AES key and decrypt the question file.
  - The source code is released into the [public domain](https://github.com/Legrandin/pycryptodome/blob/master/LICENSE.rst)
- [rsa](https://github.com/sybrenstuvel/python-rsa), which I used to generate the public/private RSA keyset
  - Released under the [Apache-2.0 License](https://github.com/sybrenstuvel/python-rsa/blob/main/LICENSE)
- [Requests](https://github.com/psf/requests), used to send a GET request to the server and retrieve the question files
  - Released under the [Apache-2.0 License](https://github.com/psf/requests/blob/master/LICENSE)

The license of this project (GNU GPL v3) is adherent to conditions set by the 3rd party libraries included.

### Version Control

This project uses Git, and the code is stored on GitHub. You can view it [here](https://github.com/ojas-sanghi/FBLA-Quiz), and the commit history [here](https://github.com/ojas-sanghi/FBLA-Quiz/commits/master)

### Code Formatting

This project uses [Black](https://github.com/psf/black) as a code formatter tool. 

### Dependencies

I used [pipenv](https://pipenv.pypa.io/en/latest/) to install and maintain project dependencies. They can be viewed in `Pipfile`

## Installation and Usage

Note: you need Python 3.8 to run this project

   1. First, install Kivy for your OS [here](https://kivy.org/doc/stable/gettingstarted/installation.html)
   2. Clone and `cd` to directory
   3. `pip install --user pipenv` to install pipenv if you don't already have it
   4. `pipenv shell` to enter a virtual environment shell
   5. `pipenv install` to install dependencies from `Pipfile`
   6. `python3 main.py` to run the app