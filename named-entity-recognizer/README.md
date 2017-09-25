# Final Project - Named Entity Recognition

In this assignment, we are asked to build a named entity recognizer for Twitter text.

## Task

Given a twitter text, we should identify the sub-spans of words that represent named entities. We are not asked to distinguish between entity types. After exploring the data set, we found that there are three type of tags: ‘O’, ‘B’, ‘I’. ‘O’ represents non-named-entity, ‘B’ means the beginning of named entity, and ‘I’ means the continue of named entity.
So basically, this NER for Twitter text is a classification problem: given each word of the twitter text, classify it into three different categories: ‘O’, ‘B’,’I’.

### Prerequisites

We used Tensorflow to implement the model. All the things you need to install is Python and Tensorflow.

```
pip install tensorflow
```


## Model

Our model is a 1-hidden-layer neural network, with an additional representation layer. We represent the context of each word as a “window” consisting of a word concatenated with its immediate neighbors:
```
x (t) = [x_t−1*L, x_t*L, x_t+1*L] ∈ R 3d
```
Where x_t-1, x_t, x_t+1 are the input one_hot row vectors and L is the embedding matrix.
We implemented this by using Tensorflow’s tf.nn.embedding_lookup. We then compute our
predictions as:
```
h = tanh(x (t)W + b1)
y = softmax(hU + b2)
```
And evaluate by cross entropy loss.


## Running the code

To run the code, simply run this command:
```
python NER.py
```
