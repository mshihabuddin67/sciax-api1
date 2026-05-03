from services.model_interface import call_llm
from services.perturb import generate_variants
from services.embeddings import embed
from services.scoring import stability, drift, risk

def analyze(prompt):

    variants = generate_variants(prompt)

    outputs = [call_llm(v) for v in variants]

    vectors = embed(outputs)

    si = stability(vectors)
    di = drift(vectors[0], vectors)

    r = risk(si, di)

    return {
        "prompt": prompt,
        "outputs": outputs,
        "stability": float(si),
        "drift": float(di),
        "risk": r
    }
