import os
import pickle
from sentence_transformers import SentenceTransformer
from app.utils.text_utils import load_text_from_txt, split_text_into_chunks
from app.utils.embeddings_utils import generate_embeddings
from app.settings import CV_TXT, MODEL_EMBEDDING


def init_embeddings():
    # Cargar texto del CV
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cv_txt_path = os.path.join(current_dir, "assets", CV_TXT)
    cv_txt = load_text_from_txt(cv_txt_path)

    # Dividir el texto en chunks
    chunks = split_text_into_chunks(cv_txt)

    # Generar embeddings
    model_embeddings = SentenceTransformer(MODEL_EMBEDDING)
    embeddings = generate_embeddings(chunks, model_embeddings)

    # Guardar los chunks y embeddings en un archivo
    with open("app/assets/embeddings.pkl", "wb") as f:
        pickle.dump({"chunks": chunks, "embeddings": embeddings, "model_embeddings": model_embeddings}, f)

    print("Inicialización completada. Chunks y embeddings guardados en 'app/assets/embeddings.pkl'.")