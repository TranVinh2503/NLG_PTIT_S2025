import openai

def open_file(filepath):
    with open(filepath, 'r',encoding= 'utf-8') as file_in:
        return file_in.read()

def save_file(filepath,content):
    with open(filepath,'a', encoding='utf-8') as file_out:
        file_out.write(content)

api_key = open_file('')

openai.api_key = api_key

with open("/merged.jsonl",'rb') as file:
    response = openai.File.create(
        file=file,
        purpose = 'fine-tune'
    )

file_id = response['id']
print(file_id)