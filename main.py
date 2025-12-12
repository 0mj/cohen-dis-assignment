import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
   
    customer_totals = {} # Create an empty dictionary to store customer totals
    
    csvfile = open(input_file, 'r') # Open and read the CSV file
    reader = csv.DictReader(csvfile)
    
    for row in reader: # Loop through each transaction row
        customer_id = int(row['customer_id'])
        amount = float(row['amount'])
        
        if customer_id not in customer_totals: # If customer doesn't exist in dictionary, add them with $0
            customer_totals[customer_id] = 0.0
        
        customer_totals[customer_id] = customer_totals[customer_id] + amount # Add this transaction amount to customer's total
    
    csvfile.close()
    print(customer_totals)
        
analyze_transactions()