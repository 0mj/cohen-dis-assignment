import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
   
    customer_totals = {} #  empty dictionary(key/val) for storing customer totals
    
    
    csvfile = open(input_file, 'r') # Open/read csv
    reader = csv.DictReader(csvfile)
    
    for row in reader: # Loop through each transaction row
        customer_id = int(row['customer_id'])
        amount = float(row['amount'])
        
        if customer_id not in customer_totals: # If id doesn't exist add with $0
            customer_totals[customer_id] = 0.0
        
        customer_totals[customer_id] = customer_totals[customer_id] + amount # Add transaction amount to customer's total
    
    csvfile.close()
    
    customer_list = [] # Convert dictionary to a LIST(ordered collection)
    for customer_id in customer_totals:
        total = customer_totals[customer_id]
        total_rounded = round(total, 2)
        
        customer_dict = {
            'customer_id': customer_id,
            'total_spend': total_rounded
        }
        customer_list.append(customer_dict)

        print(customer_list)
        
        



analyze_transactions()