import nlp_demo_bangla_tokenize as nlp_basic_tokenize
import nlp_demo_bangla_word_sentence_tokenize as nlp_nltk_tokenize

try:
    if __name__ == '__main__':
        nlp_basic_tokenize.get_bangla_tokenization()
        nlp_nltk_tokenize.get_word_sentence_tokenize()

except Exception as e:
    print('Exception is: ', e.with_traceback())