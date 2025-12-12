import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
    customer_totals = {}
    
    
    csvfile = open(input_file, 'r')
    reader = csv.DictReader(csvfile)
    
    # Step 3: Loop through each transaction row and print
    for row in reader:
        print(row)
    
    csvfile.close()
    
        
analyze_transactions()