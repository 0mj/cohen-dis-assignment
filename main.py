#   Flow Summary
#   
#   Read CSV → loop through transactions
#   Sum amounts per customer
#   Convert to list format
#   Sort by spend (highest first)
#   Slice top 5
#   Write to JSON
#   Print results




#   Loads the tools we need
#   
#   csv - reads CSV files
#   json - writes JSON files
#   defaultdict - creates a dictionary that auto-initializes missing keys to 0.0
#   itemgetter - helps sort dictionaries by a specific key
import csv
import json
from collections import defaultdict
from operator import itemgetter


#   analyze_transactions() Defines main function with default file names
#   Analyze customer transactions and identify top 5 customers by total spend.
#   Args: input_file: transactions.csv output_file: top_customers.json
#   Dictionary to store total spend per customer
#   Creates an empty dictionary to track each customer's total. 
#   defaultdict(float) means if we access a customer_id that doesn't exist yet, 
#   it starts at  0.0

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'): 
    customer_totals = defaultdict(float) 
    
    try:
        #   Example: If customer 123 has transactions of $45.67 and $89.00, customer_totals[123] becomes 134.67
        #   Read the CSV file and calculate total spend per customer Opens the CSV file
        #   DictReader reads each row as a dictionary (column names are keys)
        with open(input_file, 'r') as csvfile: 
            reader = csv.DictReader(csvfile) 
            
            for row in reader: # Loop through each transaction
                customer_id = int(row['customer_id']) # Extract customer_id and amount
                amount = float(row['amount']) 
                customer_totals[customer_id] += amount # Add the amount to that customer's running total
        
        
        #   Convert to list of dictionaries and sort by total spend (descending)
        #   Transforms the dictionary into a list of dictionaries
        #   Takes: {123: 521.22, 456: 239.10, ...}
        #   Makes: [{'customer_id': 123, 'total_spend': 521.22}, {'customer_id': 456, 'total_spend': 239.10}, ...]
        #   round(total, 2) ensures 2 decimal places for money
        customer_list = [
            {'customer_id': customer_id, 'total_spend': round(total, 2)}
            for customer_id, total in customer_totals.items()
        ]

        
        #   Sort by total_spend in descending order and get top 5
        #   sorted() - sorts the list
        #   key=itemgetter('total_spend') - sort by the 'total_spend' value
        #   reverse=True - highest first (descending order)
        #   [:5] - slice to get only the first 5 items
        top_customers = sorted(
            customer_list, 
            key=itemgetter('total_spend'), 
            reverse=True
        )[:5]
        
        #   Write results to top_customers.json
        #   Opens output file for writing
        #   json.dump() converts Python list to JSON and writes it
        #   indent=2 makes it readable with nice formatting
        with open(output_file, 'w') as jsonfile:
            json.dump(top_customers, jsonfile, indent=2)
        
        
        #   Prints success message
        #   Loops through top 5 customers with numbering (1, 2, 3...)
        #   Formats output nicely with $ and 2 decimal places
        #   Returns the list (useful if you import this function elsewhere)
        print(f"Analysis complete! Results written to {output_file}")
        print(f"\nTop 5 Customers:")
        print("-" * 40)
        for i, customer in enumerate(top_customers, 1):
            print(f"{i}. Customer {customer['customer_id']}: ${customer['total_spend']:.2f}")
        
        return top_customers

    
    #   Catches if the CSV file doesn't exist
    #   Catches any other errors (bad data, corrupted file, etc.)
    #   Prints helpful error messages instead of crashing
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None



#  if __name__ == '__main__' checks if the script is being run directly (not imported)
#  If yes, calls the function to start the analysis
if __name__ == '__main__':
    analyze_transactions()