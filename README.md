# Large Language Model Code Translation Research

## Overview
This repository contains the research project on the effectiveness of using large language models (LLMs) for program translation. The focus is on the readability, similarity to human-generated reference solutions, and syntactical correctness of the translated code.

## Project Structure
The repository is structured as follows:
- `data/`
  - `source-code/`: Original code samples in Java, Python, Prolog, and Haskell.
  - `intermediate-rep/`: Intermediate representations (pseudocode and descriptions) generated by the LLM.
  - `translated-code/`: Python code generated directly from the source code and from the intermediate representations.
  - `reference-samples/`: Human-written Python code samples used as references.
- `scripts/`: Contains all the scripts used for generating translations, evaluating them, and organizing the data.


## Usage
First navigate to the `scripts` directory. Then to evaluate the generated solutions: 

```python3 evaluate.py```

The other scripts in the folder provide functionality for regenerating intermediate representations and new translations. Be wary, this process can take several hours depending on the model chosen.

