from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    link  = request.form.get('link')
    
    '''
        To do:
        Restrict only english wiki links
        check for proper url
    '''
    
    dead_link_count = find_dead_links_count(link)
    
    user = {
        'link' : link,
        'dead_link_count' : dead_link_count
    }
    
    return render_template('result.html', user=user)

def find_dead_links_count(link):
    return randint(0, 100)

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''