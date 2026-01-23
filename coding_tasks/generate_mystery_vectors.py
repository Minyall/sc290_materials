import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')

    with open('marx_extracts.txt', 'r') as f:
        texts = f.read()

    paras = [x.replace('\n', ' ').strip() for x in texts.split('\n\n')]

    with open('insert_phrase.txt', 'r') as f:
        phrase = f.read().lower()

    split_phrase = phrase.split()
    assert len(split_phrase) == 10

    tokens = []
    for doc in nlp.pipe(paras):
        filtered_tokens = [t.lemma_.lower() for t in nlp(doc) if not t.is_stop and t.is_alpha]
        tokens.append(' '.join(filtered_tokens))

    tfidf = TfidfVectorizer(stop_words='english', max_df=0.95)
    X = tfidf.fit_transform(tokens)
    vectors = pd.DataFrame(X.todense(), columns=tfidf.get_feature_names_out())

    new_words = [w for w in split_phrase if w not in vectors.columns]
    for w in new_words:
        vectors[w] = 0.0
    vectors.loc[len(vectors)] = 0
    scores = reversed(range(1, len(split_phrase)+1))

    for word, score in zip(split_phrase, scores):
        vectors.loc[vectors.index[-1], word] = score

    assert vectors.iloc[-1].sort_values(ascending=False).head(10).index.tolist() == split_phrase

    vectors.iloc[-1],vectors.iloc[-2] = vectors.iloc[-2].copy(), vectors.iloc[-1].copy()
    vectors = vectors.sample(frac=1, axis=1)

    vectors.to_csv('mystery_vectors.csv', index=False)
    print(vectors.iloc[-2].sort_values(ascending=False).head(10))
    print(vectors.columns[:15])