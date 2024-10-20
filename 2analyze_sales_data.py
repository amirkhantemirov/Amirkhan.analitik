# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:39:15 2024

@author: Amirkhan
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('complex_sales_data.csv')


total_sales = df.groupby('Product')['Sales'].sum()


average_sales_by_region = df.groupby('Region')['Sales'].mean()


df['Date'] = pd.to_datetime(df['Date'])
sales_trend = df.groupby('Date')['Sales'].sum()
sales_by_age_group = df.groupby('Age_Group')['Sales'].sum()
sales_by_channel = df.groupby('Sales_Channel')['Sales'].sum()


plt.figure(figsize=(14, 10))
plt.subplot(3, 2, 1)
total_sales.plot(kind='bar', title='Total Sales by Product')
plt.ylabel('Total Sales')

plt.subplot(3, 2, 2)
average_sales_by_region.plot(kind='bar', title='Average Sales by Region', color='green')
plt.ylabel('Average Sales')

plt.subplot(3, 2, 3)
sales_trend.plot(title='Sales Trend Over Time')
plt.ylabel('Sales')
plt.xlabel('Date')

plt.subplot(3, 2, 4)
sales_by_age_group.plot(kind='bar', title='Sales by Age Group', color='purple')
plt.ylabel('Total Sales')

plt.subplot(3, 2, 5)
sales_by_channel.plot(kind='bar', title='Sales by Channel', color='orange')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.savefig('sales_analysis.png')
plt.show()
