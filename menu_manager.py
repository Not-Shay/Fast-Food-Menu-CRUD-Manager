import sqlite3

def initialize_database():

    conn = sqlite3.connect('fastfood.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             price REAL NOT NULL,
             category TEXT
             )
    ''')

    conn.commit()
    conn.close()

def add_item(name, price, category):
    conn = sqlite3.connect('fastfood.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO menu (name, price, category) VALUES (?, ?, ?)', (name, price, category))

    conn.commit()
    conn.close()
    print(f"Success: '{name}' added to the menu.")

def view_menu():

    conn = sqlite3.connect('fastfood.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM menu ORDER BY category, name')
    items = cursor.fetchall()

    print("\n--- CURRENT MENU ---")
    print(f"{'ID':<5} {'NAME':<20} {'PRICE':<10} {'CATEGORY'}")
    print("-" * 50)

    for item in items:
        print(f"{item[0]:<5} {item[1]:<20} ₹{item[2]:<10} {item[3]}")
    
    conn.close()

def update_price(item_id, new_price):

    conn = sqlite3.connect('fastfood.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE menu SET price = ? WHERE id = ?', (new_price, item_id))

    if cursor.rowcount == 0:
        print("Error: Item ID not found.")
    
    else:
        conn.commit()
        print("Success: Price updated.")
    
    conn.close()

def delete_item(item_id):

    conn = sqlite3.connect('fastfood.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM menu WHERE id = ?', (item_id,))

    if cursor.rowcount == 0:
        print("Error: Item ID not found.")
    
    else:
        conn.commit()
        print("Success: Item deleted.")
    
    conn.close()

if __name__ == "__main__":
    initialize_database()
    
    while True:
        print("\n=== MENU MANAGER ===")
        print("1. Add New Item")
        print("2. View Menu")
        print("3. Update Price")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            name = input("Item Name: ")
            category = input("Category: ")
            
            try:
                price = float(input("Price: "))
                add_item(name, price, category)
            except ValueError:
                print("ERROR: Price must be a number")

        elif choice == '2':
            view_menu()

        elif choice == '3':
            view_menu()

            try:
                item_id = int(input("Enter ID to update: "))
                new_price = float(input("Enter new price: "))
                update_price(item_id, new_price)
            except ValueError:
                print("ERROR: Please enter valid numbers for ID and Price.")

        elif choice == '4':
            view_menu()

            try:
                item_id = int(input("Enter ID to delete: "))
                delete_item(item_id)
            except ValueError:
                print("ERROR: ID must be a whole number.")

        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice.")