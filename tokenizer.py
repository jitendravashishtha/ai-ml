import os
import torch
#AutoTokenizer is a class from Hugging Face Transformers that automatically selects and loads the correct tokenizer for 
# a given pretrained model. It handles converting text into tokens (numerical representations) that models can process.
from transformers import AutoTokenizer
#AutoModelForCausalLM is a class that loads the appropriate causal language model (for text generation) based on 
# the model name. It is used for tasks like text completion, generation, and autoregressive prediction. 
# Both classes simplify working with many different models by automatically handling the correct configuration.
from transformers import AutoModelForCausalLM

from openai import OpenAI


os.environ["HF_TOKEN"] = 'hf_AF*******************************'  # Replace with your actual Hugging Face token
tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
print(tokenizer("Hello there!"))


input_token = tokenizer(["write an hello world application in python!"], return_tensors="pt")
print(input_token)

model = AutoModelForCausalLM.from_pretrained("google/gemma-3-1b-it", torch_dtype=torch.bfloat16)
out = model(input_ids = input_token["input_ids"]) #returns all the predection available for the input tokens
print(out)

gen_out = model.generate(input_ids = input_token["input_ids"], max_new_tokens=500)
print(gen_out) #return the response in the form of tokens
print(tokenizer.batch_decode(gen_out)) # convert the token into the readable format.
