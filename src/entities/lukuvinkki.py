class Lukuvinkki:
    def __init__(self, title, author, description, link, comment):
        self._title = title
        self._author = author
        self._description = description
        self._link = link
        self._comment = comment

    def title(self):
        return self._title

    def author(self):
        return self._author

    def __str__(self):
        return f"{self._title} {self._author}"