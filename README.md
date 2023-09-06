
# NLP using NLTK

## Introduction
Natural Lanuage Processing (NLP) is a field of aritificial intelligence that focuses on the interaction between computers and human language. It is the abiity of a computer progrma to understand human langage as it is spoken and written. It combines computational linguisitcs - rule based modelling of human language - with statistical, machine learning, and deep learning models. It drives computer programs that translate text from one language to another, respond to spoken commands, and summarized large volumes of text rapidly -even on real time.

### Steps in NLP
- Lexical analysis: _Identifying and analyzing the structure of words._
   
- Syntactic Analysis (Parsing): _Analysis of words in the sentence for grammar and arranging words in a manner that shows the relationship among the words._

- Semanic Analysis: _Draws the exact meaning or dictionry meaning from the text._

- Discourse Integration: _Understanding and modeling how diffeet parts of a text or conversation are connected in terms of meaning, coherence, and context._

- Pragmatic Analysis: _Focuses on the study of how language is used in conext to conve meaning beyond the literal interpretation of words and sentences._

### Use cases of NLP
Some use case of NLP are :
- Spam detection
- Virtual agents and chatbots
- Social media sentiment analysis
- Text summarization
- Speech recognition

## NLP using NLTK
[NLTK](https://www.nltk.org/) is a standard python library that provides a set of diverse algorithms for NLP. It provides various text processing librabries with a lot of test datasets.
#### Installation of NLTK (For Windows)
Installing  virtual environment:
```
py -m venv env
```
Activating virtual environment:
```
.\env\Scripts\activate
```
Installing ntlk:

```
pip install nltk
```

#### Installation of datasets
```
 import nltk
 nltk.download()
```
## Test Preprocessing
Text preprocessing in NLP(Natural Language Processing) is a crucial step that involves cleaning and tansforming raw text data into a format that is suitable for analysis and modeling. It is method to clean the text data and make it ready to feed data tot he model. Text data contains noise in various forms like emotions, punctuation, text in a different case. So, it is necessary to clean such noises in textual data before feeding to the model.

###  Techniques for text preprocessing
Some techniques for the textual data preprocessing are given below:
#### 1. Tokenization
Tokeniztion is the process of breaking down a text or a sequence of characters into smaller units, typically words or subwords, referred to as tokens. Tokenization can be performd in different ways, depending on the specific requirements of the NLP task and the language being processed. Common tokeization methods include:
- Word Tokenization:
    It splits text into individual words based on whitespace or punctuation marks.
- Sentence Tokenization: 
    It is the process of splitting a text or document into individual senntences. 
#### 2. Lower casing
Lower casing is a text preprocessing technique that involves converting all the letters in a given text or document to lowercase. Lowercasing ensures that all the text is in a consistent format. 
#### 3. Stopwords removal
Stopword removal is a text preprocessing technque in natural language processing(NLP)
that involves eliminating common wordsfrom a text or document. Stopwords are words that are very frequent in a laguage but often do not carry significant meaning by themselves.Examples of stopwords in English include "the","and","is","in"m"of", and "it".
#### 4. Part of Speech (POS) tagging
Part-of-Speech tagging is a fundamental task in natural language processing(NLP). It involves assigning a specific grammatical category, r part of speech. to each word in a sentence or text. The part of speech indicates th word's suntactic and grammatical role in a sentence, such as whether it is a noun, verb, adjective, adverb, etc.

Examples of common POS tags include:
- Noun (NN)
- Verb (VB)
- Adjective (JJ)
- Adverb (RB)
- Pronoun (PRP)
- Preposition (IN)

#### 5. Stemming
Stemming is a process to reduce the word to its root or base form, called the "stem".The purpose of stemming is to normalize words.

#### 6. Lemmatization
Lemmatization involves reducing words to their base or canonical form, known as the "lemma". Lemmatization aims to group togethe different inflected forms of a word so that they can be analyzed or processed as a single item.

##### Difference between stemming and Lemmatization
Stemming and lemmatization ar eboth text preprocessinng techniques in natural language processing(NLP) that aim to reduce words to their base forms, but they operate differently and have distinct characteristics.

| Aspect | Stemming | Lemmatization |
|--- | --- | --- |
| Output | Produces stems(may not be valid words) | Produces lemmas (valid words) |
| Linguistic Accuracy | Less acurate, may not always be meaningful | More accurate, ensures valid words |
| Context Sensitivity  | Lacks context awareness | Considers context and part of speech |
| Computational Complexity | Faster and computationally less intensive | Slower and computationally more intensive |
| Application | Information retrival, text classification | Machine translation, text analysis, language generation |


#### 7. Named Entity Recognition
Named Entity Recognition involves identifying and categorizing named enitites in text data. NER is essential for information extraction and helps in understanding the structure and meaning of textual content.

## Installation of the module
- Git clone
```
git clone 
```
- Install all the requirements
```
pip install -r requirements.txt
```


## References
1. [IBM](https://www.ibm.com/topics/natural-language-processing)
2. [Tutorials Point](https://www.tutorialspoint.com/artificial_intelligence/artificial_intelligence_natural_language_processing.htm)
3. [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/06/must-known-techniques-for-text-preprocessing-in-nlp/)
4. [Great Learning](https://www.mygreatlearning.com/blog/nltk-tutorial-with-python/)




