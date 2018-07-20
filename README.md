# sner
Python wrapper around the Stanford Named Entity Recognizer (NER) Server and the Part-Of-Speech (POS) Tagger Server.

[![PyPI version](https://badge.fury.io/py/sner.svg)](https://badge.fury.io/py/sner)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/caihaoyu/sner/master/LICENSE)

# Stanford Named Entity Recognizer Project

* [Home Page](https://nlp.stanford.edu/software/CRF-NER.shtml)
* [Running NER as a Server](https://nlp.stanford.edu/software/crf-faq.shtml#cc)

# Stanford Part-Of-Speech Tagger Project

* [Home Page](https://nlp.stanford.edu/software/tagger.shtml)
* [Running POS as a Server](https://nlp.stanford.edu/software/pos-tagger-faq.html#e)

# Installation
```bash
pip install sner
```
or

```bash
python setup install
```

# Start
## NER Client
Run the following commands to start the NER server

```bash
cd your_stanford_ner_dir
java -Djava.ext.dirs=./lib -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -port 9199 -loadClassifier ./classifiers/english.all.3class.distsim.crf.ser.gz  -tokenizerFactory edu.stanford.nlp.process.WhitespaceTokenizer -tokenizerOptions tokenizeNLs=false
```
Use the following in Python to access the NER server

```python
from sner import Ner

test_string = "Alice went to the Museum of Natural History."
tagger = Ner(host='localhost',port=9199)
print(tagger.get_entities(test_string))

```
The following results are expected

```python
[('Alice', 'PERSON'),
 ('went', 'O'),
 ('to', 'O'),
 ('the', 'O'),
 ('Museum', 'ORGANIZATION'),
 ('of', 'ORGANIZATION'),
 ('Natural', 'ORGANIZATION'),
 ('History', 'ORGANIZATION'),
 ('.', 'O')]
```

## POS Client
Run the following commands to start the POS server

```bash
cd your_stanford_pos_dir
java -cp stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -port 9198 -model models/english-bidirectional-distsim.tagger
```
Use the following in Python to access the POS server

```python
from sner import POSClient

test_string = "Alice went to the Museum of Natural History."
tagger = POSClient(host='localhost', port=9198)
print(tagger.tag(test_string))
```
The following results are expected

```python
[('Alice', 'NNP'),
 ('went', 'VBD'),
 ('to', 'TO'),
 ('the', 'DT'),
 ('Museum', 'NNP'),
 ('of', 'IN'),
 ('Natural', 'NNP'),
 ('History', 'NN'),
 ('.', '.')]
```
