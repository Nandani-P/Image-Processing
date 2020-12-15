Code is taken from https://inst.eecs.berkeley.edu//~cs188/sp11/projects/classification/classification.html

Python 2.7.18 required to run the code, please refer the below link if needed
https://www.python.org/downloads/

Files attached: -

1. perceptron.py
2. naiveBayes.py
3. dataClassifier.py
4. zip file(data)
5. samples.py
6. util.py
7. commands.txt
8. classificationMethod.py
9. mira.py
10. mostFrequent.py

We have worked on three files:
1. perceptron.py - Implemented a logic of train() function
2. naiveBayes.py - Implemented a logic of trainAndTune() and calculateLogJointProbabilities() functions
3. dataClassifier.py - Implemented enhancedFeatureExtractorFace() and enhancedFeatureExtractorDigit() functions

Add options for command to run with various configurations: -
'-c', '--classifier', choices= ['naiveBayes', 'perceptron', 'mira'], default='mostFrequent'
'-d', '--data', choices=['digits', 'faces'], default='digits'
'-t', '--training', default=100, type="int"
'-f', '--features', default=False, action="store_true"
'-i', '--iterations', default=3, type="int"
'-s', '--test',default=TEST_SET_SIZE, type="int"


Type in the following commands to run on command prompt/powershell

For Windows: use py -2.7 instead of python 

# To run naiveBayes on digit and face data

python dataClassifier.py -c naiveBayes
python dataClassifier.py -c naiveBayes -d faces  

# To run naiveBayes with the advanced feature (-f) and testing data of 1000 (-t 1000) 

python dataClassifier.py  -c naiveBayes -d digits -f -t 1000
python dataClassifier.py  -c naiveBayes -d faces -f 

# To run perceptron algo on digit and face data 

python dataClassifier.py -c perceptron 
python dataClassifier.py -c perceptron -d faces

# To run perceptron algo with advanced feature

python dataClassifier.py -c perceptron -f 
python dataClassifier.py -c perceptron -d faces -f

# To run mira
python dataClassifier.py -c mira
  

