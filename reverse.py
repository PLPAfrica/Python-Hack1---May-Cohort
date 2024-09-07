# Define the function to be tested
def reverse_string(s: str) -> str:
    return s[::-1]  # Simple implementation using slicing

# Define test functions
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    print("test_reverse_string passed")


#Run all tests
if __name__ == "__main__":
    test_reverse_string()
    print("reverse_string passed!")