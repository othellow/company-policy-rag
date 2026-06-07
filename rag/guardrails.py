from config import MIN_RELEVANCE_SCORE


def is_policy_question(retrieved_results):
    """
    Returns True if the query appears related
    to the policy corpus.
    """

    distances = retrieved_results["distances"][0]

    best_score = min(distances)

    return best_score < MIN_RELEVANCE_SCORE


