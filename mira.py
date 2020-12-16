# mira.py
# -------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

# Mira implementation
import util
PRINT = True

class MiraClassifier:
  """
  Mira classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__( self, legalLabels, max_iterations):
    self.legalLabels = legalLabels
    self.type = "mira"
    self.automaticTuning = False 
    self.C = 0.001
    self.legalLabels = legalLabels
    self.max_iterations = max_iterations
    self.initializeWeightsToZero()

  def initializeWeightsToZero(self):
    "Resets the weights of each label to zero vectors" 
    self.weights = {}
    for label in self.legalLabels:
      self.weights[label] = util.Counter() # this is the data-structure you should use
  
  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    "Outside shell to call your method. Do not modify this method."  
      
    self.features = trainingData[0].keys() # this could be useful for your code later...
    
    if (self.automaticTuning):
        Cgrid = [0.002, 0.004, 0.008]
    else:
        Cgrid = [self.C]
        
    return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
    """
    This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid, 
    then store the weights that give the best accuracy on the validationData.
    
    Use the provided self.weights[label] data structure so that 
    the classify method works correctly. Also, recall that a
    datum is a counter from features to values for those features
    representing a vector of values.
    """
    "*** YOUR CODE HERE ***"
    self.features = trainingData[0].keys()

    # Initialise weights for every feature of a label
    for label in self.legalLabels:

    # Initialize the weights (can update the range for testing)
      for feat in self.features:
        self.weights[label][feat] = random.randint(1,2)
      self.weights[label]['w0'] = random.randint(1,2)
      

    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      for i in range(len(trainingData)):
        "*** YOUR CODE HERE ***"
        if len(self.legalLabels) == 2:
          # face case
          label = 1

          f = self.weights[label]['w0'] 

          for feat in self.features:
            datum = trainingData[i]
                    
            #number of pixels in a feature
            numOfPixels = datum[feat]

            f = f + numOfPixels * self.weights[label][feat]

          # face condition 
          if (f >= 0 and trainingLabels[i] == label):
            continue;

          elif (f < 0 and trainingLabels[i] != label):
            continue;

          elif (f >= 0 and trainingLabels[i] != label):
            self.weights[label]['w0'] = self.weights[label]['w0'] - 1
            for feat in self.features:
              self.weights[label][feat] = self.weights[label][feat] - trainingData[i][feat]

          elif (f < 0 and trainingLabels[i] != label):
            self.weights[label]['w0'] = self.weights[label]['w0'] + 1
            for feat in self.features:
              self.weights[label][feat] = self.weights[label][feat] + trainingData[i][feat]

        # Digit condition
        else:
          # Initialize fList which stores perceptron for every digit (0 - 9)
          fList = util.Counter()
          for label in self.legalLabels:

            f = self.weights[label]['w0'] 

            for feat in self.features:
              datum = trainingData[i]
                                   
              #number of pixels in a feature
              numOfPixels = datum[feat]

              f = f + numOfPixels * self.weights[label][feat]
            fList[label] = f

          # check max and update weights
          predictedKey = fList.argMax()

          if predictedKey != trainingLabels[i]:
            for feat in self.features:
              datum = trainingData[i]
                                   
              #number of pixels in a feature
              numOfPixels = datum[feat]

              self.weights[predictedKey][feat] = self.weights[predictedKey][feat] - numOfPixels
              self.weights[trainingLabels[i]][feat] = self.weights[trainingLabels[i]][feat] + numOfPixels

            self.weights[predictedKey]["w0"] = self.weights[predictedKey]["w0"] - 1
            self.weights[trainingLabels[i]]["w0"] = self.weights[trainingLabels[i]]["w0"] + 1

    util.raiseNotDefined()

  def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    
    Recall that a datum is a util.counter... 
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
    return guesses

  
  def findHighOddsFeatures(self, label1, label2):
    """
    Returns a list of the 100 features with the greatest difference in feature values
                     w_label1 - w_label2

    """
    featuresOdds = []

    "*** YOUR CODE HERE ***"

    return featuresOdds

