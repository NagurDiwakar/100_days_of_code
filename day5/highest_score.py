student_scores = [82, 144, 58, 12, 102, 112, 124, 168, 199, 172, 101, 111, 97]

print(max(student_scores))
print(min(student_scores))
print(sum(student_scores))

# highest number in list
# we initialize a variable to hold on to a intermediate values until we reach maximum
max_score = 0
for score in student_scores:
    if score > max_score :
        max_score = score
    
print(max_score)

# lowest number in list

min_score = student_scores[-1]

for marks in student_scores:
    if marks < min_score :
        min_score = marks
    
print(min_score)