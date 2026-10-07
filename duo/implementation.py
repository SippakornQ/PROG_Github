import numpy as np

def analyze_scores(*scores):
    if not scores:
        raise ValueError("At least one score is required.")
    arr = np.array(scores, dtype=float)

    return {
        "average": float(np.mean(arr)),
        "highest": float(np.max(arr)),
        "lowest": float(np.min(arr)),
        "median": float(np.median(arr)),
        "std_dev": round(float(np.std(arr)), 2),
    }

def passing_students(*scores, pass_score=50.0):
    if not scores:
        raise ValueError("At least one score is required.")
    arr = np.array(scores, dtype=float)

    passed_count = int(np.sum(arr >= pass_score))
    failed_count = int(np.sum(arr < pass_score))

    return {
        "passed": passed_count,
        "failed": failed_count,
    }