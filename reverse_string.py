def reverse_string(input_string: str) -> str:
    stack_data = []
    for character in input_string:
        stack_data.append(character)
    
    reversed_output = ''.join(stack_data.pop() for _ in range(len(stack_data)))
    return reversed_output

