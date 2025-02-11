# Write a program to calculate the average score and classify the student

# Classify the student
# Average score >= 8.5 : Excellence
# Average score >= 7.0 and < 8.5 : Good
# Average score >= 5.5 and < 7.0 : Fair
# Average score >= 4.0 and < 5.5 : Average
# Average score < 4.0 : Poor

# Input: Scores of subjects (list of integers)

# Output:
# Average score
# Classify the student

# Program to calculate the average score and classify the students

# Calculate function

def calculate_average(scores): 
    return sum(scores) / len(scores)
# sum() to calculate total score and divided by length (number of subjects) len() in the list to calculate average score

# Classification function

def classify_student(average):
    if average >= 8.5:
        return "Excellent"
    elif average >= 7.0:
        return "Good"
    elif average >= 5.5:
        return "Average"
    else:
        return "Poor"

# Score from user input
try:
    scores = []
    num_subjects = int(input("Enter the number of subjects: "))
    if num_subjects <= 0:
        print ("The number of subjects must be greater than 0")
    else:
        for i in range(num_subjects):
            score = float(input(f"Enter the score of subjects number {i+1}: "))
            if score > 0 and score < 10:
                print ("The score must be from 0 to 10. Please enter score again.")
                break
            scores.append(score)

        if len(scores) == num_subjects:
            average_scores = calculate_average(scores)
            # parameters is the list of scores to calculate average score

            classification = classify_student(average_scores)
            print (f"Average score: {average_scores: .2f}")
    # .2f to ensure that the average score is always displayed with exactly 2 decimal places
    
            print (f"Classify: {classification}")
        
 # f-string: 
    # Making format string faster, more readable, and more efficient
    # Allow to embed variable values, perform calculations, call functions,
    # or apply formatting directly a string without formatting manual concatenation (liên kết thủ công)
    # Only need put letter 'f' in front of the string and use curly braces '{}' to ensure the expressions to insert into the string


except ValueError:
    print ("Invalid scores. Please enter valid scores.")

