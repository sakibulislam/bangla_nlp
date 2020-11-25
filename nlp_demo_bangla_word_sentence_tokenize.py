from bnlp import NLTKTokenizer

def get_word_sentence_tokenize():
    bnltk = NLTKTokenizer()
    text = "আমি ভাত খাই। সে বাজারে যায়। তিনি কি সত্যিই ভালো মানুষ?"
    word_tokens = bnltk.word_tokenize(text)
    sentence_tokens = bnltk.sentence_tokenize(text)
    print('word tokens: ', word_tokens)
    print('sentence tokens: ',sentence_tokens)