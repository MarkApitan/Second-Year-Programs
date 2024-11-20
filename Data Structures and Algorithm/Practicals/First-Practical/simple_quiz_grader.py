def grade_question(answer_key, student_answers, question_number):
    return answer_key[question_number] == student_answers[question_number]

def calculate_score(answer_key, student_answer):
    score = 0
    for i in range(len(answer_key)):
        if answer_key[i] == student_answer[i]:
            score += 1
    return score
