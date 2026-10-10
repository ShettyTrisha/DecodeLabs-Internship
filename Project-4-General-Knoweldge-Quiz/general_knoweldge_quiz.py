print("=" * 40)
print("     GENERAL KNOWLEDGE QUIZ")
print("=" * 40)

score = 0

print("\nAnswer the following 3 questions.")
print("Each correct answer gives you 1 point.\n")

# Question 1
print("1. What is the capital of France?")
answer = input("Your answer: ").strip().lower()

if answer == "paris":
    print("Correct! You earned 1 point.\n")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.\n")

# Question 2
print("2. Which planet is known as the Red Planet?")
answer = input("Your answer: ").strip().lower()

if answer == "mars":
    print("Correct! You earned 1 point.\n")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.\n")

# Question 3
print("3. What is the largest ocean in the world?")
answer = input("Your answer: ").strip().lower()

if answer == "pacific ocean" or answer == "pacific":
    print("Correct! You earned 1 point.\n")
    score += 1
else:
    print("Incorrect! The correct answer is the Pacific Ocean.\n")

# Final score
print("=" * 40)
print("           QUIZ COMPLETED")
print("=" * 40)

print("Your final score:", score, "/ 3")

if score == 3:
    print("Excellent! You answered all questions correctly.")
elif score == 2:
    print("Good job! Keep learning.")
elif score == 1:
    print("Nice try! Keep practising.")
else:
    print("Keep practising. You can improve!")

print("\nThank you for playing!")
