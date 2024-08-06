# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:40:26 2024

@author: Amirkhan
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Мәліметтерді оқу
df = pd.read_csv('complex_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Күн бойынша орташа сатылымдарды есептеу
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Уақыттық ерекшеліктерді қосу
daily_sales['Day'] = daily_sales['Date'].dt.day
daily_sales['Month'] = daily_sales['Date'].dt.month
daily_sales['Year'] = daily_sales['Date'].dt.year

# Мәліметтерді бөлу
X = daily_sales[['Day', 'Month', 'Year']]
y = daily_sales['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Модельді құру
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Болжау жасау
y_pred = model.predict(X_test)

# Нәтижелерді бағалау
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Нәтижелерді визуализациялау
plt.figure(figsize=(10, 5))
plt.plot(daily_sales['Date'], daily_sales['Sales'], label='Actual Sales')
plt.plot(daily_sales['Date'].iloc[-len(y_test):], y_pred, label='Predicted Sales')
plt.legend()
plt.title('Actual vs Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.savefig('sales_forecast.png')
plt.show()
