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
    
    for i in range(len(customer_list)): # Sort total_spend (highest to lowest)
        for j in range(i + 1, len(customer_list)): # bubble-sort
            if customer_list[i]['total_spend'] < customer_list[j]['total_spend']:
                # Swap positions if current is less than next
                temp = customer_list[i]
                customer_list[i] = customer_list[j]
                customer_list[j] = temp
    
    top_customers = [] # Get only the top 5 customers
    count = 0
    for customer in customer_list:
        if count < 5:
            top_customers.append(customer)
            count = count + 1
    
    jsonfile = open(output_file, 'w') # Write results to JSON file
    json.dump(top_customers, jsonfile, indent=2)
    jsonfile.close()
    
    # Print results to console
    print("Analysis complete! Results written to " + output_file)
    print("")
    print("Top 5 Customers:")
    print("----------------------------------------")
    
    position = 1
    for customer in top_customers:
        cust_id = customer['customer_id']
        spend = customer['total_spend']
        print(str(position) + ". Customer " + str(cust_id) + ": $" + str(spend))
        position = position + 1
    
    return top_customers
        



if __name__ == '__main__': # script run directly (not imported)? If yes, calls the function to start the analysis
    analyze_transactions()