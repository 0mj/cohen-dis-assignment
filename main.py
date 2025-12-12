import csv
import json

def analyze_transactions(input_file='transactions.csv', output_file='top_customers.json'):
   
    # Create an empty dictionary to store customer totals
    customer_totals = {}
    
    try:
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
        
        # Convert dictionary to a list of dictionaries
        customer_list = []
        for customer_id in customer_totals:
            total = customer_totals[customer_id]
            total_rounded = round(total, 2)
            
            customer_dict = {
                'customer_id': customer_id,
                'total_spend': total_rounded
            }
            customer_list.append(customer_dict)
        
        # Sort the list by total_spend (highest to lowest)
        # We'll use a simple bubble-sort approach that's easier to understand
        for i in range(len(customer_list)):
            for j in range(i + 1, len(customer_list)):
                if customer_list[i]['total_spend'] < customer_list[j]['total_spend']:
                    # Swap positions if current is less than next
                    temp = customer_list[i]
                    customer_list[i] = customer_list[j]
                    customer_list[j] = temp
        
        # Get only the top 5 customers
        top_customers = []
        count = 0
        for customer in customer_list:
            if count < 5:
                top_customers.append(customer)
                count = count + 1
        
        # Write results to JSON file
        jsonfile = open(output_file, 'w')
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
        
    except FileNotFoundError:
        print("Error: " + input_file + " not found.")
        return None
    except Exception as e:
        print("Error processing file: " + str(e))
        return None

# Run the script
if __name__ == '__main__':
    analyze_transactions()