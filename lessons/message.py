"""Class to store a message (operator overload, union types, default parameters)."""

class Email:

    to: str
    message: str
    important: bool

    def __init__(self, input_to: str, input_message: str = "", input_important: bool = False):
        """Constructor for email."""
        self.to = input_to
        self.message = input_message
        self.important = input_important

    def __str__(self) -> str:
        """Overload str method."""
        m_string: str = f'To: {self.to}\nImportant?: {self.important}\nMessage: "{self.message}"'
        return m_string
    
    def __mul__(self, factor) -> None:
        """Overload multipliaction method."""
        self.message *= factor

email_to_chiara: Email =  Email("Chiara", True)

email_to_chiara * 4

print(email_to_chiara)
