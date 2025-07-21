# RAG AI Agent

### command to run 

#### setup the virual enviorment 
python -m venv venv

#### unable to create virtal env on windows because of policy, use the following command
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

#### activate the virtual enviorment 
 .\venv\Scripts\activate

 #### install the dependenct from requriements file
 pip install -r .\requirements.txt

 #### download ollama to run the model locally
https://ollama.com/
after installation run ollama command from terminal

 #### pull model from ollama
ollama pull llama3.2
ollama pull mxbai-embed-large
to know more models, we can find them here -> https://ollama.com/library

 #### list the installed model on you machine
ollama list

#### run the code
python.exe .\main.py