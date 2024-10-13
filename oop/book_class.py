
class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book instance for end-user readability."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance, suitable for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

