# PS
The task is to build a machine learning model to filter out correct and incorrect
question answer pairs.

# Solution Approach

* combined Question and Answer with a sep_token.
* created label 1 for the provided question.
* generated negative samples by either copying question into answer or shuffling answers for the question.
* Created a custom classfication model, which takes inputs as embeddings of the sentences (derived from BERT Tokenizer)
and returns the label.
* Added the BERT layer in the model, that gives learned excellent representation of the words wrt context to the classifier.
* Achieved ~51% accuracy, which can be improved with generalisation techniques and more data and training.
