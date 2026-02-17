import numpy as np
import faiss 
from app.config import EMBEDDINGS_PATH, FAISS_INDEX_PATH

def main():
    embeddings = np.load(EMBEDDINGS_PATH).astype("float32")
    dimension = embeddings.shape[1]
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlat(dimension)
    index.add(embeddings)

    faiss.write_index(index, FAISS_INDEX_PATH)
    print("FAISS index saved:", index.ntotal)

if __name__ == "__main__":
    main()    

