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

    def description(self):
        return self._description

    def link(self):
        return self._link

    def comment(self):
        return self._comment

    def __str__(self):
        return f"{self._title} {self._author}"
