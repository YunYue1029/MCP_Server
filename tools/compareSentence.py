import re

def compare_sentence_mismatch(arguments):
    original = arguments.get("original", "")
    spoken = arguments.get("spoken", "")

    if not original or not spoken:
        return {"error": "Missing 'original' or 'spoken' in arguments."}

    original_words = original.split()
    spoken_words = spoken.split()

    # 建立小寫版本供比較用
    original_words_lower = [w.lower() for w in original_words]
    spoken_words_lower = [w.lower() for w in spoken_words]

    result = []
    i, j = 0, 0
    correct = 0
    total = len(original_words)

    while i < len(original_words):
        if j < len(spoken_words) and original_words_lower[i] == spoken_words_lower[j]:
            result.append(original_words[i])  # 保留原字
            correct += 1
            i += 1
            j += 1
        elif j < len(spoken_words) and (i + 1 < len(original_words) and original_words_lower[i + 1] == spoken_words_lower[j]):
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

def preprocess_to_words(text):
    # 移除標點符號並轉小寫
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip().split()

def levenshtein_words(s1_words, s2_words):
    m, n = len(s1_words), len(s2_words)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    trace = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
        trace[i][0] = 'del'
    for j in range(n + 1):
        dp[0][j] = j
        trace[0][j] = 'ins'
    trace[0][0] = None

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1_words[i - 1] == s2_words[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                trace[i][j] = 'match'
            else:
                choices = [
                    (dp[i - 1][j] + 1, 'del'),
                    (dp[i][j - 1] + 1, 'ins'),
                    (dp[i - 1][j - 1] + 1, 'sub')
                ]
                dp[i][j], trace[i][j] = min(choices, key=lambda x: x[0])

    # 反向回推步驟
    i, j = m, n
    steps = []
    while i > 0 or j > 0:
        action = trace[i][j]
        if action == 'match':
            steps.append(f"  {s1_words[i-1]} == {s2_words[j-1]} (match)")
            i -= 1
            j -= 1
        elif action == 'sub':
            steps.append(f"  {s1_words[i-1]} → {s2_words[j-1]} (substitution)")
            i -= 1
            j -= 1
        elif action == 'ins':
            steps.append(f"  _ → {s2_words[j-1]} (insert)")
            j -= 1
        elif action == 'del':
            steps.append(f"  {s1_words[i-1]} → _ (delete)")
            i -= 1

    steps.reverse()
    return dp[m][n], steps

def compare_sentence_word_level(arguments):
    original_raw = arguments.get("original", "")
    spoken_raw = arguments.get("spoken", "")

    if not original_raw or not spoken_raw:
        return {"error": "Missing 'original' or 'spoken' in arguments."}

    original_words = preprocess_to_words(original_raw)
    spoken_words = preprocess_to_words(spoken_raw)

    distance, trace_steps = levenshtein_words(original_words, spoken_words)
    max_len = max(len(original_words), 1)
    accuracy = round((1 - distance / max_len) * 100, 2)

    differences = [step for step in trace_steps if "(match)" not in step]

    return {
        "levenshtein_distance": distance,
        "accuracy": f"{accuracy}%",
        "differences": differences
    }