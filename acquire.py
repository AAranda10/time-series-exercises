#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Acquire.py Functions Using REST API that Returns JSON

import requests
import os
import numpy as np
import pandas as pd

######################################### Get Items Data ########################################

def get_items():
    # If there is no csv created, this will get the data from scratch and create one
    if os.path.isfile('items.csv') == False:
        
        url = 'https://python.zach.lol'
        api = url + '/api/v1/items'
        response = requests.get(api)
        items_data = response.json()
        df = pd.DataFrame(items_data['payload']['items'])
        
    else:
        # This will read csv if there is one created
        df = pd.read_csv('items.csv', index_col=0)
        
    return df

######################################### Get Stores Data #######################################

def get_stores():
    # If there is no csv created, this will get the data from scratch and create one
    if os.path.isfile('stores.csv') == False:
        
        url = 'https://python.zach.lol'
        api = url + '/api/v1/stores'
        response = requests.get(api)
        stores_data = response.json()
        df = pd.DataFrame(stores_data['payload']['stores'])
        
    else:
        # This will read csv if there is one created
        df = pd.read_csv('stores.csv', index_col=0)

    return df
    
######################################### Get Sales Data ########################################

def get_sales():
    # If there is no csv created, this will get the data from scratch and create one
    if os.path.isfile('sales.csv') == False:
        
        url = 'https://python.zach.lol'

        api = url + '/api/v1/'
        response = requests.get(api + 'sales')
        sales_data = response.json()
    
        # This will return the first page
        output = sales_data['payload']['sales']

        # This will loop through and do the same to all pages and merge them in one df
        while sales_data['payload']['next_page'] != None:
    
            response = requests.get(url + sales_data['payload']['next_page'])
            all_sales_data = response.json()
            output.extend(all_sales_data['payload']['sales'])
    
        df = pd.DataFrame(output)
        
    else:
        # This will read csv if there is one created
        df = pd.read_csv('sales.csv', index_col=0)
        
    return df

####################################### Get All Sales Data ########################################

def get_all_sales_data():
    # If there is no csv created, this will get the data from scratch and create one
    if os.path.isfile('complete_sales_df.csv') == False:
        
        items = get_items()
        stores = get_stores()
        sales = get_sales()
    
        # join sales and stores
        df = pd.merge(sales, stores, left_on='store', right_on='store_id').drop(columns={'store'})
    
        # join the joined df to the items
        df = pd.merge(df, items, left_on='item', right_on='item_id').drop(columns={'item'})
        
    else:
        # This will read csv if there is one created
        df = pd.read_csv('complete_sales_df.csv', index_col=0) 
        
    return df

######################################### Get Power Data ########################################

def get_power():
    # If there is no csv created, this will get the data from scratch and create one
    if os.path.isfile('power.csv') == False:
        
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        
    else:
        # This will read csv if there is one created
        df = pd.read_csv('power.csv', index_col=0)
    
    return df

