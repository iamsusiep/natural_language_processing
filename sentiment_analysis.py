import nltk

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

{'!': True, 'animals': True, 'are': True, 'the': True, 'ever': True, 'Dogs': True, 'best': True}
open("C:/Users/iamsu/nlp/pos_tweets.txt")
# pos = []
# with open("pos_tweets.txt") as f:
#     for i in f:
#         pos.append([format_sentence(i), 'pos'])
# neg = []
# with open("./neg_tweets.txt") as f:
#     for i in f:
#         neg.append([format_sentence(i), 'neg'])
#
# training = pos[:int((.9)*len(pos))] + neg[:int((.9)*len(neg))]
# test = pos[int((.1)*len(pos)):] + neg[int((.1)*len(neg)):]
