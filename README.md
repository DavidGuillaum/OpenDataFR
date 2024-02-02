<h1 align="center">OpenDataFr</h1>

<p align="center">
The goal of this project is to create a small web-app displaying some data. I'll apply the concept of API and Pipeline.

<br>
  <a href="https://opendata.fr.ch/pages/home/"><strong>Open Data portal of Fribourg Canton</strong></a>
  <br>
  <a href="https://medium.com/@guillaume.david11"><strong>My blog post</strong></a>
  <br>
</p>

## Table of contents

- [How to run the project](#How-to-run-the-project)
- [Motivation and goals](#Motivation-and-goals)
- [Structure](#Structure)
- [Author and acknowledgement](#author-and-acknowledgement)

## How to run the project

Here is the list of installed packages for this proj


Clone the GitHub repository and use Anaconda distribution of Python 3.11.

    $ git clone https://github.com/DavidGuillaum/OpenDataFR.git

In addition This will require pip installation of the following:

     pip install pandas
     pip install sys
     pip install numpy
     pip install plotly
     pip install flask


- To run the dashboard<br>
    ```python app\run.py```


## Motivation and goals

The goals of this project are the following:
- I. Create a web-app displaying a dashboard
- II. Make API REST request
- III. Automate with a ETL Pipeline


## Structure
This project is structure is 3 main folders/parts: app, data and models. The app folder will contains everything related to the web app. Regarding the data, there are 2 raw dataset, one SQL DB (we want to stock it here at the end) and a python file containing all the process of cleaning... The last main folder named model will contains the file to train the model and the trained model.
- app
    - template
        - master.html  # main page of web app
        - go.html  # classification result page of web app
    - run.py  # Flask file that runs app

- data
    - disaster_categories.csv  # data to process 
    - disaster_messages.csv  # data to process
    - process_data.py   #python code to load-clean-save the data (ETL Pipeline)
    - disaster_response.db   # database to save clean data into

- models
    - train_classifier.py
    - model.pkl  # saved model 

- README.md

- project_preparation
    - ETL_Pipeline.ipynb   # Jupyter file to transform the data
    - ML_Pipeline.ipynb   # Jupyter file to create the model
    - disaster_response.db   # database to save clean data into

<br>



## Author and acknowledgement
I'm David Guillaume, currently studying for a master's degree in Data Analytics and Economics at the University of Fribourg (Switzerland). I'm very interested in data sciences and economics in particular (bachelor's degree in Political Economy). I hope you'll like my project. I would like to thank Udacity for overseeing this program.
<br>
<a href="https://www.linkedin.com/in/david-guillaume-a7bb1b201/"><strong>Here is my Linkedin</strong></a>
<br>