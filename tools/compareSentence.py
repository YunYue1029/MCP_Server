import re

STOP_WORDS = {"the", "a", "an", "in", "on", "at", "of", "to"}

def preprocess_to_words(text):
    text = re.sub(r"[^\w\s']", '', text)
    words = text.lower().strip().split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    return filtered_words

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

    i, j = m, n
    steps = []
    while i > 0 or j > 0:
        action = trace[i][j]
        if action == 'match':
            i -= 1
            j -= 1
        elif action == 'sub':
            steps.append(f"  {s1_words[i-1]} (substitution)")
            i -= 1
            j -= 1
        elif action == 'ins':
            j -= 1
        elif action == 'del':
            steps.append(f"  {s1_words[i-1]} (delete)")
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