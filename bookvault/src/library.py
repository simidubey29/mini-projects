from storage import load_books, save_books
from book import Book


class Library:

    def add_book(self):
        books = load_books()

        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")

        new_book = Book(book_id, title, author)

        books.append(new_book.to_dict())

        save_books(books)

        print("Book Added Successfully!")

    def view_books(self):
        books = load_books()

        if not books:
            print("No Books Available")
            return

        print("\n========== BOOK LIST ==========")

        for book in books:
            status = "Available" if book["available"] else "Borrowed"

            print(
                f"\nID: {book['book_id']}"
                f"\nTitle: {book['title']}"
                f"\nAuthor: {book['author']}"
                f"\nStatus: {status}"
            )

    def search_book(self):
        books = load_books()

        keyword = input("Enter Book Title: ").lower()

        found = False

        for book in books:
            if keyword in book["title"].lower():
                print("\nBook Found")
                print(book)
                found = True

        if not found:
            print("Book Not Found")

    def borrow_book(self):
        books = load_books()

        book_id = input("Enter Book ID: ")

        for book in books:
            if book["book_id"] == book_id:

                if book["available"]:
                    book["available"] = False
                    save_books(books)

                    print("Book Borrowed Successfully")

                else:
                    print("Book Already Borrowed")

                return

        print("Book Not Found")

    def return_book(self):
        books = load_books()

        book_id = input("Enter Book ID: ")

        for book in books:
            if book["book_id"] == book_id:

                if not book["available"]:
                    book["available"] = True

                    save_books(books)

                    print("Book Returned Successfully")

                else:
                    print("Book Was Not Borrowed")

                return

        print("Book Not Found")