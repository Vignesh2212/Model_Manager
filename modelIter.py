#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:10:31 2019

@author: subramanian
"""

class modelIter(object):
    def __init__(self):
        #All the initializations for the model
        self.modelDesc = ''
        self.modelType = 'Classification'
        self.modelTechnique = ''
        self._modelObjSet = False
        self._trainScoresSet = False
        self._TestScoresSet = False
        self._testScoresSet = False
        self.perfMetric = ''


    def setModelType(self,modelType):
        if any(modelType in types for types in ['Classification','Regression']):
            self.modelType = modelType
        else:
            print('Accepted values are Classification/Regression. Default - Classification')

    def setModelTechnique(self,modelTechnique):
        self.modelTechnique = modelTechnique

    def setModelObj(self,model):
        self.modelObj = model
        self._modelObjSet = True

    def setPerfMetric(self, perfMetric):
        self.perfMetric = perfMetric
        if self.modelType == 'Classification':
            if any(perfMetric in classPerf for class in ['accuracy_score',
                                                        'auc',
                                                        'average_precision_score',
                                                        'balanced_accuracy_score',
                                                        'brier_score_loss',
                                                        'cohen_kappa_score',
                                                        'f1_score',
                                                        'fbeta_score',
                                                        'hamming_loss',
                                                        'hinge_loss',
                                                        'jaccard_similarity_score',
                                                        'log_loss',
                                                        'matthews_corrcoef',
                                                        'precision_score',
                                                        'recall_score',
                                                        'roc_auc_score',
                                                        'zero_one_loss']):
                self.perfMetric = perfMetric
            else:
                print('Not recognized performance metric. Using default - auc')
                self.perfMetric = 'auc'
        #else:
            #Regression part to be coded later

    def plotROCCurve(self):
        #Code to plot ROC Curve of model on request

    def printConfusionMatrix(self):
        #Code to print confusion matrix on request

    def printClassificationReport(self):
        #Code to print classification report on request

    def setTrainScoresDF(self, trainScores, **varMap):
        self.trainScores = trainScores
        self._trainScoresSet = True
        self._Train_UID = varMap['Train_UID']
        self._Train_y_Actual = varMap['Train_y_Actual']
        self._Train_y_Predicted = varMap['Train_y_Predicted']
        if all(elem in trainScores[self._Train_y_Actual].unique() for elem in trainScores[self._Train_y_Predicted].unique()):
            self._trainPredType = 'Class'
        else:
            self._trainPredType = 'Prob'

    def setValidScoresDF(self,validScores, **varMap):
        self.validScores = validScores
        self._validScoresSet = True
        self._Valid_UID = varMap['Valid_UID']
        self._Valid_y_Actual = varMap['Valid_y_Actual']
        self._Valid_y_Predicted = varMap['Valid_y_Predicted']
        if all(elem in validScores[self._Valid_y_Actual].unique() for elem in validScores[self._Valid_y_Predicted].unique()):
            self._validPredType = 'Class'
        else:
            self._validPredType = 'Prob'

    def setTestScoresDF(self,testScores, **varMap):
        self.testScores = testScores
        self._testScoresSet = True
        self._Test_UID = varMap['Test_UID']
        self._Test_y_Actual = varMap['Test_y_Actual']
        self._Test_y_Predicted = varMap['Test_y_Predicted']
        if all(elem in testScores[self._Test_y_Actual].unique() for elem in testScores[self._Test_y_Predicted].unique()):
            self._testPredType = 'Class'
        else:
            self._testPredType = 'Prob'

    def computePerfMetricTrain(self):
        if _trainScoresSet:
            if self.perfMetric != '':
                #Code to compute performance metric for train
            else:
                print('Please set performance metric prior to computing')
        else:
            print('Please set the train DF prior to computing')

    def computePerfMetricValid(self):
          if _validScoresSet:
              if self.perfMetric != '':
                  #Code to compute performance metric for valid
              else:
                  print('Please set performance metric prior to computing')
          else:
              print('Please set the valid DF prior to computing')

    def computePerfMetricTest(self):
          if _testScoresSet:
              if self.perfMetric != '':
                  #Code to compute performance metric for test
                  #Thinking the return type shall be dict with all performance
                  #metrics needed accessible
                  #Possibly compute all possible performance metrics instead of
                  #Setting one
              else:
                  print('Please set performance metric prior to computing')
          else:
              print('Please set the test DF prior to computing')
