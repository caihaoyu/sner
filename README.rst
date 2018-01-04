sner
====

Python wrapper around the Stanford Named Entity Recognizer (NER) Server and the Part-Of-Speech (POS) Tagger Server.

Stanford Named Entity Recognizer Project
===================

-  `Home Page <https://nlp.stanford.edu/software/CRF-NER.shtml>`__

-  `NER Server <https://nlp.stanford.edu/software/crf-faq.shtml#cc>`__

Stanford Part-Of-Speech Tagger Project
===================

-  `Home Page <https://nlp.stanford.edu/software/CRF-NER.shtml>`__

-  `POS Server <https://nlp.stanford.edu/software/crf-faq.shtml#cc>`__

Installation
============

.. code:: bash

    pip install sner

or

.. code:: bash

    python setup install

Start
=====

NER
-----
Run the following commands to start the NER server

.. code:: bash

    cd your_stanford_ner_dir
    java -Djava.ext.dirs=./lib -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -port 9199 -loadClassifier ./classifiers/english.all.3class.distsim.crf.ser.gz

Use the following in Python to access the NER server

.. code:: python

    from sner import NERClient

    test_string = "Alice went to the Museum of Natural History."
    tagger = NERClient(host='localhost',port=9199)
    print(tagger.tag(test_string))

The following results are expected

.. code:: python

    [('Alice', 'PERSON'),
     ('went', 'O'),
     ('to', 'O'),
     ('the', 'O'),
     ('Museum', 'ORGANIZATION'),
     ('of', 'ORGANIZATION'),
     ('Natural', 'ORGANIZATION'),
     ('History', 'ORGANIZATION'),
     ('.', 'O')]

POS
-----
Run the following commands to start the POS server

.. code:: bash

    cd your_stanford_pos_dir
    java -cp stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -port 9198 -model models/english-bidirectional-distsim.tagger

Use the following in Python to access the POS server

.. code:: python

    from sner import POSClient

    test_string = "Alice went to the Museum of Natural History."
    tagger = POSClient(host='localhost',port=9199)
    print(tagger.tag(test_string))

The following results are expected

.. code:: python

    [('Alice', 'NNP'),
     ('went', 'VBD'),
     ('to', 'TO'),
     ('the', 'DT'),
     ('Museum', 'NNP'),
     ('of', 'IN'),
     ('Natural', 'NNP'),
     ('History', 'NN'),
     ('.', '.')]
