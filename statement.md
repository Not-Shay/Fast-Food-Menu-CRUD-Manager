# Project Statement

## 1. Problem Statement
Managing a fast food menu in today's day and age manually is quite a tedious task. Times like these call for an advanced CRUD management system to maintain a database record.

## 2. Scope of the Project
The scope of this project is to develop a **Command Line Interface (CLI)** application that serves as a backend management tool for restaurant data.
* **In Scope:**
    * Developing a persistent database using SQLite.
    * Implementing full CRUD (Create, Read, Update, Delete) operations.
    * Input validation to prevent system crashes.
    * Data sorting and categorization logic.
* **Out of Scope:**
    * Customer-facing graphical user interface (GUI) or website.
    * Payment processing or order tracking.
    * Multi-user authentication (login system).

## 3. Target Users
This tool is designed for **Back-Office Employees** and **Restaurant Managers**, not for customers.
* **Restaurant Managers:** To add new seasonal items or remove discontinued ones.
* **Administrative Staff:** To perform daily price adjustments and audit the current menu list.

## 4. High-Level Features
* **Persistent Data Storage:** Uses `sqlite3` to ensure data remains saved even after the application closes.
* **Dynamic Menu Management:** Allows users to add, update, and delete menu items in real-time.
* **Automated Sorting:** The "View" function automatically organizes items by Category and Name using SQL queries.
* **Crash-Proof Interface:** Includes robust error handling (`try...except`) to manage invalid data entry (e.g., entering text instead of numeric prices) without terminating the program.
* **Formatted Output:** Displays database records in a clean, and formatted way.
