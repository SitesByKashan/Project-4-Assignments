MAX_TERM_VALUE: int = 10000

def fibonacci_sequence():
    current_term = 0  
    next_term = 1  
    while current_term <= MAX_TERM_VALUE:
        print(current_term, end=" ")  
        term_after_next = current_term + next_term
        current_term = next_term
        next_term = term_after_next

fibonacci_sequence()