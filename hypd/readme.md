HYPD: product recommendation problem 
PPT Format: https://docs.google.com/presentation/d/17s89xQqL7nk2fqKzNBzHgbk-XM8amp5XL-WuTOTi00w/edit?usp=sharing

# PS:
1 Design a recommendation engine for the content creators, to recommend products based on their content and elaborate it.

2 Do you think ML is even required in this case.

3 Do you think the given data points are sufficient for building the product recommendation engines for the creators.

4 If you believe additional data points are required to solve the given problems, please list down the data points that you think could be handy. And explain your data collection strategy.

5 Any other thoughts you might want to share.

# Solution:

## 1. Recommendation Engine Pipeline
Data Extraction
Data Preprocessing
Model Training and Hyper parameter Tuning
Prediction
Post Processing
Evaluation

### Data Extraction
The following data points can be useful for the recommendation:
From content.json  (explicit + implicit data)
*  Catalog_ids
*  Hashtags
*  Interests
*  Genders
*  caption
From catalog.json
*  Catalog_id
*  Name
*  keywords

### Data Preprocessing
* lowering texts
* preprocessing text (only for captions)
  * tokenizing
  * removing special characters
  * removing stop words (added few extra words to nltk stop words like today, get etc.,)

* combining these text from content and creating a set (for input)
  * hashtags
  * interests
  * genders
  * caption
  * catalog_tags

### Model Training and Parameter Tuning
* The content based filtering technique can be used here, since we can recommend products to users by combining the tags associated with products and previously used (tags and captions) by creators.Therefore the following steps:
* Combine data into corpus
  * Here the hashtags, interests, gender, and captions after preprocessing will be converted into a corpus i.e., by joining them.
* Vectorize the corpus
  * The corpus which is text, needs to be converted into numbers, hence an approach from amongst these can be used
  * TFIDF: importance of words for sentences
  * Bag Of Words: considers no of appearance of each words
  * Word2Vec:  considers placement of words
  * Here, the hyper parameters of these models will require tuning.
 
### Prediction
* The data points should be converted to corpus.
* A similarity score will be used for given points, with training points, the similarity scores that can be tried out:
* Cosine similarity.
* Manhattan distance.
* Jaccard distance.
* The top n titles can be returned.


## 2. ML is required?
Without ML, we would have been just using tags, and find all the similar products, without even ranking. Therefore when we use ml here ( *text retrival using nlp)*, measure the combined distance of the tags provided with the training points, and rank them based on their similarity score.

## 3,4.  Given Points are enough?
I guess for the content based filtering, the given data points are enough, when the keywords of the catalog gives the complete description of the product. 

## 5. Other Thoughts
Additional data points can be created around the given dataset like adding color to the product and their respective tags, removing common adjectives like beautiful from the tags to further strengthen the dataset.
