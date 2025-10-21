# cohen-DIS-assignment
# DIS Technical Assessment
Thank you for interviewing with us!
As part of our process, we’d like you to complete a short technical assessment.
We’re giving you two assignment options below. You may choose to complete either one (whichever best showcases your skills) or both.  
 We expect this assignment to take about 2–3 hours, but please don’t feel pressure to over-engineer — we’re more interested in seeing your approach, clarity, and coding style than a perfect production-ready system. Do not be overly concerned with style and design of the application. Just make sure it clearly displays the functionality it is supporting and meets the requirements outlined below. Likewise, if you run into challenges either completing the application or with particular aspects, it’s ok. We would still like to see what you accomplished and talk through things with you.
________________________________________
## Option 1: 
## Data Processing & Transformation

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

________________________________________
## Option 2: 
## API Integration (Structured)

### Task:
Write a Python script that:
1.	Fetches repository data from the **GitHub public API** for a given user (e.g., `octocat`).
     - > Endpoint: `https://api.github.com/users/octocat/repos`
2.	Stores `repo name`, `stars`, and `last updated date` in a local **SQLite database** (`repos.db').
3.	Queries the database to find the repo with the most stars.

### Requirements:

-	Use `requests` and `sqlite3` (no other dependencies).
-	Include basic error handling for HTTP and DB operations.
-	The script should print:
    - `Most starred repo: <name> with <stars> stars.`
-	Include a short **README** explaining how to run it.

### Deliverables:
```
•	main.py
•	repos.db (optional if generated on run)
•	README.md
```

________________________________________
## Submission Instructions

Candidates can choose one of the two exercises ***or*** complete both but should be prepared to talk about both assignments in the follow-up assessment.

Please submit your code and deliverables as a zipped folder or GitHub repository link (**preferred**), including your `README.md`.
Please [email your folder or repository link](mailto:jsilverman@cohenco.com%3Bmduleba@cohenco.com?cc=cgamble@cohenco.com%3Bayarnot@cohenco.com%3Bjgraham@cohenco.com%3Bkmalloy@cohenco.com&Subject=DIS%20Technical%20Assessment).  Please complete as soon as possible so we can proceed with your interview process ideally within a week (if you need more time please reach out and let us know).

You do ***not*** need to implement a user interface, API endpoint, or Docker container — a simple script is perfect.

