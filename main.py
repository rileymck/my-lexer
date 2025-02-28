import myLexer  # Ensure this is correctly named as your lexer file

while True:
    text = input('R@R > ')  # Custom prompt
    result = myLexer.run('<stdin>', text)  # Correct function call
    print(result)
