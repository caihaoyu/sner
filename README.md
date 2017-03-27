# sner
The Python interface to the Stanford Named Entity Recognizer Server.
# Installation
```bash
pip install sner
```
or

```bash
python setup install
```

# start

run these commands to start java server

```bash
cd your_stanford_ner_dir
java  -mx2g -cp -Djava.ext.dirs=./lib -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -port 9199 -loadClassifier ./classifiers/english.all.3class.distsim.crf.ser.gz
```
Then the sner can worked like this

```python
from sner import Ner

test_string = "Alice went to the Museum of Natural History."
tagger = Ner(host='localhost',port=9199)
print(tagger.get_entities(test_string))
```
result is

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




