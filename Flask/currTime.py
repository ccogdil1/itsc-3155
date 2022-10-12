from flask import Flask, render_template #Flask library

import datetime #Get the current datetime

import calendar #To get the day

#Initalizing a flask app

currTime = Flask(__name__)

#routing at '/'

@currTime.route('/')

def index():

    #sets the current time 
    current_time = datetime.datetime.now()
    
    #turns the time into a string
    ctime = current_time.strftime("%B %d %Y %H:%M:%S")

    #returns the data and time formatted
    return render_template('index.html', ctime = calendar.day_name[current_time.weekday()] + ', ' +ctime)

if __name__ == '__main__':

    currTime.run()