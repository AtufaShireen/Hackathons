# PS: Sentiment Analysis problem

* Scrape a blogging website and calculate sentiment scores of each blog.
* Include the following for Text Analysis:
  *    AVG WORD LENGTH
  *    PERSONAL PRONOUNS
  *    SYLLABLE PER WORD
  *    WORD COUNT
  *    COMPLEX WORD COUNT
  *    AVG NUMBER OF WORDS PER SENTENCE
  *    FOG INDEX
  *    PERCENTAGE OF COMPLEX WORDS
  *    AVG SENTENCE LENGTH

* Include the following for Sentiment Analysis:
  *    POLARITY SCORE
  *    NEGATIVE SCORE
  *    POSITIVE SCORE
  *    SUBJECTIVE SCORE

# Solution:
* used beautiful soup for extracting data from website.
* used nltk for text preprocessing, including lemmatization.
* stop words removed from https://sraf.nd.edu/textual-analysis/resources/ .
* Positive and negative words accounted from https://sraf.nd.edu/textual-analysis/resources/.

## sentiment Analysis:
* Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
* Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
* Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 

Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
* Subjectivity Score: This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 

Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)

## Analysis of Readability:
* Average Sentence Length = the number of words / the number of sentences.
* Complex words are words in the text that contain more than two syllables.
* Percentage of Complex words = the number of complex words / the number of words.
* Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words).


* Average Number of Words Per Sentence = the total number of words / the total number of sentences.
* word count: number of words after removing the stop words (using stopwords class of nltk package), removing any punctuations like ? ! ,.
* Syllables count: counting the vowels present in each word and also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.
* personal pronouns: “I,” “we,” “my,” “ours,” and “us”, etc. Special care is taken so that the country name US is not included in the list.
* avg word length: Sum of the total number of characters in each word/Total number of words.

