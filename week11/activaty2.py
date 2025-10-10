from db import create_table
from cost_manager import add_cost, view_costs, calculate_total_cost

def menu():
    print("\n==== Cost Manager ====")
    print("1. Add Cost")
    print("2. View All Costs")
    print("3. Calculate Total Cost")
    print("4. Exit")


def main():
    create_table()

    while True:
        menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_cost(amount, description)
        elif choice == '2':
            costs = view_costs()
            for cost in costs:
                print(cost)
        elif choice == '3':
            total = calculate_total_cost()
            print(f"Total Cost: {total}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()