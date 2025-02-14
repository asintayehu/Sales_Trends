import pandas as pd

df = pd.read_excel('sales_data')

# Every row is a purchase; either first class, same day, second class, or standard class
# Further, every row is either consumer, corporate, or home office
# Ship Mode	| Segment | Order ID | Order Date | Sales |

first_class_consumer = []

first_class = {"Consumer":first_class_consumer}

for element in df['First Class']:
    if str(element) != "nan" and str(element) != 'Consumer':
        first_class['Consumer'].append(element)

for item in 

print(first_class)