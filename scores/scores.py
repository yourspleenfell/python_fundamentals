def scoresGrades():
    result = " "
    import random
    score = random.randint(1, 100)
    if score >= 90:
        result = "Score: " + str(score) + "; Your grade is A"
    elif score >= 80:
        result = "Score: " + str(score) + "; Your grade is B"
    elif score >= 70:
        result = "Score: " + str(score) + "; Your grade is C"
    elif score >= 60:
        result = "Score: " + str(score) + "; Your grade is D"
    elif score < 60:
        result = "Score: " + str(score) + "; Your grade is F"
    print result

scoresGrades()