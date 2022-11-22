# PHYTON
Text plagiarism detection program. COH-PIAH


Exercise Completion course Introduction to computer science with Python - Plataforma Coursera (USP), Módulo 1 - Python

Prologue
In this last exercise in Part 1, we'll practice not only what we've seen so far in the course but also another important skill.
of a programmer: using and interacting with code written by others. Here, you will not implement your program from scratch.
You will start from an already started program and complete it. In fact, this is the most common case in the software industry,
where many developers work collaboratively on the same program.

Introduction
Manuel Estandarte is a tutor in the subject Introduction to Textual Production I at the University of Pasárgada (UPA). During the school term,
Manuel discovered that an epidemic of COH-PIAH was spreading across the UPA. This rare and highly contagious disease causes
infected individuals unwittingly produce texts very similar to those of other people. After submitting the first essay,
Manuel suspected that some students were suffering from COH-PIAH. Manuel, worried about the group's health, decided to look for a method to
identify cases of COH-PIAH. For this, he needs your help to develop a program that will help him identify infected students.

Authorship detection
Different people have different writing styles; for example, some people prefer shorter sentences, others prefer shorter sentences.
longer. Using various statistics of the text, it is possible to identify aspects that act as a “signature” of its author and,
therefore, it is possible to detect whether two given texts were written by the same person. That is, this “signature” can be used for detection
of plagiarism, forensic evidence or, in this case, to diagnose the serious illness COH-PIAH.

Linguistic traits
In this exercise we will use the following statistics to detect the disease:

*  Average Word Length: Simple average of the number of characters per word.

*  Type-Token Ratio: Number of different words used in a text divided by the total number of words.

*  Hapax Legomana Ratio: Number of words used once divided by the total number of words.

*  Average Sentence Length: Simple average of the number of characters per sentence.

*  Sentence complexity: Simple average of the number of sentences per sentence.

*  Average sentence length: Simple average of the number of characters per sentence.

Program operation
From the known signature of a COH-PIAH carrier, your program should receive several texts and calculate the values ​​of the different
linguistic traits of these texts to compare them with the given signature. The linguistic features your program should use are calculated
this way:

*   Average word length is the sum of the word lengths divided by the total number of words.
* Type-Token Ratio is the number of different words divided by the total number of words. For example, in the sentence "The cat hunted the mouse",
    we have 5 words in total (the, cat, hunted, the, mouse) but only 4 different ones (the, cat, hunted, mouse). In this sentence, the Type-Token relationship is worth
    5/5 = 0.8
* Hapax Legomana ratio is the number of words appearing only once divided by the total number of words. For example, in the sentence "The cat hunted the mouse",
    we have 5 words in total (the, cat, hunted, the, mouse) but only 3 that appear only once (cat, hunted, mouse). In this sentence, the relation Hapax Legomana
    worth 3/5 = 0.6
* Average sentence length is the sum of the number of characters in all sentences divided by the number of sentences (the characters separating a
    sentence of the other shall not be counted as part of the sentence).
* Sentence complexity is the total number of sentences divided by the number of sentences.

*  Average sentence length is the sum of the number of characters in each sentence divided by the number of sentences in the text (the characters that separate a sentence
    of the other shall not be counted as part of the sentence).

After calculating these values for each text, you must compare them with the signature provided for those infected with COH-PIAH. The degree of similarity
between two texts, a and b, is given by the formula:

       S_{ab} = ((∑{i=1 6}) * ∣∣f_{i,a} - f_{i,b}∣∣) / 6

*  S_{ab} is the degree of similarity between texts a and b;
* f_{i,a} is the value of each linguistic feature i in text a;
* f_{i,b} is the value of each linguistic feature i in text b;


In our case, the text b is not known, but we have the corresponding signature: the signature of a student infected with COH-PIAH. That is, we know the value of
f_{i,b} which is given as the input value of the program.

In case you are not used to mathematical notation, we can break this formula down as follows:

*   For each linguistic feature i (average word length, type-token ratio, etc.) we want the difference between the value obtained in each given text (a) and the
    typical text value of an infected person (b): f_{i, a} - f_{i, b}
* this difference takes the module (||...||), remember python's abs function.
* We add the results of the 6 linguistic features (∑(i=1 6))
* And finally we divide by 6 (x/6)

Note that the more similar a and b are, the smaller S_{ab} will be. For each text, you must calculate the degree of similarity with the bearer's signature
of COH-PIAH and, at the end, display which text was most likely written by an infected student (that is, the text with the signature most similar to the given signature).

Hint: don't worry about the implementation details of pre-made skeleton functions, like "separa_sentenca()", "separa_frase()" etc. not even with the settings
exact phrase and sentence. These functions already take care of that for you, and can be thought of as "black boxes": you can use them knowing what you get and what
that they return, but it is not necessary to know about their internal details. In addition to this being very common when programming in a team, using these functions you will
calculate as expected by the autocorrect.

Caution: The le_texts() function considers that a "text" is a line of text, that is, it is not possible to insert separate paragraphs. if you type
some "enter", the function will understand that you are starting a new text. Pay special attention to this if using "copy/paste" to insert the texts!
Note also that, in the similarity calculation, it is necessary to find the absolute value of each of the differences.

Signature Example
An important step for your program is to correctly calculate the signature of the texts. To test whether your function computes_signature()
is correct, here is an example of execution:


>text = "So he decided to go play with the Machine to also be emperor of the children of the cassava. But the three wedges laughed a lot and said that this
            gods was a fat old lie, that there was no god and that nobody doesn't play with the machine because it kills. The machine was not a god,
            nor did it possess the feminine badges the hero was so fond of. It was made by men. It moved with electricity with fire with water with wind
            with smoke, men taking advantage of the forces of nature. But alligator believed? not the hero! He got up on the bed and with a gesture, that one! well
            guaçu of disdain, tó! hitting his left forearm inside the other bent one, energetically moved his right wrist to three wedges and left.
            At that moment, they say, he invented the famously offending gesture: the pacova."
>calcula_assinatura(texto)
>[4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]


