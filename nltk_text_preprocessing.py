"""
NLTK TEXT PREPROCESSING MODULE
"""

# import nltk
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

# tokenize words
def tokenize_words(text):
    """
    Tokenizes the input text into words using NLTK's word_tokenize function. 

    Args:
        text (str): The input text to be tokenized.
    
    Returns:
        list of str: A list of tokens (words) extracted from the input text.
    """
    tokens = word_tokenize(text)
    return tokens


# tokenize words
def tokenize_sentence(text):
    """
    Tokenizes the input text into sentences using NLTK's sent_tokenize function. 

    Args:
        text (str): The input text to be tokenized into sentences.
    
    Returns:
        list of str: A list of sentences extracted from the input text.
    """
    tokens = sent_tokenize(text)
    return tokens


# lower casing
def lowercase_text(text):
    """
    Converts the input text to lowercase.

    Args:
        text (str): The input text to be converted to lowercase.

    Returns:
        str: The input text converted to lowercase.
    """
    lowercase = text.lower()
    return lowercase

# stopwords removal
def remove_stopwords(text):
    """
    Remove stopwords from the input texxt using NLTK's stopwords list.

    Args:
        text (str): The input text from which stopwords will be removed.

    Returns:
        str: The input text with stopwords removed.
    """
    # Tokenize the text
    words = nltk.word_tokenize(text)
    
    # Remove Stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Reconstruct the text
    cleaned_text = ' '.join(filtered_words)
    return cleaned_text


# POS tagging
def pos_tag_text(text):
    """
    Performs Part-of-Speech(POS) tagging on the input text using NLTK'S pos_tag functions.

    Args:
        text (str): The input text to be POS tagged.

    Returns:
        list of tuple: A list of (word, POS tag) pairs for each word in the input text.
    """
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    return pos_tags
    
# word lemmatization
def lemmatize_text(text):
    """
    Lemmatizes the input text using NLTK's WordNetLemmatizer.

    Args:
        text (str): The input text to be lemmatized.

    Returns:
        str: The lemmatized text.
    """
    lemmatizer = WordNetLemmatizer()
    
    # tokenize the text
    words = nltk.word_tokenize(text)
    
    # deterine the part of speech tags to WordNet tags
    pos_tags = nltk.pos_tag(words)
    
    # Map part of speech tags to WordNet tags
    def get_wordnet_pos(tag):
        tag = tag[0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag,wordnet.NOUN)
    
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    lemmatized_text = ' '.join(lemmatized_words)
    
    return lemmatized_text


# stemming
def stem_text(text):
    """
    Stems the words in the input text using NLTK's porter Stemmer.

    Args:
        text (str): The input text whose words will be stemmed.

    Returns:
        str: The input text with words stemmed.
    """
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_text = ' '.join(stemmed_words)
    return stemmed_text
    
 
# named entity identifier 
def named_entity_recognition(text):
    """
    Performs Named Entity Recognition (NER) on the input text using NLTK's ne_chunk function.

    Args:
        text (str): The input text in which named entities will be recognized.

    Returns:
        nltk.Tree: A tree structure containing named entities and their labels.

    """
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    named_entities = nltk.ne_chunk(pos_tags)
    return named_entities

  
if __name__ == "__main__":
    # tokenize  words
    sample_text = "Oh man, this is pretty cool. We will do more such things."
    words = tokenize_words(sample_text)
    print("Original Text:", sample_text)
    print("\n**Word tokens**\n", words)
    
    # tokenize sentences
    text = "This is the first sentence. And here is the second one!"
    sentences = sent_tokenize(text)
    print("Original Text:", text)
    print("Sentences:",sentences)
    
    # lowercasing
    text = "This Is An Example Sentence."
    lowercase = lowercase_text(text)
    print("Original Text:",text)
    print("Lowercase Text:",lowercase)
    
    # removing stopwords
    text = "This is an example sentence with some stopwords."
    cleaned_text = remove_stopwords(text)
    print("Original text:", text)
    print("Text with Stopwords Removed:", cleaned_text)
    
    # POS tagging
    text = "I am running in the park"
    pos_tags = pos_tag_text(text)
    print("Original Text:", text)
    print("POS Tags:", pos_tags)
    
    # lemmatization
    text = "I am running in the park"
    lemmatized_text = lemmatize_text(text)
    print("Original Text:", text)
    print("Lemmatized Text:", lemmatized_text)
    
    # Stemming
    text = "running quickly in the park"
    stemmed_text = stem_text(text)
    print("Original Text:", text)
    print("Stemmed Text:", stemmed_text)
    
    # Named Entity Identifer
    text = "Apple Inc. is headquartered in Cupertino, California."
    named_entities = named_entity_recognition(text)
    print("Original Text:", text)
    print("Named Entities:")
    print(named_entities)
     