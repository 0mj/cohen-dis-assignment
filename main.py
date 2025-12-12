import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
   
    # Create an empty dictionary to store customer totals
    customer_totals = {}
    
    # Open and read the CSV file
    csvfile = open(input_file, 'r')
    reader = csv.DictReader(csvfile)
    
    # Loop through each transaction row
    for row in reader:
        customer_id = int(row['customer_id'])
        amount = float(row['amount'])
        
        # If customer doesn't exist in dictionary, add them with $0
        if customer_id not in customer_totals:
            customer_totals[customer_id] = 0.0
        
        # Add this transaction amount to customer's total
        customer_totals[customer_id] = customer_totals[customer_id] + amount
    
    csvfile.close()
    print(customer_totals)
        
analyze_transactions()