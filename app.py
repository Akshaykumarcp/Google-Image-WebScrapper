# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:00:26 2020

@author: Akshay kumar C P
"""

from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify
import os # for reading dir here
from scrapperimage.ScrapperImage import ScrapperImage
from BusinessLayer.BusinessLayerUtil import BusinessLayer

# render_template for displaying HTML file

# import request
app = Flask(__name__) # initialising the flask app with the name'app'

# response = 'welcome'

@app.route('/') # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def fetchImages():
    list_images = os.listdir('static')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found", e)
        return "Please try with a different search keyword"

@app.route('/searchImages',methods=['Get','POST'])
def searchImage():
    if request.method=='POST':
        search_term = request.form['keyword'] # assigning the value of the input keyword to the variable keyword
    else:
        print("PLease enter something")
    
# instantiate a object for scrapperImage class    
    imagescrapperutil = BusinessLayer  # instantiated busniess layer
    imagesScrapper = ScrapperImage() # instantiated data layer
    
    # delete downloaded images before search
    list_images = os.listdir('static')
    imagesScrapper.delete_downloaded_images(list_images) # delete the old images before search

    image_name = search_term.split()
    image_name="+".join(image_name)
    
    # add header metadata
    
    header={
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
            }
    
    lst_images = imagescrapperutil.downloadImages(search_term,header)
    
    return fetchImages()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000) # port to run an local machine
    # app.run(debug=True) # to run on cloud