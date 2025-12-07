import csv
import json
from collections import defaultdict
from operator import itemgetter

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
    
    customer_totals = defaultdict(float)
    
    try:
    
        with open(input_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                customer_id = int(row['customer_id'])
                amount = float(row['amount'])
                customer_totals[customer_id] += amount
        
    
        customer_list = [
            {'customer_id': customer_id, 'total_spend': round(total, 2)}
            for customer_id, total in customer_totals.items()
        ]
        
    
        top_customers = sorted(
            customer_list, 
            key=itemgetter('total_spend'), 
            reverse=True
        )[:5]
        
    
        with open(output_file, 'w') as jsonfile:
            json.dump(top_customers, jsonfile, indent=2)
        
        print(f"Analysis complete! Results written to {output_file}")
        print(f"\nTop 5 Customers:")
        print("-" * 40)
        for i, customer in enumerate(top_customers, 1):
            print(f"{i}. Customer {customer['customer_id']}: ${customer['total_spend']:.2f}")
        
        return top_customers
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None

if __name__ == '__main__':
    analyze_transactions()