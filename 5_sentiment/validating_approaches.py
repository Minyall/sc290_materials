from datasets import load_dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
from pathlib import Path

path = Path("validation_labels.csv")
if not path.exists():
    data = load_dataset("stanfordnlp/sst2")
    sample = data['validation'].to_pandas().sample(100, random_state=42)
    corpus = sample['sentence'].tolist()

    print('Data Loaded')
    # VADER
    analyzer = SentimentIntensityAnalyzer()
    vader_guesses = []
    for item in corpus:
        scores = analyzer.polarity_scores(item)
        vader_guesses.append(scores['compound'])

    sample['vader'] = vader_guesses
    print('Vader Labels Done')


    # TRANSFORMER
    analyzer = pipeline('sentiment-analysis')
    transformer_guesses = []
    for item in corpus:
        result = analyzer(item)[0]['label']
        transformer_guesses.append(result)

    sample['transformer'] = transformer_guesses
    print('Transformer Labels Done')
    # GEMINI


    from google import genai
    from cred import GEMINI_KEY

    client = genai.Client(api_key=GEMINI_KEY)
    config = genai.types.GenerateContentConfig(
            temperature=1.0,
            response_mime_type="application/json",
        )

    prompt = "You are a sentiment classifier that " \
    "classifies documents as either positive or negative. " \
    "Analyze each document provided and assign it either the label " \
    "positive or negative depending on the sentiment it expresses."

    contents = prompt + sample[['sentence']].to_json(orient='index')
    contents = [genai.types.Part.from_text(text=x) for x in contents]

    response = client.models.generate_content(model="gemini-2.0-flash",
                    config=config,
                    contents=contents,
    )

    structured = json.loads(response.text)
    records = {}
    for item in structured:
        records.update(item)
    records = {int(k):v for k,v in records.items()}

    ai_labels = pd.DataFrame.from_dict(records, orient='index', columns=['AI_label'])
    sample = sample.merge(ai_labels, left_index=True, right_index=True)
    print('Ai Labels Done')
    sample.to_csv(path)


sample = pd.read_csv(path)
sample['label'] = sample['label'].map({0:'Negative', 1:'Positive'})
plt.figure()
sns.catplot(data=sample,x='label', hue='label', y='vader',kind='box').set(title='Vader Labels')
plt.tight_layout()
plt.savefig('vader.png',dpi=400)

plt.figure()
ct = pd.crosstab(sample['label'], sample['transformer'])
ct = ct.divide(ct.sum(axis=1), axis=0)
sns.heatmap(ct, cmap='coolwarm', annot=True, fmt=".2f").set(title='Transformer Labels')
plt.tight_layout()
plt.savefig('transformer.png', dpi=400)

plt.figure()
ct = pd.crosstab(sample['label'], sample['AI_label'])
ct = ct.divide(ct.sum(axis=1), axis=0)
sns.heatmap(ct, cmap='coolwarm', annot=True, fmt=".2f").set(title='Gemini Labels')
plt.tight_layout()
plt.savefig('gemini.png', dpi=400)