#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:57:24 2019

@author: subramanian
"""

import pandas as pd
import os


class modelManager(object):
    def __init__(self):
        #Set init values. 
        self.overWrite = False
        self.modelName = "Model"
        self.modelList = []
        
    #Set project folder for storing bivariate pdfs to avoid clutter
    def setCurrentDir(self,newDir):
        self.oldDir = os.getcwd()
        os.chdir(newDir)

    #Use this method to revert working directory to old one, if available
    def revertDir(self):
        if self.oldDir != "":
            os.chdir(self.oldDir)
        else:
            print("No old working directory available to revert to") 
            
    #By default, all the model versions overwrite protected.
    #call this constructor to overwrite any dataset.
    #Once a dataset is overwritten, it is overwrite protected again
    def setOverWrite(self):
        self.overWrite = True
        print("Project overwrite protections is disabled")
        
    def resetOverWrite(self):
        self.overWrite = False
        print("Project overwrite protection is enabled")
    
    def createNewModel(self, modelName):
        if os.path.isfile(modelName + 'BaseFile.pkl'):
            if self.overWrite:
                self._resetExistingModel()
                self.modelName = modelName
                self.overWrite = False
            else:
                print("Over Write protected. call setOverWrite method to overwrite existing project")
        else:
            self._resetNewModel()
            self.modelName = modelName
            
    def _resetExistingModel(self):
        #All the methods to reset existing model project into a new one
        os.remove(modelName + 'BaseFile.pkl')
        
    def _resetNewModel(self):
        #All the methods to create structure for new model project
        
    def addNewModel(self, modelObj):
        
        
        
    
    