from library import Library

def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.borrow_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            print("Thank You for Using the Library Management System!")
            break
        else:
            print("Invalid Choice. Please Try Again.")

if __name__ == "__main__":
    main()
