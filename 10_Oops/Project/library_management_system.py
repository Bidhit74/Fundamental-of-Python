# Library Management System
# 🔹 Features: Show available books, Borrow a book, Return a book

class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("\n📚 Available Books:")
        for book in self.books:
            print(f"✔ {book}")
        if not self.books:
            print("❌ No books available.")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"✅ You borrowed: '{book_name}'")
        else:
            print("❌ Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You returned '{book_name}'")


# --- Starting Books in Library ---
book_list = ["Python", "Java", "C++", "HTML", "Machine Learning"]
lib = Library(book_list)

# --- Menu Loop ---
print("📘 Welcome to the Bidhit Library System!")

while True:
    print("\n📋 Menu:")
    print("1. Show Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        lib.display_books()

    elif choice == "2":
        book_name = input("Enter book name to borrow: ")
        lib.borrow_book(book_name)

    elif choice == "3":
        book_name = input("Enter book name to return: ")
        lib.return_book(book_name)

    elif choice == "4":
        print("📚 Thank you for visiting the Bidhit Library. Goodbye! 👋")
        break

    else:
        print("❌ Invalid option. Please try again.")


# ✅ OOPs Used:
# Class/Object – Library
# Encapsulation – List of books is protected
# Polymorphism possible – Extend borrow_book() with student type etc.
