#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Sat Sep 21 22:06:10 2019



@author: margaritaprokhodko

"""



import time # time for date time

import requests # get 

import json # Json is web page

import pandas as pd #Panda library for big data

import logging 

import csv

import os

import glob

import mysql.connector



LOG_FILENAME = "ESGLoader.log"


# create logger

logger = logging.getLogger(LOG_FILENAME)

logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages

fh = logging.FileHandler(LOG_FILENAME)

fh.setLevel(logging.DEBUG)

# create console handler with a higher log level

ch = logging.StreamHandler()

ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

fh.setFormatter(formatter)

# add the handlers to logger

logger.addHandler(ch)

logger.addHandler(fh)







def WriteDictToCSV(csv_file,csv_columns,dict_data,header_true):

    try:

        with open(csv_file, 'a') as csvfile:

             if (header_true):  csvfile.writerow(csv_columns)

        csvfile.writerow(dict_data.values())
          

    except IOError :

            print("I/O error({0}): {1}".format(errno, strerror))    

    return     





def saveContents(ticker, output_filename):

    url = "https://finance.yahoo.com/quote/{}/sustainability?p={}".format(ticker, ticker)
    

    print(url)
    
    myfile = requests.get(url)


    if (myfile.status_code==200):

       logger.debug(ticker)

       logger.debug((myfile))

    contents = str(myfile.content)

    # open(output_filename, 'wb').write(myfile.content)

    return contents



def saveJson(s, output_filename):

    d = json.loads(s)

   # print(json.dumps(d, indent=4, sort_keys=True))

   # with open(output_filename, 'w') as outfile:
 
   #   json.dump(d, outfile)

    return



def cleanFileList(fileList) :

    for filePath in fileList:

        try:

              os.remove(filePath)

        except:

            print("Error while deleting file : ", filePath)

    return    

db = mysql.connector.connect(
  host="localhost",
  user="esgindex_viacheslav",
  password="cp4^oRaI7DA1",
  db="esgindex_db1"
)

cursor = db.cursor()


# cursor.execute("Delete From result")
# db.commit()

cursor.execute("Select SecId, Symbol From securitymaster Limit 99999")

for row in cursor.fetchall():
    secId = row[0]
    ticker = row[1]
    

    try :
        timestr = time.strftime("%Y%m%d-%H%M%S")
        output_filename = ticker+'_'+timestr+'.html'

        contents = saveContents(ticker, output_filename)#save the original html page to a file and return contents str
    
        #ESG scores for the ticker and peers

        esgScores_json_str = '{'+contents[contents.find('"esgScores'):contents.find(',"FinanceConfigStore')]

    
        output_filename = ticker + '_esgScores_' + timestr + '.json'

        saveJson(esgScores_json_str, output_filename)#save json to a file


        #times series of historical ESG data for the ticker and peers

        esgHistorical_json_str = '{'+contents[contents.find('"ESGStore'):contents.find(',"peerScores":{},"peerScoresSymbol"')]+'}}'

        #output_filename = 'esg/'+ticker+'_esgHistorical_'+timestr+'.json'
        
        #saveJson(esgHistorical_json_str, output_filename)#save json to a file

        esg1=json.loads(esgScores_json_str)
        

        str_ESGScoresSocial=str(esg1['esgScores']['socialScore']['raw'])

        str_ESGScores_Environmental=str(esg1['esgScores']['environmentScore']['raw'])
        
        str_ESGScores_Governance=str(esg1['esgScores']['governanceScore']['raw'])

        str_ESGScores_Total = str(esg1['esgScores']['socialScore']['raw'] + esg1['esgScores']['environmentScore']['raw'] + esg1['esgScores']['governanceScore']['raw'])
        
        
        # boolean values
        str_Alcoholic_Beverages = "1" if esg1['esgScores']['alcoholic'] == True else "0"
        
        str_Adult_Entertainment = "1" if esg1['esgScores']['adult'] == True else "0"
        
        str_Gambling = "1" if esg1['esgScores']['gambling'] == True else "0"
        
        str_Tobacco_Products = "1" if esg1['esgScores']['tobacco'] == True else "0"
        
        str_Animal_Testing = "1" if esg1['esgScores']['animalTesting'] == True else "0"
        
        str_Fur_and_Specialty_Leather = "1" if esg1['esgScores']['furLeather'] == True else "0"
        
        str_Controversial_Weapons = "1" if esg1['esgScores']['furLeather'] == True else "0"
        
        str_Small_Arms = "1" if esg1['esgScores']['smallArms'] == True else "0"
        
        str_Catholic_Values = "1" if esg1['esgScores']['catholic'] == True else "0"
        
        str_GMO = "1" if esg1['esgScores']['gmo'] == True else "0"
        
        str_Military_Contracting = "1" if esg1['esgScores']['militaryContract'] == True else "0"
        
        str_Pesticides = "1" if esg1['esgScores']['pesticides'] == True else "0"
        
        str_Thermal_Coal = "1" if esg1['esgScores']['coal'] == True else "0"
        
        str_Palm_Oil = "1" if esg1['esgScores']['palmOil'] == True else "0"
        
        str_AsOfDate = time.strftime("%Y-%m-%d %H:%M:%S")
        
        query = "Insert into ESGScore (Secid, AsOfDate, Symbol, ESGScoresSocial, ESGScores_Environmental, ESGScores_Governance, ESGScores_Total, Alcoholic_Beverages, Adult_Entertainment, Gambling, Tobacco_Products, Animal_Testing, Fur_and_Specialty_Leather, Controversial_Weapons, Small_Arms, Catholic_Values, GMO, Military_Contracting, Pesticides, Thermal_Coal, Palm_Oil)"

        query = query + " Values('" + str(secId) + "', '" + str_AsOfDate + "', '','" + str_ESGScoresSocial + "','" + str_ESGScores_Environmental + "','" + str_ESGScores_Governance + "','" + str_ESGScores_Total + "', " + str_Alcoholic_Beverages + "," + str_Adult_Entertainment + "," + str_Gambling + "," + str_Tobacco_Products + "," + str_Animal_Testing + "," + str_Fur_and_Specialty_Leather + "," + \
str_Controversial_Weapons + "," + str_Small_Arms + "," + str_Catholic_Values + "," + str_GMO + "," + str_Military_Contracting + "," + str_Pesticides + "," + str_Thermal_Coal + "," + str_Palm_Oil + ")"

        # print(query)                        
        
        
        try:
            cursor.execute(query)
            db.commit()
        except MySQLdb.Error as err:
            print(err)
        
        
    

        fileList = glob.glob('*.html')

        cleanFileList(fileList)

        fileList = glob.glob('*.json')

        cleanFileList(fileList)
        
    except Exception as e:   
        print("error")
        logger.debug(e.__doc__)
        print(output_filename)
        print(e)

cursor.close()
db.close()