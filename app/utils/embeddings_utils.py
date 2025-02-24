from sentence_transformers import SentenceTransformer
import numpy as np
import os

from app.utils.text_utils import load_text_from_txt

def generate_embeddings(chunks, model: SentenceTransformer):
    return model.encode(chunks)

def find_most_relevant_chunk(question, chunks, embeddings, model):
    question_embedding = model.encode([question])[0]
    similarities = []
    for embedding in embeddings:
        similarity = np.dot(question_embedding, embedding) / (
            np.linalg.norm(question_embedding) * np.linalg.norm(embedding))
        similarities.append(similarity)
    most_relevant_index = np.argmax(similarities)
    return chunks[most_relevant_index]

def get_all_cv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cv_txt_path = os.path.join(current_dir, "assets", CV_TXT)
    cv_txt = load_text_from_txt(cv_txt_path)
    return cv_txt