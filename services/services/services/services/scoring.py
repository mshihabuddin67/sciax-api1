import numpy as np

def stability(embeddings):
    sims = []

    for i in range(len(embeddings)):
        for j in range(i+1, len(embeddings)):
            sims.append(
                np.dot(embeddings[i], embeddings[j])
            )

    return sum(sims) / len(sims)


def drift(base, variants):
    return float(np.mean([
        np.linalg.norm(base - v)
        for v in variants
    ]))


def risk(si, di):
    if si < 0.5:
        return "HIGH"
    elif di > 0.7:
        return "MEDIUM"
    return "LOW"
