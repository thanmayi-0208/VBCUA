def semantic_score(user_text, reference_text):
    user_words = set(user_text.lower().split())
    reference_words = set(reference_text.lower().split())

    common_words = user_words.intersection(reference_words)

    if len(reference_words) == 0:
        return 0

    score = (len(common_words) / len(reference_words)) * 100
    return round(score, 2)