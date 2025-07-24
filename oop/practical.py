class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id_number}")


class Librarian(Person):
    def __init__(self, name, id_number, employee_id):
        super().__init__(name, id_number)
        self.employee_id = employee_id

    def display_info(self):
        print(f"Librarian: {self.name}, ID: {self.id_number}, Employee ID: {self.employee_id}")


class Member(Person):
    def __init__(self, name, id_number, membership_type):
        super().__init__(name, id_number)
        self.membership_type = membership_type

    def display_info(self):
        print(f"Member: {self.name}, ID: {self.id_number}, Membership: {self.membership_type}")


class Book:
    total_borrowed = 0  # class variable

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_book(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {status}")


# Storage
books = []
members = []

# Menu
def menu():
    while True:
        print("\n📚 LIBRARY SYSTEM MENU")
        print("1. Register Member")
        print("2. Add Book")
        print("3. View Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Show Borrowed Count")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            name = input("Enter member name: ")
            id_number = input("Enter ID number: ")
            membership_type = input("Enter membership type (student/staff): ")
            member = Member(name, id_number, membership_type)
            members.append(member)
            print("✅ Member registered.")

        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            books.append(book)
            print("✅ Book added.")

        elif choice == '3':
            if not books:
                print("No books in library.")
            else:
                print("\n📖 All Books:")
                for book in books:
                    book.display_book()

        elif choice == '4':
            isbn = input("Enter ISBN of book to borrow: ")
            found = False
            for book in books:
                if book.isbn == isbn:
                    found = True
                    if book.available:
                        book.available = False
                        Book.total_borrowed += 1
                        print(f"✅ You borrowed '{book.title}'")
                    else:
                        print("❌ Book already borrowed.")
                    break
            if not found:
                print("❌ Book not found.")

        elif choice == '5':
            isbn = input("Enter ISBN of book to return: ")
            found = False
            for book in books:
                if book.isbn == isbn:
                    found = True
                    if not book.available:
                        book.available = True
                        Book.total_borrowed -= 1
                        print(f"✅ You returned '{book.title}'")
                    else:
                        print("❌ Book was not borrowed.")
                    break
            if not found:
                print("❌ Book not found.")

        elif choice == '6':
            print(f"📊 Total books currently borrowed: {Book.total_borrowed}")

        elif choice == '7':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

# Run the program
menu()
