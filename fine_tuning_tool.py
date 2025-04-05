import yaml,json


"""
"messages": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""},
        {"role": "assistant", "content": ""}
    ]
"""
data = []

with open('data/stories/stories_demo.yml', 'r',encoding='utf-8') as f:
    stories_file = yaml.safe_load(f)

with open('domain.yml', 'r',encoding='utf-8') as f:
    domain_file = yaml.safe_load(f)

with open('data/nlu/nlu_demo.yml', 'r',encoding='utf-8') as f:
    nlu = yaml.safe_load(f)

actions = set()
intents = set()

for story in stories_file["stories"]:
    messages = []
    data_test = {}
    for step in story["steps"]:
            if "action" in step and step['action'] in domain_file["responses"]:
                action_text = domain_file["responses"][step['action']]
                for content in action_text:
                    content_assistant = content['text']
            if "intent" in step: 
                for intent_data in nlu['nlu']:
                    if intent_data['intent'] == step['intent']:
                            content_user = intent_data['examples']

    # Khởi tạo một message cho mỗi story
    message_system = {
        "role": "system",
        "content": story['story']
    }
    message_user = {
         "role": "user", 
         "content": content_user
    }
    message_assistant = {
          "role": "assistant", 
         "content": content_assistant
    }
    messages.append(message_system)
    messages.append(message_user)
    messages.append(message_assistant)
    data_test['messages'] = messages
    data.append(data_test)



with open('fine_tuning/demo.jsonl', 'w', encoding='utf-8') as f:
    for message in data:
        json.dump(message, f, ensure_ascii=False)
        f.write('\n')

print("Data has been written to output.jsonl")
       



