Demonstrates how to use the Hugging Face Transformers library to tokenize input text, run inference with a causal language model, and decode generated outputs. It also includes commented code for generating embeddings using the OpenAI API.

# Requirements
- Python 3.8+
## Install dependencies
- pip install transformers
- pip install openai
## How it works
### Set Hugging Face Token
The script sets the HF_TOKEN environment variable for authentication.

### Tokenization
Loads the google/gemma-3-1b-it tokenizer and tokenizes input text.

### Model Inference
Loads the google/gemma-3-1b-it causal language model, runs inference, and generates new tokens.

### Decoding
Decodes generated tokens into readable text.

### OpenAI Embeddings (Commented Example)
Shows how to use the OpenAI API to generate text embeddings.

##### Notes: 
- Replace the Hugging Face and OpenAI API keys with your own credentials.
- The OpenAI embedding example is commented out; uncomment and configure as needed.

https://tiktokenizer.vercel.app/?model=google%2Fgemma-7b 
