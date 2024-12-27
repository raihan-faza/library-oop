class Book:
    def __init__(
        self, book_id: int, name: str, author: str, content: dict[str, int]
    ) -> None:
        self.id = book_id
        self.name = name
        self.author = author
        self.content = content

    def get_book_id(self) -> int:
        return self.id

    def get_author(self) -> str:
        return self.author

    def get_book_name(self) -> str:
        return self.name

    def get_content(self) -> dict:
        return self.content
