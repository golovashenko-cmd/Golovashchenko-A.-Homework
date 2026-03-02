

"""
Project: Gradebook
Follow the instructions to practice creating, appending, and modifying Python lists.
"""

# --- Create Some Lists ---

# 1. Create a list called 'subjects' and fill it with the classes you are taking:
# "physics", "calculus", "poetry", "history"
subjects = ["physics", "calculus", "poetry", "history"]

# 2. Create a list called 'grades' and fill it with your scores:
# 98, 97, 85, 88
grades = [98, 97, 85, 88]

# 3. Create a two-dimensional list to combine subjects and grades.
# Use the table below as a reference for the associated values:
gradebook = [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]]
]

# Name          |  Test Score
# ---------------------------
# "physics"     |  98
# "calculus"    |  97
# "poetry"      |  85
# "history"     |  88
#
# Assign the value into a variable called gradebook.


# 4. Print gradebook.
print (gradebook)

# --- Add More Subjects ---
gradebook.append(["computer science", 100])
# gradebook.insert(0,["matematics", 100])
# print (gradebook)


# 5. Your computer science grade is in! You got a 100.
# Add a list with the values ["computer science", 100] using a pythom list method.
# to our two-dimensional list gradebook.


# 6. Your "visual arts" grade is in! You got a 93.
# Add ["visual arts", 93] to gradebook using a python list method.
gradebook.append(["visual arts", 93])

# --- Modify The Gradebook ---

# 7. Your instructor is rewarding an extra 5 points for the visual arts class.
# Access the index of the grade for visual arts and modify it to be 5 points greater.
gradebook[-1][-1]+=5
print (gradebook)


# 8. You decided to switch poetry to a Pass/Fail option.
# Find the grade value for poetry and use a python list method to delete it.

gradebook[2].pop(-1)
print (gradebook)
# 9. Add a new "Pass" value to the poetry sublist using a python list method.
gradebook[2].append("Pass")
print (gradebook)
# --- One Big Gradebook! ---

# Provided data for Step 10:
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# 10. Create a new variable full_gradebook that combines last_semester_gradebook using a python
# list operator.
full_gradebook = last_semester_gradebook + gradebook

# Print full_gradebook to see the completed list.
print (full_gradebook) 