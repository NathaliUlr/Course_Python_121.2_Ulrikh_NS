from book import Book

library = [
    Book('The Great Gatsby', 'F.Scott Fitzgerald'),
    Book('Anna Karenina', 'Leo Tolstoy'),
    Book('Jane Eyre', 'Charlotte Bronte')
]

for book in library:
    print(f'{book.book_title} - {book.author}')
