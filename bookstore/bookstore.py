def create_bookstore(name):
    store = {}
    store["name"] = name
    store["authors"] = {}
    store["authors_ids"] = 0
    store["books"] = {}
    store["books_ids"] = 0

    return store

def print_dict(mydict):
    for key, val in mydict.items():
        print(str.format("[{0}] : {1}", key, val))

def add_author(bookstore, name, nationality):
    author = {}
    bookstore["authors_ids"] = bookstore["authors_ids"] + 1
    author["name"] = name
    author["nationality"] = nationality
    author["id"] = bookstore["authors_ids"]

    bookstore["authors"][author["id"]] = author
    return author

def get_author_by_name(bookstore, name):
    for author_id, authors_dict in bookstore["authors"].items():
        if authors_dict['name'] == name:
            return authors_dict

def get_author_by_id(bookstore, author_id):
    return bookstore["authors"][author_id]

def add_book(bookstore, title, isbn, author_id):
    book = {}
    bookstore["books_ids"] = bookstore["books_ids"] + 1
    book["title"] = title
    book["isbn"] = isbn
    book["author_id"] = author_id
    book["id"] = bookstore["books_ids"]

    bookstore["books"][book["id"]] = book
    return book

def get_book_by_title(bookstore, title):
    for book_id, book_dict in bookstore["books"].items():
        if book_dict['title'] == title:
            return book_dict

def get_book_by_id(bookstore, book_id):
    return bookstore["books"][book_id]

def get_books_by_author(bookstore, author_id):
    book_list = []
    print_dict(bookstore)
    for book_id, book_dict in bookstore["books"].items():
        print_dict(book_dict)
        if book_dict["author_id"] == author_id:

            book_list.append(book_dict)

    return book_list