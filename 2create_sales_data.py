# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:37:56 2024

@author: Amirkhan
"""

import pandas as pd
import numpy as np

# Мәліметтерді генерациялау
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', periods=365)
products = ['Product A', 'Product B', 'Product C']
regions = ['North', 'South', 'East', 'West']
channels = ['Online', 'In-store']
age_groups = ['18-25', '26-35', '36-45', '46-60']

data = {
    'Date': np.random.choice(dates, 1000),
    'Product': np.random.choice(products, 1000),
    'Region': np.random.choice(regions, 1000),
    'Sales_Channel': np.random.choice(channels, 1000),
    'Age_Group': np.random.choice(age_groups, 1000),
    'Sales': np.random.randint(100, 1000, 1000)
}

df = pd.DataFrame(data)
df.to_csv('complex_sales_data.csv', index=False)
print("Complex sales data created and saved to 'complex_sales_data.csv'")
