#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from acquire import get_store_data, germany_power

#################################### Prepare Store Data Function ############################################

def prep_store_data():
    
    df = get_store_data()
    df['sale_date'] = pd.to_datetime(df.sale_date)
    df = df.set_index("sale_date").sort_index()
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

#################################### Prepare Germany Power Data Function ############################################

def prep_germany_power_data():
    df = germany_power()
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date").sort_index()
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df = df.fillna(0)
    return df
