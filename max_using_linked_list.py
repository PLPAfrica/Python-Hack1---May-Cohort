from linked_list import LinkedList

def best_score():
    """
    Find the maximum test score in a list using a LinkedList
    
    This function allows the user to input test scores, adds them to a linked list,
    and then retrieves and prints the highest score.
    
    Returns:
        None
    """
    test_scores = LinkedList()

    print("Enter test scores. Type 'done' when finished:")

    while True:
        input_score = input("Enter score: ")
        
        if input_score.lower() == 'done':
            break
        
        try:
            score = int(input_score)
            test_scores.append(score)
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")

    # Find and print the maximum score
    if not test_scores.empty():
        print("The highest test score is:", test_scores.find_max())
    else:
        print("No scores were entered.")

if __name__ == "__main__":
    best_score()
