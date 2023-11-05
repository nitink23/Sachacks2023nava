import json
from sentence_transformers import SentenceTransformer
import numpy as np

def sentence_transfrom(filtered):
    # Load a pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    word =model.encode(filtered)
    # Generate embeddings
    return word

with open("technology_keywords.json", "r") as f:
    data = json.load(f)

objs = []
counter = 0

for job in data:
    counter = counter +1
    obj = dict(job)
    obj['vectorized']= sentence_transfrom(job['reqs']).tolist()
    objs.append(obj)
    print("COUNTER", counter)
   
with open("vectorized.json", "w") as f:
    json.dump(objs, f) 