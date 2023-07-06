import csv


def range_of_years() -> tuple:
    """
    Set range
    :return: Tuple with range start and end
    """
    input_range = input('Enter a range of years (format: YYYY-YYYY): ')

    input_range = input_range.split('-')

    if len(input_range) != 2:
        print('ERROR! Please enter range correctly!')
        range_of_years()

    try:
        input_range = tuple(map(int, input_range))
    except ValueError:
        print('ERROR! Please use integer numbers!')
        range_of_years()

    return input_range


def find_by_years(library: str, start: int, end: int) -> list:
    """
    Searches for books that were released within a given range
    :param library: File-name of library
    :param start: Start of range
    :param end: End of range
    :return: List of found books
    """
    found_books = []

    with open(library) as file:
        books = list(csv.DictReader(file, delimiter=';'))

    for book in books:
        if start <= int(book['Release date']) <= end:
            found_books.append(book)

    return found_books


def main():
    file = 'books.csv'

    range_ = range_of_years()
    found_books = find_by_years(file, *range_)

    if len(found_books) == 0:
        print('No books found in this range')
    else:
        print('Found books:')
        for book in found_books:
            print('Book: {} | Author: {} | Release date: {}'.format(*book.values()))


main()
