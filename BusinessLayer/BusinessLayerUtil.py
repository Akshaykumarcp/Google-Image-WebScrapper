# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:53:29 2020

@author: Akshay kumar C P
"""

from scrapperimage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    # class variables
    keyword=""
    fileLoc=""
    image_name=""
    header=""
    
    def downloadImages(keyword,header):
        imgScrapper  = ScrapperImage
        url = imgScrapper.createImageURL(keyword)
        rawHtml = imgScrapper.scrap_html_data(url,header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyword,header)
        
        return masterListOfImages