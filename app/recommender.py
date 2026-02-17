import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from app.config import MODEL_NAME, CLEAN_DATA_PATH, FAISS_INDEX_PATH
from app.schemas import RecommendationResponse

class JobRecommender:

    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.df = pd.read_csv(CLEAN_DATA_PATH)
        self.index = faiss.read_index(FAISS_INDEX_PATH)
        print("FAISS loaded:", self.index.ntotal)

    def recommend(self, resume_text: str, top_k: int = 5):
        query_embedding = self.model.encode([resume_text], convert_to_numpy=True)

        distances, indices = self.index.search(query_embedding.astype("float32"), top_k )
        print("raw indices :", indices)
        jobs = self.df.to_dict(orient="records")

        results =[jobs[int(i)] for  i in indices[0]]
        print("final length:", len(results))

        return[
            {
                "title": jobs["Title"],
                "description": jobs["JobDescription"],
                "jobrequirements": jobs["JobRequirment"]
                
            }
            for jobs in results
        ]
        



    

             

        



        

            
