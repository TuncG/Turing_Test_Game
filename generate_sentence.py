import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class Sentence:
    """

    """
    question: str

    def init(self):
        self.question = ' '
        pass

    def generate_response(self, temp_ques):
        self.question = temp_ques
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        model = GPT2LMHeadModel.from_pretrained('gpt2')

        sequence = self.question

        inputs = tokenizer.encode(sequence, return_tensors='pt')

        outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=5.0, top_k=50)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return text

#sent = Sentence
#a = sent.generate_response(sent,"What is your name?")
#print(a)