# ☕ Smart Cafe Ordering System (Python)

## 📌 Project Overview

The **Smart Cafe Ordering System** is a simple Object-Oriented Programming (OOP) based Python application that simulates a cafe ordering process.
It allows customers to add items to their order, remove items, view their order, and calculate the total bill.

This project is developed as part of the **Software Construction and Development Lab** course.

---

## 🎯 Features

* Add menu items to order
* Remove items from order
* Display current order
* Calculate total bill
* Clean and modular OOP design

---

## 🧱 Project Structure

```
SmartCafe/
│── SmartCafe.py          # Main program file
│── README.md        # Project documentation
```

---

## 🧑‍💻 Technologies Used

* Python 3.x
* Object-Oriented Programming (OOP)

---

## 📚 Classes Description

### 🔹 MenuItem

Represents a single item in the cafe menu.

**Attributes:**

* `name` – Name of item
* `price` – Price of item

**Methods:**

* `display()` – Show item details
* `get_price()` – Return item price
* `get_name()` – Return item name

---

### 🔹 Order

Manages a list of menu items.

**Methods:**

* `add_item(item)` – Add item to order
* `remove_item(name)` – Remove item by name
* `display_order()` – Display all items
* `calculate_total()` – Calculate total bill

---

### 🔹 Customer

Represents a customer placing an order.

**Attributes:**

* `name` – Customer name
* `order` – Customer's order

**Methods:**

* `add_order_item(item)`
* `remove_order_item(name)`
* `display_order()`
* `checkout()`

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/Ali-Ashor/SmartCafe.git
cd SmartCafe
```

### 2. Run Program

```
python SmartCafe.py
```

---

## 💻 Example Output

```
Order for Ali:
Coffee - $3.5
Sandwich - $5.0
Burger - $7.0

After removing Sandwich:
Order for Ali:
Coffee - $3.5
Burger - $7.0

Total: $10.5
```

---

## 🔄 Future Improvements

* Add graphical user interface (GUI)
* Store orders in files or database
* Add multiple customers support
* Implement staff/admin panel

---

## 🧪 Learning Outcomes

* Understanding of OOP concepts (Encapsulation, Modularity)
* Working with classes and objects in Python
* Managing collections (lists)
* Writing clean and maintainable code

---

## 📸 Screenshots

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d448c414-55cd-41a1-92ba-5c8bc9c9d4a8" />


---

## 👨‍🎓 Author

**Shujaat Ali**
BS Software Engineering – Semester 5

---

## 📄 License

This project is for educational purposes only.
