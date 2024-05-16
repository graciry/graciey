# Step 1: Print Statement
def print_welcome_message():
    print("Welcome to Personal Finance Tracker")
    print("Please follow the instructions to manage your finances.")

# Step 2: Variables
income = 0.0
expenses = 0.0
savings = 0.0
transactions = []

# Step 3: Data Types
# No specific implementation needed here as Python dynamically infers data types

# Step 4: Input and Output
def get_user_input():
    return input("Enter your transaction: ")

def display_financial_summary():
    print(f"Income: ${income}")
    print(f"Expenses: ${expenses}")
    print(f"Savings: ${savings}")

# Step 5: Functions
def add_income(amount):
    global income
    income += amount

def add_expense(amount):
    global expenses
    expenses += amount

def calculate_savings():
    global savings
    savings = income - expenses

# Step 6: Conditional Statements
def handle_user_choice(choice):
    if choice == '1':
        transaction = get_user_input()
        transactions.append(transaction)
        add_income(float(transaction))
    elif choice == '2':
        transaction = get_user_input()
        transactions.append(transaction)
        add_expense(float(transaction))
    elif choice == '3':
        calculate_savings()
        display_financial_summary()
    elif choice == '4':
        print("Thank you for using Personal Finance Tracker.")
        exit()
    else:
        print("Invalid choice. Please try again.")

# Step 7: File Handling
# Functions to read and write transaction data to/from a file can be implemented here

# Step 8: Categories and Reports
# Functions to categorize expenses and generate reports can be implemented here

# Step 9: Data Visualization (Optional)
# Matplotlib or Plotly can be used for data visualization

# Step 10: Error Handling and Validation
# Add error handling and validation mechanisms as needed

# Step 11: Test and Refine
# Test the functions and refine the code based on testing results and user feedback

# Step 12: Conclusion
def print_closing_message():
    print("Thank you for using Personal Finance Tracker.")

# Main function
def main():
    print_welcome_message()
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Financial Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")
        handle_user_choice(choice)

if __name__ == "__main__":
    main()
