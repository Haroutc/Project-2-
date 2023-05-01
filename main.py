#Brandon Nguyen
#Krystal Phan
#Haroutyun Chamelian

# Define the parsing table as a dictionary
parsingTable = {
    'E': {'a': 'TQ', '(': 'TQ'},
    'Q': {'+': '+TQ', '-': '-TQ', ')': '', '$': ''},
    'T': {'a': 'FR', '(': 'FR'},
    'R': {
        '+': '',
        '-': '',
        '*': '*FR',
        '/': '/FR',
        ')': '',
        '$': ''
    },
    'F': {'a': 'a', '(': '(E)'}
}

# Define the main function that accepts a string as input
def main(string):
  # Initialize the stack with the start symbol of the grammar and the end of input symbol
  stack = "E$"

  # If the first character of the input string is not 'a' or '(', the string is not accepted/invalid
  if string[0] != "a" and string[0] != "(":
    print("Stack:", str(list(stack[::-1])))
    print('Output: String is not accepted/invalid.')
    return

  # Process the input string and the stack in a loop until the stack is empty except for the end of input symbol
  while len(stack) > 1:
    # Print the input string and the current state of the stack
    print(f'Input: {string}')
    print("Stack:", str(list(stack[::-1])))

    # If the top of the stack matches the next input symbol, remove them both from the stack
    if stack[0] == string[0]:
      string = string[1:]
      stack = stack[1:]
    else:
      # Look up the appropriate production rule to apply for the top of the stack and the next input symbol
      initial = parsingTable.get(stack[0], None)
      secondary = initial.get(string[0], None)

      # If a valid production rule is found, replace the top of the stack with the production rule
      if secondary is not None:
        stack = secondary + stack[1:]
      else:
        # If no valid production rule is found, the input string is not accepted/invalid
        print('Output: String is not accepted/invalid.')
        return

  # If the stack is empty except for the end of input symbol and the input string is also empty, the string is accepted
  if string == stack:
    print(f"Input: {string}")
    print("Stack:", str(list(stack[::-1])))
    print('Output: String is accepted.')

# Define a list of test cases to pass to the main function
if __name__ == "__main__":
  test_cases = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]
  for test_case in test_cases:
    main(test_case)
    print("\n\n")