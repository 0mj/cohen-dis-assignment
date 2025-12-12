import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
    
    csvfile = open(input_file, 'r')
    print(csvfile)
        
analyze_transactions()