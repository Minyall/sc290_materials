# Copilot Instructions for SC290 Materials

## Project Overview
This codebase supports a text and network analysis course, organized by topic in numbered folders. Each topic builds on the previous, covering text cleaning, vectorization, topic modeling, sentiment analysis, and more. Most workflows are demonstrated in Jupyter notebooks, with supporting Python scripts for data preparation and validation.

## Directory Structure
- `1_Introduction/`: Course intro (empty)
- `2_text_prep/`: Text cleaning and tokenization (`2_text_prep.ipynb`, `farright_dataset.parquet`)
- `3_vectors/`: Text vectorization (`3_vectors.ipynb`, cleaned dataset)
- `4_topic_modelling/`: Topic modeling and visualization
- `5_sentiment/`: Sentiment analysis, validation, and external API integration
- `prototypes/`: Experimental notebooks and models
- Root scripts: `clean_dataset_text.py` (bulk cleaning/tokenization), `cred.py` (API keys)

## Key Workflows
- **Data Cleaning**: Use `clean_dataset_text.py` to process raw text datasets. Output is saved as a new parquet file with cleaned and tokenized text.
- **Notebook-Driven Analysis**: Each topic folder contains a notebook that demonstrates the main workflow for that topic. Notebooks expect input files from previous steps (e.g., cleaned datasets).
- **Sentiment Validation**: `5_sentiment/validating_approaches.py` runs multiple sentiment models (VADER, HuggingFace, Gemini) and saves results/plots. Requires API keys in `cred.py`.

## Conventions & Patterns
- **Data Flow**: Parquet files are the main data exchange format between steps. Each step reads from the previous step's output.
- **API Keys**: Store sensitive keys in `cred.py` (never commit real keys).
- **Batch Processing**: Use spaCy's `nlp.pipe` for efficient bulk tokenization.
- **External APIs**: Sentiment analysis integrates VADER, HuggingFace Transformers, and Google Gemini (see `validating_approaches.py`).
- **Plotting**: Visualizations are saved as PNG/HTML in topic folders.

## Build & Environment
- Python 3.10.12 required (see `pyproject.toml`).
- Install dependencies with `pip install -r requirements.txt` or use Poetry (see `pyproject.toml`).
- Notebooks require kernels with all dependencies installed.

## Tips for AI Agents
- Always check for required input files before running notebooks/scripts.
- Follow the topic folder sequence for end-to-end workflows.
- Reference `pyproject.toml` for dependency management.
- Use batch processing and efficient I/O for large datasets.
- When integrating new models or APIs, add credentials to `cred.py` and document usage in the relevant notebook/script.

## Example: Cleaning Workflow
1. Run `clean_dataset_text.py` to process `2_text_prep/farright_dataset.parquet`.
2. Output: `2_text_prep/farright_dataset_cleaned.parquet`.
3. Use cleaned file in `3_vectors/3_vectors.ipynb`.

---
For questions or unclear conventions, review topic notebooks and root scripts for examples. Update this file if new workflows or patterns are added.
