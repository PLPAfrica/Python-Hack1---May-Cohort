
# Reversing a String Using a Stack

def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

sentence = "Hello, world!"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)  # Outputs "world! Hello,"





