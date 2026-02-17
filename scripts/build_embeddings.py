import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from app.config import MODEL_NAME, CLEAN_DATA_PATH, EMBEDDINGS_PATH

def main():
    df = pd.read_csv(CLEAN_DATA_PATH)
    texts = df["full_text"].tolist()
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts, show_progress_bar=True)
    np.save(EMBEDDINGS_PATH, embeddings)
    print("Embeddings saved:", embeddings.shape)

if __name__ == "__main__":
    main()   
     