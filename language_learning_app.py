import random
import time

# Expanded list of Spanish words and their English translations
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"},
    {"spanish": "grande", "english": "big/large"},
    {"spanish": "día", "english": "day"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "mujer", "english": "woman"},
    {"spanish": "niño", "english": "boy/child"},
    {"spanish": "niña", "english": "girl/child"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "trabajar", "english": "to work"},
]

def quiz_user(words, num_questions):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0
    start_time = time.time()  # Start timer

    for idx, word in enumerate(words[:num_questions], 1):
        attempts = 3
        hint_used = False
        print(f"\nQuestion {idx}/{num_questions}:")
        
        while attempts > 0:
            user_answer = input(f"What is the English translation of '{word['spanish']}'? ").strip().lower()
            correct_answer = word['english'].lower()
            
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong! You have {attempts} attempts left.")
                    if not hint_used:
                        use_hint = input("Would you like a hint? (y/n): ").strip().lower()
                        if use_hint == 'y':
                            hint_used = True
                            hint = word['english'][:3] + "..."  # Provide the first 3 letters as a hint
                            print(f"Hint: The English word starts with '{hint}'")
                else:
                    print(f"Out of attempts! The correct answer was '{word['english']}'.\n")

    # End timer
    end_time = time.time()
    total_time = end_time - start_time

    # Display final score and time taken
    print(f"\nQuiz complete! Your score: {score}/{num_questions}")
    print(f"Total time taken: {total_time:.2f} seconds")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    
    # Allow the user to choose the number of questions
    while True:
        try:
            num_questions = int(input(f"How many questions would you like? (1-{len(words)}): "))
            if 1 <= num_questions <= len(words):
                break
            else:
                print(f"Please enter a number between 1 and {len(words)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    input("Press Enter to start the quiz...")
    quiz_user(words, num_questions)

if __name__ == "__main__":
    main()
