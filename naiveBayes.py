# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math
# import sys

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__(self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter, ** use it in your train method **
    self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **
    self.legalLabelProbablity = {}
    self.totalLabelCounter = util.Counter()

  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """  
      
    # might be useful in your code later...
    # this is a list of all features in the training set.
    self.features = list(set([ f for datum in trainingData for f in datum.keys() ]));
    
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
    else:
        kgrid = [self.k]
        
    self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
      
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Trains the classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter 
    that gives the best accuracy on the held-out validationData.
    
    trainingData and validationData are lists of feature Counters.  The corresponding
    label lists contain the correct label for each datum.
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """

    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # 1 = face , 0 = no-face
    # count total training labels - for each legal value

    for legalLabel in self.legalLabels:
        for trainingLabel in trainingLabels:
            if (trainingLabel == legalLabel):
                self.totalLabelCounter[legalLabel] += 1
            
    self.totalLabelCounter.normalize()

    # x = 0
    # find probablity for each feature's option - for each type of legal value
    for legalLabel in self.legalLabels:
        
        featureProbablityTable = {}

        for feat in self.features:
            # feat can be (x,y)
            featureOptionsCounter = util.Counter()
            # x = 0

            # featureOptionsCounter[0] += 1
            # featureOptionsCounter[0] += 1
            # featureOptionsCounter.normalize()
            # posteriorrint("featureOptionsCounter ", featureOptionsCounter[0])
            # print("featureOptionsCounter totalCount", featureOptionsCounter.totalCount())

            # featureOptions = []
            for i in range(len(trainingLabels)):
                if (trainingLabels[i] == legalLabel):
                    datum = trainingData[i]
                    # print "label ", legalLabel
                    # print "datum[feat] ", datum[feat]
                    columnOption = datum[feat]

                    # if (columnOption == 0){
                    #     featureOptionsCounter[0] += 1
                    # } else (columnOption == 1){
                    #     featureOptionsCounter[1] += 1
                    # }

                    featureOptionsCounter[columnOption] += 1
                    # x = x + 1
                    # print("featureOptionsCounter totalCount", featureOptionsCounter.totalCount())

            # if (x>1):
            #     print "x", x
            

            featureOptionsCounter.normalize()
            # print "featureOptionsCounter totalCount", featureOptionsCounter.totalCount()
            # print("featureOptionsCounter[0]", featureOptionsCounter[0])
            featureProbablityTable[feat] = featureOptionsCounter

        self.legalLabelProbablity[legalLabel] = featureProbablityTable
    # for ww in self.featureProbablityTable.keys():
        # print ww.totalCount()
        # print self.featureProbablityTable[ww][0]
        # sys.stdout.write(self.featureProbablityTable[ww].totalCount())


    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    You shouldn't modify this method.
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculateLogJointProbabilities(self, datum):
    """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.    
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """
    logJoint = util.Counter()
    
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    
    for legalLabel in self.legalLabels:
        xProb = 1
        for feat in self.features:
            currentFeatureVal = datum[feat]
            featureProbablityTable = self.legalLabelProbablity[legalLabel]
            featureOptionsRow = featureProbablityTable[feat]
            if featureOptionsRow[currentFeatureVal] == 0 :
                xProb = xProb * 0.001                
            else:
                xProb = xProb * featureOptionsRow[currentFeatureVal]

        # add prior probablity
        xProb = xProb * self.totalLabelCounter[legalLabel]

        logJoint[legalLabel] = xProb

    # logJoint['0'] = final-probabilty
    # logJoint['1'] = final-probabilty-face

    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


    return logJoint
  
  def findHighOddsFeatures(self, label1, label2):
    """
    Returns the 100 best features for the odds ratio:
            P(feature=1 | label1)/P(feature=1 | label2) 
    
    Note: you may find 'self.features' a useful way to loop through all possible features
    """
    featuresOdds = []
       
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    return featuresOdds
    

    
      
