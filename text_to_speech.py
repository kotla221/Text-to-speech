# -*- coding: utf-8 -*-
"""text to speech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kQTAaXeFBtjUEEQ6GCYAEcQ1VH8gdNa8
"""

import nltk

import nltk.corpus

"""Tokenization"""

from nltk.tokenize import word_tokenize

chess = "Samay Raina is the best chess streamer in the world"

chess

nltk.download('punkt')

word_tokenize(chess)

#sentence tokenizer
from nltk.tokenize import sent_tokenize

chess2= "Samay is the best chess streamer in the world.Sagar Shah is the best coaach in the world"

sent_tokenize(chess2)

#checking number of tokens
len(word_tokenize(chess))

astronaut="Can anybody hear me or am I talking to myself?My mind is running crzay"

astronaut_token=(word_tokenize(astronaut))

list(nltk.bigrams(astronaut_token))

list(nltk.trigrams(astronaut_token))

list(nltk.ngrams(astronaut_token,5))

"""STEMMING"""



from nltk.stem import PorterStemmer

my_stem=PorterStemmer()

my_stem.stem("eating")

my_stem.stem("fucking")

"""POS_TAGGING"""

tom="Tom Hanks is the best actor in the world"

tom_token=word_tokenize(tom)

nltk.pos_tag(tom_token)

nltk.download('averaged_perceptron_tagger')

"""Named entity recognition"""

from nltk import ne_chunk

prime="Narendra Modi is the Prime Minister Of India"

prime_token=word_tokenize(prime)

prime_pos=nltk.pos_tag(prime_token)

print(ne_chunk(prime_pos))

nltk.download('maxent_ne_chunker')

nltk.download('words')

!pip install gTTS

from gtts import gTTS
from IPython.display import Audio
tts=gTTS('Sareee Manchidi')
tts.save('1.wav')
sound_file='1.wav'
Audio(sound_file, autoplay=True)

