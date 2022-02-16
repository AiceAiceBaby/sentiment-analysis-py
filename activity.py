from textblob import TextBlob

sentence = input("Ënter a sentence : ")
sentenceBlob = TextBlob(sentence)
polarity = sentenceBlob.sentiment.polarity

if polarity < 0: print("Negative")
elif polarity == 0: print("Neutral")
elif polarity > 0 and polarity <=1: print("Positive")