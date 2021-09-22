import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

sequence = ("He began his premiership by forming a five-man war cabinet which included Chamerlain as Lord President "
            "of the Council, Labour leader Clement Attlee as Lord Privy Seal (later as Deputy Prime Minister), "
            "Halifax as Foreign Secretary and Labour's Arthur Greenwood as a minister without portfolio.")
inputs = tokenizer.encode(sequence, return_tensors='pt')

outputs = model.generate(
    inputs, max_length=200, do_sample=True, temperature=5.0, top_k=50
)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)

