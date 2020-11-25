from bnlp import BasicTokenizer

def get_bangla_tokenization():
    basic_tokenizer = BasicTokenizer()
    raw_text = "আমি বাংলায় গান গাই।"
    tokens = basic_tokenizer.tokenize(raw_text)
    print('basic tokens: ', tokens)