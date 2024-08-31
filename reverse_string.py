# Reversing  a String Using a Stack
def reverse_string(s: str) -> str:
    # Create an empty list that we’ll use as a stack to hold characters.
    stack = []
    
    # Go through each character in the string and add it to our stack.
    # Think of the stack like a stack of plates where you add new plates on top.
    for char in s:
        stack.append(char)
    
    # Now we need to create the reversed version of the string.
    # We do this by removing characters from the top of the stack.
    # Removing from the top of the stack gives us characters in reverse order.
    reversed_str = ''.join(stack.pop() for _ in range(len(stack)))
    
    return reversed_str

# Let's test our function with a string to see if it works.
fun_fact_string = "Did you know you can't say stupid with your mouth shut"
print(reverse_string(fun_fact_string)) 

## Output: tuhs htuom ruoy htiw diputs yas t'nac uoy wonk uoy diD