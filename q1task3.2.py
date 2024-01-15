from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text_file, model_name, top_n=30):
    # Loading Auto Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Reading text from the file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text, add_special_tokens=False)))

    # Counting occurrences of each token
    token_counts = Counter(tokens)

    # Getting the top n most common tokens
    top_tokens = token_counts.most_common(top_n)
    return top_tokens

text_file_path = 'allcsvs.txt'
model_name = 'bert-base-uncased' 

top_tokens = count_unique_tokens(text_file_path, model_name)
print(top_tokens)