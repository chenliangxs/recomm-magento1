# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:49:33 2019

@author: Silk
"""

import db_info
import pymysql
import numpy as np

class Data():
    def __init__(self):
        myhost = db_info.config['host']
        myuser = db_info.config['user']
        mypassword = db_info.config['password']
        mydb = db_info.config['database']
        myport = db_info.config['port']
        db = pymysql.connect(host=myhost,user=myuser,password=mypassword,db=mydb,port=myport)

        self.cursor = db.cursor()
        self.product_map = self.getProductMapping()
        self.customer_map = self.getCustomerMapping()
        self.category_map = self.getCategoryMapping()
        
    def getProductMapping(self):
        product_map = {}
        productMapQuery = "SELECT * FROM rec_product_index_mapping"
        self.cursor.execute(productMapQuery)
        productMapResults = self.cursor.fetchall()
        for row in productMapResults:
            index = row[0]
            product_id = row[1]
            product_map[product_id] = index
            #print(product_map[product_id])
        return product_map
        
    def getCustomerMapping(self):
        customer_map = {}
        customerMapQuery = "SELECT * FROM rec_customer_index_mapping"
        self.cursor.execute(customerMapQuery)
        customerMapResults = self.cursor.fetchall()
        for row in customerMapResults:
            index= row[0]
            customer_id = row[1]
            customer_map[customer_id] = index
            #print(customer_map[customer_id])
        return customer_map

    def getCategoryMapping(self):
        category_map = {}
        categoryMapQuery = "SELECT * FROM rec_category_index_mapping"
        self.cursor.execute(categoryMapQuery)
        categoryMapResults = self.cursor.fetchall()
        for row in categoryMapResults:
            index= row[0]
            category_id = row[1]
            category_map[category_id] = index
            #print(customer_map[customer_id])
        return category_map
        
    #prepage training data from user_product_count table
    def getOrderData(self):
        trainX = np.zeros([len(self.product_map), len(self.customer_map)])
        trainR = np.zeros([len(self.product_map), len(self.customer_map)])
        getCountQuery = "SELECT * FROM rec_user_product_count"
        self.cursor.execute(getCountQuery)
        results = self.cursor.fetchall()
        for row in results:
            customer = row[1]
            product = row[2]
            count = row[3]
            trainX[self.product_map[product] - 1][self.customer_map[customer] - 1] = count
            if count > 0:
                trainR[self.product_map[product] - 1][self.customer_map[customer] - 1] = 1
        print("trainning matrix load ready")
        #normalize based on single customer to a 0-10 scale
        #base = np.amax(trainX, axis=0)
        trainX = np.where(np.max(trainX, axis=0)==0, trainX, trainX*10./np.max(trainX, axis=0))
        #print(base)
        return trainX, trainR
    
    #get viewed products by customer from table report_viewed_product_index
    def getViewedData(self):
        viewed = np.zeros([len(self.product_map), len(self.customer_map)])
        getViewedQuery = """SELECT a.customer_id, a.product_id FROM
                        report_viewed_product_index AS a 
                        INNER JOIN rec_product_index_mapping AS p ON a.product_id=p.product_id
                        INNER JOIN rec_customer_index_mapping AS c ON a.customer_id=c.customer_id"""
        self.cursor.execute(getViewedQuery)
        results = self.cursor.fetchall()
        for row in results:
            customer = row[0]
            product = row[1]
            viewed[self.product_map[product] - 1][self.customer_map[customer] - 1] = 1
        return viewed
    
    #prepage feature data from procat table
    def getFeatureData(self):
        trainTheta = np.zeros([len(self.product_map), len(self.category_map)])
        getProCatQuery = "SELECT * FROM rec_product_category"
        self.cursor.execute(getProCatQuery)
        results = self.cursor.fetchall()
        for row in results:
            product = row[1]
            category = row[2]
            trainTheta[self.product_map[product] - 1][self.category_map[category] - 1] = 1
        print("feature matrix load ready")
        return trainTheta
            
        
            
        
