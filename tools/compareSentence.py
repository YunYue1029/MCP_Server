def compare_sentence_mismatch(arguments):
    original = arguments.get("original", "")
    spoken = arguments.get("spoken", "")

    if not original or not spoken:
        return {"error": "Missing 'original' or 'spoken' in arguments."}

    original_words = original.split()
    spoken_words = spoken.split()

    result = []
    i, j = 0, 0
    correct = 0
    total = len(original_words)

    while i < len(original_words):
        if j < len(spoken_words) and original_words[i] == spoken_words[j]:
            result.append(original_words[i])
            correct += 1
            i += 1
            j += 1
        elif j < len(spoken_words) and (i + 1 < len(original_words) and original_words[i + 1] == spoken_words[j]):
            result.append(f"{original_words[i]}(missing)")
            i += 1
        elif j < len(spoken_words):
            result.append(f"{original_words[i]}({spoken_words[j]})")
            i += 1
            j += 1
        else:
            result.append(f"{original_words[i]}(missing)")
            i += 1

    accuracy = round((correct / total) * 100, 2) if total > 0 else 0.0

    return {
        "comparison_result": " ".join(result),
        "accuracy": f"{accuracy}%"
    }