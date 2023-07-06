import csv

books = [
    ('The Curious Case Of Benjamin Button', 'F. Scott Fitzgerald', '1922'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', '1922'),
    ('The Little Prince', 'Antoine de Saint-Exupéry', '1943')
]
# Use context manager to open csv file
with open('books.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    # Write the names of the columns
    writer.writerow(
        ('Book', 'Author', 'Release date')
    )
    # Write our "library"
    writer.writerows(books)
