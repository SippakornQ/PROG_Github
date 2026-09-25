def calculate_score(quiz_score: float, exam_score: float, bonus: float = 0.0) -> float:
    average_score = (quiz_score + exam_score)/2
    return average_score + bonus

def print_result(quiz_score: float , exam_score: float , bonus: float = 0.0):
    final_score = calculate_score(quiz_score, exam_score , bonus)

    print(f"Final score: {final_score:.2f}")
    if final_score >= 50:
        print("pass")
    else:
        print("False")

print_result(78.0, 86.0, 4.0)