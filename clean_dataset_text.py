from bs4 import BeautifulSoup
import pandas as pd
import spacy
from pathlib import Path

def clean_guardian_text(text:str, remove_elements:tuple[str]=('span','aside')) ->str:
    soup = BeautifulSoup(text, 'html.parser')
    [e.decompose() for e in soup.find_all() if e.name in remove_elements]
    paras = [p.text for p in soup.find_all('p', class_=None)]
    cleaned_item ='\n'.join(paras)
    return cleaned_item

def tokenise_doc(doc:spacy.tokens.Doc) -> str:
    tokens = [w.lemma_.lower() for w in doc if not w.is_stop and w.is_alpha]
    return ' '.join(tokens)

if __name__ == '__main__':
    PATH_STR = "4_topic_modelling/farage_large_dataset.parquet"
    FILE_PATH = Path(PATH_STR)
    DESTINATION_PATH = FILE_PATH.with_stem(FILE_PATH.stem + '_cleaned')

    df = pd.read_parquet(FILE_PATH)
    texts = df['body'].tolist()
    df['cleaned_text']= [clean_guardian_text(t) for t in texts]

    nlp = spacy.load('en_core_web_sm')

    BATCH_SIZE = 150
    WORKERS = -1

    tokens = []
    for doc in nlp.pipe(df['cleaned_text'].tolist(), batch_size=BATCH_SIZE, n_process=WORKERS):
        tokens.append(tokenise_doc(doc))

    df['tokens'] = tokens
    df.to_parquet(DESTINATION_PATH)


