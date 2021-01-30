# FBLA Quiz

Quiz about various aspects of FBLA!

It randomly generates a 5 question quiz based off a 50 question database in `questions.json`

---

## Tools Used

### 3rd party licenses used in code

- I used [Kivy](https://kivy.org/#home), a cross-platform python library to make the GUI for my app
  - It is released under the [MIT License](https://github.com/kivy/kivy/blob/master/LICENSE)  
- Although Kivy provided the base for the GUI, I primarily used [KivyMD](https://github.com/kivymd/KivyMD), a library of Google's [Material Design](https://material.io/design)-adherent Kivy widgets
  - This is also licensed under the [MIT License](https://github.com/kivymd/KivyMD/blob/master/LICENSE)

Kivy(MD) was the primary 3rd party library I used throughout the app, but for the printing functionality I used a couple others:  

- [Dominate](https://github.com/Knio/dominate/), which I used to programmatically generate a HTML document
  - Released under the [GNU LGPL v3 License](https://github.com/Knio/dominate/blob/master/LICENSE.txt)
- [WeasyPrint](https://www.courtbouillon.org/weasyprint), used to convert the HTML document to a PDF file
  - Licensed under the [BSD 3-Clause "New" or "Revised" License](https://github.com/Kozea/WeasyPrint/blob/master/LICENSE)


- The license of this project (GNU GPL v3) is adherent to conditions set by the 3rd party libraries included.

### Version Control

This project uses Git, and the code is stored on GitHub. You can view it [here](https://github.com/ojas-sanghi/FBLA-Quiz), and the commit history [here](https://github.com/ojas-sanghi/FBLA-Quiz/commits/master)


### Code Formatting

This project uses [Black](https://github.com/psf/black) as a code formatter tool. 

### Dependencies

I used [pipenv](https://pipenv.pypa.io/en/latest/) to install and maintain project dependencies. They can be viewed in `Pipfile`

---

## Installation and Usage

Note: you need Python 3.8 to run this project

   1. First, install Kivy for your OS [here](https://kivy.org/doc/stable/gettingstarted/installation.html)
   2. Clone and `cd` to directory
   3. `pip install --user pipenv` to install pipenv if you don't already have it
   4. `pipenv shell` to enter a virtual environment shell
   5. `pipenv install` to install dependencies from `Pipfile`
   6. `python3 main.py` to run the app