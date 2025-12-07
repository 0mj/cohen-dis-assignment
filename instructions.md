# Data Intelligence Services (DIS) Technical Assessment


## Option 1:  Data Processing & Transformation

### Task:
You are given a CSV file (`transactions.csv`) with:
```
date,customer_id,amount,category
2025-01-01,123,45.67,groceries
2025-01-02,456,12.50,books
...
```
### Write a Python script that:
1.	Computes total spend per customer.
2.	Identifies the top 5 customers by total spend.
3.	Outputs a JSON file called `top_customers.json` with this structure:
```
[
  {"customer_id": 123, "total_spend": 456.78},
  ...
]
```

### Requirements:
-	Use only standard Python libraries (or `pandas` if preferred).
- Code should run via `python main.py`.
- Include a short **README** explaining how to run it.

### Deliverables:
```
•	main.py
•	top_customers.json
•	README.md
```
