import pandas as pd
import random
from datetime import datetime, timedelta

# डेटा पैरामीटर्स  
num_rows = 1000
categories = ["Electronics", "Fashion", "Home & Kitchen", "Sports", "Books"]
products = {
    "Electronics": ["Wireless Mouse", "Smartwatch", "Bluetooth Headphones", "Laptop Cooling Pad"],
    "Fashion": ["Running Shoes", "Denim Jacket", "Sunglasses", "Leather Wallet"],
    "Home & Kitchen": ["Air Fryer", "Vacuum Cleaner", "Pressure Cooker", "Water Purifier"],
    "Sports": ["Football", "Badminton Racket", "Dumbbells", "Yoga Mat"],
    "Books": ["Self-Help Guide", "Science Fiction", "Business Strategies", "History of India"]
}
return_reasons = ["Defective", "Wrong Size", "Late Delivery", "Wrong Product", "Other"]
regions = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"]
customer_types = ["New", "Returning"]

# प्रोडक्ट के फिक्स्ड प्राइस  
product_prices = {
    "Wireless Mouse": 599, "Smartwatch": 2999, "Bluetooth Headphones": 1999, "Laptop Cooling Pad": 1299,
    "Running Shoes": 1499, "Denim Jacket": 1999, "Sunglasses": 999, "Leather Wallet": 899,
    "Air Fryer": 4999, "Vacuum Cleaner": 3999, "Pressure Cooker": 2499, "Water Purifier": 5999,
    "Football": 799, "Badminton Racket": 1299, "Dumbbells": 2999, "Yoga Mat": 599,
    "Self-Help Guide": 499, "Science Fiction": 699, "Business Strategies": 899, "History of India": 999
}

# डेटा जनरेशन  
data = []
start_date = datetime(2024, 1, 1)
for i in range(1, num_rows + 1):
    order_id = 1000 + i
    customer_id = f"C{random.randint(1000, 9999)}"
    category = random.choice(categories)
    product_name = random.choice(products[category])
    order_date = start_date + timedelta(days=random.randint(0, 30))
    return_date = order_date + timedelta(days=random.randint(5, 15))
    return_reason = random.choice(return_reasons)
    refund_amount = product_prices[product_name]  # प्रोडक्ट के अनुसार फिक्स्ड रिफंड अमाउंट
    processing_time = random.randint(3, 10)
    customer_type = random.choice(customer_types)
    region = random.choice(regions)

    data.append([order_id, customer_id, product_name, category, order_date.strftime("%Y-%m-%d"),
                 return_date.strftime("%Y-%m-%d"), return_reason, refund_amount,
                 processing_time, customer_type, region])

# DataFrame बनाना  
df = pd.DataFrame(data, columns=[
    "Order ID", "Customer ID", "Product Name", "Category", "Order Date", "Return Date",
    "Return Reason", "Refund Amount", "Processing Time (Days)", "Customer Type", "Region"
])

# CSV फाइल सेव करना  
df.to_csv("returns_refunds_1000.csv", index=False)
print("CSV फाइल 'returns_refunds_1000.csv' सफलतापूर्वक बनाई गई!")
