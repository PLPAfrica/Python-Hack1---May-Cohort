class stack:
    def __init__(strg):
        strg.stack = []
       
    
    def check_empty(strg):
        return len(strg.stack) == 0
    
    def push(strg, txt):
        strg.stack.append(txt)
    
    def pop(strg):
        if strg.check_empty():
            return "strg is empty"
        
        return strg.stack.pop()

def reverse_string(input_string):
    Stack = stack()



    for txt in input_string:
        Stack.push(txt)


    reversed_string = ""
    while not Stack.check_empty():
        reversed_string += Stack.pop()
        
    return reversed_string

input_string  = "Python progamming is fun"
reversed_string = reverse_string(input_string)

print("original string:", input_string)

print("Reversed string:", reversed_string)

