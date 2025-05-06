import numpy as np


def search(embedding, index, k=5):
    """Mock search function to simulate vector retrieval."""
    return sorted(
        range(len(index)), key=lambda i: np.linalg.norm(embedding - index[i])
    )[:k]
