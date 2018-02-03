import nltk
nltk.download('punkt')
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

{'!': True, 'animals': True, 'are': True, 'the': True, 'ever': True, 'Dogs': True, 'best': True}

pos = []
with open("C:/Users/iamsu/nlp/pos_tweets.txt", encoding="utf8") as f:
    for i in f:
        pos.append([format_sentence(i), 'pos'])
neg = []
with open("C:/Users/iamsu/nlp/neg_tweets.txt", encoding="utf8") as f:
    for i in f:
        neg.append([format_sentence(i), 'neg'])

training = pos[:int((.9)*len(pos))] + neg[:int((.9)*len(neg))]
test = pos[int((.1)*len(pos)):] + neg[int((.1)*len(neg)):]
#Building a Classifier
from nltk.classify import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(training)
classifier.show_most_informative_features()
#Classification (testing model)
example1 = "this workshop is awesome."

print(classifier.classify(format_sentence(example1)))
example2 = "this workshop is awful."

print(classifier.classify(format_sentence(example2)))

#Accuracy
from nltk.classify.util import accuracy
print(accuracy(classifier, test))

#case sensitivity
import re
re1 = re.compile('python')
print(bool(re1.match('Python')))

#Disjunction