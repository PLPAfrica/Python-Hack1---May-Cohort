# 1. Reverse a string using a stack
# def reverse_string(s: str) -> str:
#     stack = []
#     for char in s:
#         stack.append(char)
#     reversed_string = ''.join(stack.pop() for _ in range(len(stack)))

#     return reversed_string
# print(reverse_string("hello"))

# 2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def__init__(self):
        self.stack1 = []
        self.stack2 = []
 