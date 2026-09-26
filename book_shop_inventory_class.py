"""
Basic Python to class
Sarah Estes
Turning a basic code block into a class
Using code block from Project 1, Book Shop Inventory
9/26/26
"""

class BookInventory:
    """Describing book inventory"""
    def __init__(self, *books):
        """Initialize books attribute"""
        self.books = books

    def get_book_names(self, *books):
        for book in books:
            print(book.title())

BookInventory.get_book_names(
    "vampires of el norte", "the pirate queen",
    "the witch", "the haunting of hill house",
    "mexican gothic", "frankenstein",
    "dracula"
)
