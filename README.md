## Job Recommendation System (FAISS + Sentence Transformers)
A semantic job recommendation system that matches resume text with relevent 
job description using Sentence Transformers and FAISS vector search.


# Features
- Resume text input
- Sentence embeddings using 
     all-MiniLM-L6-v2
- FAISS vector search (L2similarity)
- TOP-K job recommendations
- Optional similarity score in response
- FastAPI backend support


# Tech Stack
- Python
- pandas
- SentenceTransformers
- FAISS
- FastAPI
- Uvicorn


# Project Stucture
Job-recommendation system v2
|
|__app/
|   |__main.py
|   |__recommender.py
|   |__schemas.py
|   |__config.py
|
|___data/
|     |__jobs_clean.csv
|     |___jobposts.csv
|
|___scripts/
|      |__build_embeddings.py
|      |__build_faiss_index.py
|      |__preprocess.py
|
|__requirements.txt
|__README.md
|__.gitignore


# How It WOrks
1. Convert job descriptions into embeddings
2. Store embeddings in FAISS index
3. Convert resume text into embedding
4. Search Top-K similar jobs
5. Return job title, description and jobrequirements


# Run Locally
# Create virtual Environments
python -m venv venv
venv\scripts\activate  # windows

# install dependencies:
pip install -r requirements.txt

## Dataset
- Full dataset is not included due to size limitations

# Place your dataset inside:
data/

# Then run:
python scripts/preprocess.py
python scripts/build_embeddings.py
python scripts/build_faiss_index.py


# Run API:
uvicorn app.main:app --reload

# Open Swagger:
https://127.0.0.1:8000/docs

# API Endpoint
POST/recommend
Request Body:
{
    "query": "Data Scientist with Python and Machine Learning skills",
    "top_K: 5
}

# Response:
[
    {
        "title": "senior python Developer",
        "description": "....."
        "jobrequirements": "....."
    }
]

## Future Improvements
- Add similarity score in API
- Deploy API using Docker
- Add frontend interface
- Use larger transformer model

# Author:
Ajit Rout




  




