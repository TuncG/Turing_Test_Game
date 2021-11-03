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

        length = 15
        sequence = self.question
        length_input = len(sequence)
        temp = self.question.split()

        if len(temp) >= 5:
            length = 20
        if len(temp) > 10:
            length = 25

        inputs = tokenizer.encode(sequence, return_tensors='pt')

        outputs = model.generate(inputs, max_length=length, do_sample=True, temperature=0.5, top_k=40)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(text)
        if self.question[-1] == '?':
            text = text[length_input+1:]
        text = text.strip()
        return text


# sent = Sentence
# a = sent.generate_response(sent,"What is your name?")
# print(a)
