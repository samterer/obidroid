#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Crawler
=========
Give an APP-CATEGORY, it should try crawling the app store for similar
applications in the category and compile the links of the applications
into a text file, that can then be used in the Scraper.py script for
extracting the requisite features.

app-games.txt
-------------
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
"""
from __future__ import division
from optparse import OptionParser
from lxml import html
# from time import strftime
# today=strftime("%Y-%m-%d") #today's date

def getAppCategory():
    optionparser = OptionParser()

    optionparser.add_option('-c', '--category', dest='appCategory')

    (option, args) = optionparser.parse_args()

    if not option.appCategory:
        return optionparser.error('Application Category not provided.\n Usage: --url="path.to.appurl"')

    return { 'cat' : option.appCategory }


def get_ids_from_html(html_file_name):
    '''
    open the html from disk, 
    parse with lxml.html, 
    use xpath to get list of app IDs, 
    save
    '''
    #intialize local variables
    ids=[]
    html_file=open(html_file_name)

    #use lxml to parse html
    doc = html.parse(html_file).getroot()
    html_file.close()

    #xpath makes a list of all the hrefs in elements of class "card-content-link"
    ids=doc.xpath('//*[@class="card-content-link"]/@href')
    
    ## print ids
    ## print str(len(ids))

    #Save it
    id_file_name=html_file_name+"_ids.txt"
    save_ids_to_txt(ids,id_file_name)
    print "IDs from "+html_file_name + " were extracted into "+id_file_name


def save_ids_to_txt(ids,filename="ids.txt"):
    f=open(filename,"w")
    for i in ids:
        f.write(i+"\n")
    f.close()




def main():
    # print __doc__

    appCat = getAppCategory()

    print appCat

    get_ids_from_html('input.html')


if __name__ == '__main__':
    main()
