import pandas as pd
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string
from nltk.stem import 	WordNetLemmatizer
# nltk.download('wordnet')

class TextAnalysis():
    '''For Calculating these 9 variables
    AVG WORD LENGTH
    PERSONAL PRONOUNS
    SYLLABLE PER WORD
    WORD COUNT
    COMPLEX WORD COUNT
    AVG NUMBER OF WORDS PER SENTENCE
    FOG INDEX
    PERCENTAGE OF COMPLEX WORDS
    AVG SENTENCE LENGTH
    '''
    def __init__(self,link):
        '''Read and concatenate title and article text'''
        self.link = link   
        headers = { 'Accept-Language' : "en-US,en;q=0.9,hi;q=0.8,ur;q=0.7,bn;q=0.6",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
        page = requests.get(self.link,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('h1',class_='entry-title').text
        text = soup.find('div',class_='td-post-content')
        text = ''.join([i.text for i in text.find_all('p')])
        self.text = '.'.join([title,text])      

   
    def _rem_stops(self,token_text):
        stop_words = set(stopwords.words('english'))
        tokens = list(filter(lambda token_text: token_text.lower() not in stop_words, token_text))
        return tokens
    
    
    def _rem_punc(self,token_text):
        tokens = list(filter   (lambda token_text: token_text.lower() not in string.punctuation, token_text))
        return tokens
    
    def _final_tokens_nltk(self,text):
        '''remove stops and puns with nltk'''
        word_tokens = word_tokenize(text)
        rem_stopped = self._rem_stops(word_tokens)
        rem_puncs_stops = self._rem_punc(rem_stopped)
        return rem_puncs_stops

    def word_count(self):
        '''after removing stops and puns with nltk'''
        word_count = len(self._final_tokens_nltk(self.text))
        return word_count
    
    def avg_word_length(self):
        '''AVG WORD LENGTH:
            Removes punctuations from tokens
            calculates avg word length'''
        word_tokens = self._rem_punc(word_tokenize(self.text))
        avg_words = sum(len(w) for w in word_tokens)/len(word_tokens)
        return avg_words
    
    def _check_prp(self,word):
        prons = ["i","he","him","her","it","me","she","them","they","we","you"]
        if word=='US':
            return False
        else:
            if word.lower() in prons:
                return True

    def personal_pronoun(self):
        '''PERSONAL PRONOUNS:
            Removes Punctuations, tokenizes,
            calculates personal pronouns count'''
        word_tokens = self._rem_punc(word_tokenize(self.text))
        tokens = len(list(filter(lambda token_text: self._check_prp(token_text), word_tokens)))  
        return tokens

    def avg_wrd_sent(self):
        '''AVG SENTENCE LENGTH,AVG NUMBER OF WORDS PER SENTENCE:
            Removes punctuations from tokens
            calculates avg sent length'''
        word_tokens = self._rem_punc(word_tokenize(self.text))
        return len(word_tokens)/len(nltk.sent_tokenize(self.text))
    
    def _countSyllables(self,word):
        '''Excluding es,ed ending words, include ing as well.'''
        count= 0
        vowels = "aeiou"
        
        if len(word)>2 and word[-2:]=='es':
            return count
        elif len(word)>2 and word[-2:]=='ed':
            return count
        
        else:
            for ch in list(word):
                if ch in list(vowels):
                    count+=1
        return count

    def syllables_per_wrd(self):
        '''SYLLABLE PER WORD:
            Removes Punctuations, tokenizes,
            calculates syllables per words'''
        word_tokens = self._rem_punc(word_tokenize(self.text))
        avg_sylbl = sum(self._countSyllables(w) for w in word_tokens)/len(word_tokens)
        return avg_sylbl

    def complex_count(self):
        '''COMPLEX WORD COUNT
        Removes Punctuations, tokenizes,
        calculates complex word count'''
        sum = 0
        word_tokens = self._rem_punc(word_tokenize(self.text))
        for word in word_tokens:
            if self._countSyllables(word)>2:
                sum+=1
        return sum
    
    def complex_percnt(self):
        '''PERCENTAGE OF COMPLEX WORDS:
            Removes punctuations
            calculates complex percentage'''
        word_tokens = len(self._rem_punc(word_tokenize(self.text)))
        percnt = (self.complex_count()/word_tokens)*100
        return percnt

    def fog_index(self):
        '''FOG INDEX:
            Removes punctuations,
            calculates FOG index'''
        fog_index = 0.4* (self.avg_wrd_sent() + self.complex_percnt())
        return fog_index


class SentimentAnalysis(TextAnalysis):
    '''For Calculating these 4 variables
    POLARITY SCORE
    NEGATIVE SCORE
    POSITIVE SCORE
    SUBJECTIVE SCORE
    '''
    def __init__(self, link,stop_dict_link,master_dict_link):
        super().__init__(link)
        self.stop_dict_link = stop_dict_link
        self.master_dict_link = master_dict_link

    def _master_dictionary(self):
        df = pd.read_csv(self.master_dict_link,usecols=['Word','Positive','Negative'],dtype={
            'Word':'str',
            'Positive':'int16',
            'Negative':'int16'
            })

        return df

    def _stop_dictionary(self):
        # can change to list or set later
        df = pd.read_csv(self.stop_dict_link,names=['Word'])
        return df

    def _rem_dict_stops(self,text):
        '''Tokenize, rem puncs, rem 1 len words(not found in dictionary),nums normalize text'''
        wordnet_lemmatizer = WordNetLemmatizer()

        stops = self._stop_dictionary()

        tokens = word_tokenize(text)
        tokens = self._rem_punc(tokens)
        
        l = [wordnet_lemmatizer.lemmatize(i) for i in tokens if ( (len(i)>=2) & (i.upper() not in set(stops['Word'].values)) & (not i.isnumeric())  )]
        return l
    
    def pos_neg_counts(self):
        '''POSITIVE SCORE, NEGATIVE SCORE:
            Removes stop words from sraf stop words,
            Applies Lemma on words
            calculates pos and neg score '''
        pos_count = 0
        neg_count = 0
        
        master_dict = self._master_dictionary()

        tokens = self._rem_dict_stops(self.text)
        for word in tokens:
            try:
                k = master_dict[master_dict['Word']==word.upper()]
                if ((k['Positive'] >0).bool()==True):
                    pos_count+=1
                    continue #could be either pos or neg or none
                if ((k['Negative'] >0).bool()==True):
                    neg_count+=1
                    continue 

            except (KeyError,ValueError): #could result in not Found or empty series
                continue
        # return {'pos_count':pos_count,'neg_count':neg_count}
        return pos_count,neg_count

    def polarity_score(self):
        '''POLARITY SCORE:
            Removes stop words from sraf stop words,
            Applies Lemma on words
            calculates pos and neg score
            calculates polarity score '''
        pos_count,neg_count = self.pos_neg_counts()
        polar_score = (pos_count-neg_count) / (pos_count+neg_count+0.000001)
        return polar_score

    def subjective_score(self):
        '''POLARITY SCORE:
            Removes stop words from sraf stop words,
            Applies Lemma on words
            calculates pos and neg score
            calculates subjective score '''
        tokens = len(self._rem_dict_stops(self.text))
        pos_count,neg_count = self.pos_neg_counts()
        subj_score = (pos_count+neg_count) / (tokens+0.000001)
        return subj_score



#-------------------Execution Of Calculating Scores In Output Files-----------------------------#

df = pd.read_excel('/content/drive/MyDrive/coffee/output_ds.xlsx') #link to output file containing links

new_df = df.copy()
for i in range(new_df.shape[0]):
    id = new_df.iloc[i]

# Using TextAnalysis class For 9 Obj variables
    ana=TextAnalysis(id['URL'])   #url_link
    id['AVG WORD LENGTH'] = ana.avg_word_length()
    id['PERSONAL PRONOUNS'] = ana.personal_pronoun()
    id['SYLLABLE PER WORD'] = ana.syllables_per_wrd()
    id['WORD COUNT'] = ana.word_count()
    id['COMPLEX WORD COUNT'] = ana.complex_count()
    id['AVG NUMBER OF WORDS PER SENTENCE'] = ana.avg_wrd_sent()
    id['FOG INDEX'] = ana.fog_index()
    id['PERCENTAGE OF COMPLEX WORDS'] =  ana.complex_percnt()
    id['AVG SENTENCE LENGTH'] = ana.avg_wrd_sent()

# Using TextAnalysis class For 9 Obj variables

    senti = SentimentAnalysis(ana.link,"/content/drive/MyDrive/coffee/StopWord.csv", #url_link, stopwords_csv link,master_dict_csv link(containing pos,neg years)
                                      '/content/drive/MyDrive/coffee/MasterDictionary.csv')
    id['POLARITY SCORE'] = senti.polarity_score()
    pos,neg = senti.pos_neg_counts()
    id['POSITIVE SCORE'],id['NEGATIVE SCORE'] = pos,neg = senti.pos_neg_counts()
    id['SUBJECTIVITY SCORE'] = senti.subjective_score()
    print("Done!",id)
    new_df.iloc[i] = id