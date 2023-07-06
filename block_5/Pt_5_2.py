import csv


def extend_library(file_name: str):
    """
    Adds books to the library
    :param file_name: File-name of library
    :return:
    """
    n = int(input('How many books you want to add to the list?\n'))

    books = []

    print('Enter information (use format: book,author,realease_date):')
    for i in range(n):
        entry = input(f'{i + 1}. ').split(',')
        books.append(entry)

    with open(file_name, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(books)


def find_books(library: str, author: str) -> list:
    """
    Searches for books by a given author in the library
    :param library: File-name of library
    :param author: Author to search
    :return: List of found books
    """
    found_books = []

    with open(library) as file:
        books = list(csv.DictReader(file, delimiter=';'))
    for book in books:
        if book['Author'] == author:
            found_books.append(book)

    return found_books


def main():

    file = 'books.csv'
    extend_library(file)

    author = input('Enter an author to find his books: ')
    result = find_books(file, author)
    # If no book was found
    if len(result) == 0:
        print('No books by this author found :(')
    else:
        print(f'{author} books:')
        for book in result:
            print(f'Book: {book["Book"]} | Release date: {book["Release date"]}')


main()
