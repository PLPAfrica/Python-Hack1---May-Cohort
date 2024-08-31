from src.stack_reverse import reverse_string

def test_reverse_string():
    """
    This function tests the reverse_string function from the src.stack_reverse module.

    It tests the reverse_string function with various inputs and asserts that the
    expected output matches the actual output. It also tests the function's behavior when
    given a non-string input.
    
    Raises:
    AssertionError: If any of the test cases fail.
    ValueError: If the reverse_string function raises a ValueError for a non-string input.
    """

    # Test cases with assertions and print statements
    s = "Wellcome To My Data Structure Class Let's Have Fun Together!"
    reversed_s = reverse_string(s)
    print(f"Original String: {s}, Reversed String: {reversed_s}")  # Display output
    assert reversed_s == "!rehtegoT nuF evaH s'teL ssalC erutcurtS ataD yM oT emoclleW"

    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("madam") == "madam"
    assert reverse_string("wuodrose") == "esordouw"

    # Test with non-string input
    try:
        reverse_string(12345)
        assert False, "Did not raise ValueError for non-string input"
    except ValueError:
        print("ValueError raised as expected for non-string input")  # Display output
        assert True

if __name__ == "__main__":
    test_reverse_string()
    print("All reverse_string tests passed!")
