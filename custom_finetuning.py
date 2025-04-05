import torch
from transformers import AutoModel, AutoTokenizer

phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base-v2")

# INPUT TEXT MUST BE ALREADY WORD-SEGMENTED!
sentence = 'Tôi là trợ lí cho trung tâm tiếng anh enspire'  

input_ids = torch.tensor([tokenizer.encode(sentence)])

with torch.no_grad():
    features = phobert(input_ids)  # Models outputs are now tuples

## With TensorFlow 2.0+:
# from transformers import TFAutoModel
# phobert = TFAutoModel.from_pretrained("vinai/phobert-base")