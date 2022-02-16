from textblob import TextBlob

def sentiment_analyser(word):
    global happyWordCount, sadWordCount
    wordBlob = TextBlob(word)
    polarity = wordBlob.sentiment.polarity
    if polarity < 0: sadWordCount += 1
    elif polarity > 0 and polarity <=1: happyWordCount += 1


def dataset_matcher(word, filename):
    with open(filename, "r") as a_file:
        for line in a_file:
            line = line.strip()
            if word == line:
                return True

    return False


def number_happy(sentence):
    global happyWordCount
    for word in sentence.split():
        if dataset_matcher(word, "positive-words.txt"): happyWordCount += 1
        else: sentiment_analyser(word)


def number_sad(sentence):
    global sadWordCount
    for word in sentence.split():
        if dataset_matcher(word, "negative-words.txt"): sadWordCount += 1
        else: sentiment_analyser(word)


def output_analysis():
    print(f"Sentence: {sentence}")

    print(f'Happy words: {happyWordCount}')
    print(f'Sad words: {sadWordCount}')

    analysis = ""

    if (happyWordCount > sadWordCount): analysis = 'Positive'
    elif (happyWordCount == sadWordCount): analysis = 'Neutral'
    else: analysis = 'Negative'

    print(f"Analysis: {analysis}")


if __name__ == "__main__":
    sentence = input("Ënter a sentence : ")

    sadWordCount = 0
    happyWordCount = 0

    number_happy(sentence)
    number_sad(sentence)
    output_analysis()
