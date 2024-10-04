import pandas as pd
import matplotlib.pyplot as plt

# Load the csv file
book_data = pd.read_csv('Initial_Data.csv')

# Finding missing emails
customers_with_missing_emails = book_data.loc[(book_data['Email'].isna())]
print(customers_with_missing_emails['Name'])

# Finding missing phones
customers_with_missing_phones = book_data.loc[(book_data['PhoneNumber'].isna())]
print(customers_with_missing_phones)

# Purchased amount per month in a graph
    # datetime format
book_data['PurchaseDate'] = pd.to_datetime(book_data['PurchaseDate'], errors = 'coerce')

# Group by 'month' and calculate the total sales for each month
book_data['month'] = book_data['PurchaseDate'].dt.strftime('%B')

monthly_sales = book_data.groupby('month')['PurchaseAmount'].sum().reindex(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
).reset_index()

# Display the monthly sales
print("Sales for each month:")
print(monthly_sales)

# Plot the monthly sales using a bar graph
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['month'].astype(str), monthly_sales['PurchaseAmount'], color='blue')

# Set chart title and labels
plt.title('Total Sales Per Month', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45)  # Rotate month labels for better readability

# Show the plot
plt.tight_layout()  # Adjusts the layout so everything fits without overlap
plt.show()



