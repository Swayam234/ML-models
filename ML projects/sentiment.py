import nltk
from nltk.corpus import movie_reviews
nltk.download("movie_reviews")
movie_reviews.words()
nltk.FreqDist(movie_reviews.words()) #Displays frequency of words
nltk.FreqDist(movie_reviews.words())['happy'] # prints frequency of the word "happy"
nltk.FreqDist(movie_reviews.words()).most_common(15) #prints frequency of 15 most common words
movie_reviews.categories()
movie_reviews.fileids(categories="pos")
movie_reviews.fileids()
movie_reviews.fileids("pos") #prints fileids of positive reviews
movie_reviews.fileids("neg")  #prints file ids of negative reviews
movie_reviews.words("neg/cv001_19502.txt") 

import random
documents=[(list(movie_reviews.words(fileid)),category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

#Define the feature extractor
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=list(all_words)[:2000]
print(all_words)
def document_features(document):
    document_words=set(document)
    features={}
    for word in word_features:
        features['contains({})'.format(word)]=(word in document_words)
    return features

#Train Naive bayes classifier
featuresets=[(document_features(d),c) for(d,c) in documents]
train_set,test_set=featuresets[100:],featuresets[:100]
classifier=nltk.NaiveBayesClassifier.train(train_set)

#Test the classifier
print(nltk.classify.accuracy(classifier,test_set))
#Show the most important features as interpreted by Naive Bayes
classifier.show_most_informative_features(5)