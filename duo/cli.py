from implementation import analyze_scores, passing_students

def parse_user_scores():
    raw_input = input(">> Enter student scores (separated by space): ").strip()

    if not raw_input:
        print("  [!] Error: Score input cannot be empty.")
        return None

    try:
        score_list = [float(val) for val in raw_input.split()]
        for score in score_list:
            if score < 0 or score > 100:
                print(f"  [!] Error: Invalid score '{score}'. Score must be between 0 and 100.")
                return None

        return score_list

    except ValueError:
        print("  [!] Error: Invalid numeric input. Please enter numbers only.")
        return None

def show_menu():
    print("\n" + "=" * 35)
    print("   STUDENT SCORE EVALUATOR (CLI)")
    print("=" * 35)
    print(" [1] Calculate Statistical Analysis")
    print(" [2] Evaluate Pass/Fail Threshold")
    print(" [3] Exit Program")
    print("-" * 35)

def main():
    while True:
        show_menu()
        user_choice = input("Select an option (1-3): ").strip()

        if user_choice == "1":
            scores = parse_user_scores()
            if scores is not None:
                try:
                    summary = analyze_scores(*scores)
                    print("\n--- STATISTICAL SUMMARY ---")
                    print(f" Average Score : {summary['average']:.2f}")
                    print(f" Highest Score : {summary['highest']}")
                    print(f" Lowest Score  : {summary['lowest']}")
                    print(f" Median Score  : {summary['median']}")
                    print(f" Std Deviation : {summary['std_dev']}")
                except ValueError as err:
                    print(f"  [!] Calculation Error: {err}")

        elif user_choice == "2":
            scores = parse_user_scores()
            if scores is not None:
                try:
                    threshold_input = input(
                        ">> Enter pass cutoff score (Default = 50): "
                    ).strip()

                    if threshold_input == "":
                        result = passing_students(*scores)
                    else:
                        cutoff = float(threshold_input)
                        result = passing_students(*scores, pass_score=cutoff)

                    print("\n--- PASS / FAIL SUMMARY ---")
                    print(f" Total Passed : {result['passed']} student(s)")
                    print(f" Total Failed : {result['failed']} student(s)")
                except ValueError as err:
                    print(f"  [!] Invalid Cutoff Error: {err}")

        elif user_choice == "3":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("  [!] Invalid choice. Please select option 1, 2, or 3.")

if __name__ == "__main__":
    main()