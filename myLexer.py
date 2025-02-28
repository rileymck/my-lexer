# Create a Token Class as given below
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, '{self.value}')"

# Create TOKENS list
RR_INT = 'RR_INT'
RR_FLOAT = 'RR_FLOAT'
RR_PLUS = 'RR_PLUS'
RR_MINUS = 'RR_MINUS'

# Create number list
DIGITS = '0123456789'

# Create a lexer class constructor
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn    
        self.text = text
        self.pos = -1 
        self.current_char = None
        self.advance()
        
    # Complete the advance function to move through characters
    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    # Making tokens function, now also includes '-' and numbers
    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(RR_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(RR_MINUS))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            else:
                self.advance()
        return tokens

    # Make number function - to handle both integer and float numbers
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break  # Second dot in a number is invalid
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(RR_INT, int(num_str))
        else:
            return Token(RR_FLOAT, float(num_str))

# Executing function
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens = lexer.make_tokens() 
    return tokens
