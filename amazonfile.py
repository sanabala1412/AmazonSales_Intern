import pandas as pd 
import matplotlib.pyplot as plt
file_path = r'D:\\Amazon Sale Report.csv'       #load dataset
data = pd.read_csv(file_path)
print(data.head())

data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y', errors='coerce')
data = data.dropna(subset=['Date'])
sales_over_time = data.groupby('Date')['Amount'].sum()  #sales overview
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time.index, sales_over_time.values)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales (INR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

category_distribution = data['Category'].value_counts()
plt.figure(figsize=(12, 6))
category_distribution.plot(kind='bar')
plt.title('Distribution of Product Categories')  #product analysis
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fulfillment_distribution = data['Fulfilment'].value_counts()
plt.figure(figsize=(12, 6))
fulfillment_distribution.plot(kind='bar') #Fullfilment analysis
plt.title('Distribution of Fulfillment Methods')
plt.xlabel('Fulfillment Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

city_distribution = data['ship-city'].value_counts().head(10)
plt.figure(figsize=(12, 6))
city_distribution.plot(kind='bar')
plt.title('Top 10 Cities by Sales')  #customer segmentation
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

state_distribution = data['ship-state'].value_counts()
plt.figure(figsize=(12, 6))
state_distribution.plot(kind='bar')  #Geographical analysis
plt.title('Distribution of Sales by State')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
