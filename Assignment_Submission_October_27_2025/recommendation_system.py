import numpy as np

def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def recommend(user_index):
    """
    Finds the user most similar to the given user index based on ratings.
    """
    ratings = np.array([
        [5, 3, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [1, 0, 0, 4],
        [0, 1, 5, 4],
    ])

    similarities = []
    target_user = ratings[user_index]

    for i in range(len(ratings)):
        if i != user_index:
            sim = cosine_similarity(target_user, ratings[i])
            similarities.append((i, sim))

    # Sort users by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)

    print(f"\n User {user_index} is most similar to User {similarities[0][0]} (score = {similarities[0][1]:.2f})")

if __name__ == "__main__":
    recommend(0)  # Compare User 0 with others
