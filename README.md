# SC290 Text & Network Analysis Course

Welcome to the SC290 course materials repository! This project provides hands-on workflows for text and network analysis, organized by topic in numbered folders. Each topic builds on the previous, guiding you through modern NLP and network analysis techniques using Python.

## Topics Covered

- **Text Cleaning & Tokenization**: Learn to preprocess raw text data for analysis.
- **Text Vectorization**: Transform cleaned text into numerical vectors for modeling.
- **Topic Modeling**: Discover latent topics in text using models like LDA.
- **Sentiment Analysis**: Apply and validate multiple sentiment models (VADER, HuggingFace, Gemini).
- **Network Analysis**: (Prototypes folder) Explore experimental approaches to network modeling.
- **Visualization**: Generate and save plots for analysis results.

All workflows are demonstrated in Jupyter notebooks, with supporting Python scripts for data preparation and validation.

## Repository Structure

- `1_Introduction/`: Course overview
- `2_text_prep/`: Text cleaning and tokenization
- `3_vectors/`: Text vectorization
- `4_topic_modelling/`: Topic modeling and visualization
- `5_sentiment/`: Sentiment analysis and validation
- `prototypes/`: Experimental notebooks and models
- Root scripts: Bulk cleaning, API credential management

## Environment Setup

This repository uses [uv](https://github.com/astral-sh/uv) for fast Python dependency management, with all dependencies specified in `pyproject.toml`.

### Steps

1. **Install Python 3.10.12**  
    Ensure you have Python 3.10.12 installed.

2. **Install uv**  
    ```bash
    pip install uv
    ```

3. **Install dependencies**  
    From the repository root:
    ```bash
    uv pip install -r requirements.txt
    # or, using pyproject.toml:
    uv venv
    uv pip install -e .
    ```

4. **Set up Jupyter kernel**  
    Make sure your environment is available as a Jupyter kernel:
    ```bash
    python -m ipykernel install --user --name=sc290-env
    ```

5. **API Credentials**  
    If using external APIs (e.g., HuggingFace, Gemini), add your keys to `cred.py`. **Never commit real keys.**

## Usage Tips

- Follow the topic folder sequence for end-to-end workflows.
- Check for required input files before running notebooks/scripts.
- Use batch processing for large datasets.
- Reference `pyproject.toml` for dependency management.

---

For more details, see the notebooks in each topic folder and the [Copilot Instructions](.github/copilot-instructions.md).
