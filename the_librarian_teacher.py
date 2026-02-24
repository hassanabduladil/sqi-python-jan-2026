library = [
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_of_publication": 1976, "isbn": "987-678-233-889", "available": True},
    {"title": "1984", "author": "George Orwell", "year_of_publication": 1949, "isbn": "978-045-152-4935", "available": True},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year_of_publication": 1988, "isbn": "978-006-112-2415", "available": False},
    {"title": "Purple Hibiscus", "author": "Chimamanda Ngozi Adichie", "year_of_publication": 2003, "isbn": "978-140-003-3416", "available": True},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year_of_publication": 1937, "isbn": "978-054-792-8227", "available": False},
]


def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year_of_publication = int(input("Enter the year of publication: "))
    isbn = input("Enter the ISBN: ")


    book = {
        "title": title,
        "author": author,
        "year_of_publication": year_of_publication,
        "isbn": isbn,
        "available": True
    }

    library.append(book)

    print("Book added successfully")


def view_books():
    for i, book in enumerate(library, start=1):
        availability = "Yes" if book["available"] else "No"
        print(f"{i}. {book["title"]} by {book["author"]} published in {book["year_of_publication"]} with ISBN {book["isbn"]}. Availabile? {availability}")

def update_book(isbn):

    for book in library:
        if book["isbn"] == isbn:
            title = input(f"Enter the new title of the book or leave blank to use '{book["title"]}': ")
            author = input(f"Enter the new author of the book or leave blank to use '{book["author"]}': ")
            year_of_publication = input(f"Enter the new year of publication or leave blank to use '{book["year_of_publication"]}': : ")

            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if year_of_publication:
                book["year_of_publication"] = int(year_of_publication)

            print("Book updated successfully")
            return
    print("Book not found")


def update_book(isbn):

    for book in library:
        if book["isbn"] == isbn:
            title = input(f"Enter the new title of the book or leave blank to use '{book["title"]}': ") or book["title"]
            author = input(f"Enter the new author of the book or leave blank to use '{book["author"]}': ") or book["author"]
            year_of_publication = int(input(f"Enter the new year of publication or leave blank to use '{book["year_of_publication"]}': : ")) or book["year_of_publication"]

            
            book["title"] = title
            book["author"] = author
            book["year_of_publication"] = year_of_publication

            print("Book updated successfully")
            return
    print("Book not found")


menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Quit
"""
while True:
    print(menu)

    choice = input("Enter a choice from 1 to 8: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        isbn = input("Enter the ISBN of the book you wish to update: ")
        update_book(isbn)
    elif choice == "8":
        print("Exiting...")
        break