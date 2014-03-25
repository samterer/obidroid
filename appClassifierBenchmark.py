#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Benchmark different classifiers

Classifiers tried:

- Naive Bayes
- Random Forest
- SVM
    - linear
    - kernelized
"""

from __future__ import division
from optparse import OptionParser
import pandas as pd
import numpy as np
from sklearn import svm

def getUserInput():
    """
    Get User Input
    """
    optionparser = OptionParser()

    optionparser.add_option('-m', '--model', dest='model', default="all")
    optionparser.add_option('-f', '--file', dest='file')


    (option, args) = optionparser.parse_args()

    if not option.file:
        return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')

    return { 'model' : option.model, 'file': option.file }





def loadAppData(datafile):
    """
    Data File added
    {
        'fair' : False,
        'unfair': True
    }
    """
    df = pd.read_csv(datafile)

    ## Remove the unnamed column as not sure
    cols = set(df.columns)
    cols.remove('Unnamed: 7')
    df = df[list(cols)]

    ## Convert appLabel to boolean: True for 'unfair'
    df['appLabel'] = df['appLabel'].map(lambda x: x=='unfair')

    return df


def trimDf(df):
    """
    Trim the dataframe provided
    Remove features that we don't think are helping
    """
    cols = set(df.columns)

    cols.remove('exclamationCount') # bug in our feature extraction code
    cols.remove('price') # considered only free apps
    cols.remove('appName') # removing appNames

    return df[list(cols)]




def prepareClassifier(df):
    """
    Classify the apps
    """


    def classify(cDf):
        """
        Given the dataframe combined with equal fair and unfair apps,
        classify them
        """
        cDf = cDf.reindex(np.random.permutation(cDf.index)) # shuffle the dataframe
        featCols = set(cDf.columns)
        featCols.remove('appLabel')

        X = cDf[list(featCols)]
        Y = cDf['appLabel']


        svc = svm.SVC() # initiating the SVM based classifier
        Y_pred_svc = svc.fit(Y[:36], X).predict(Y[37:46]) # train on first 36 and test on last 10

        print "SVM classifier Prediction Errors: \t\t%5d" % (Y_pred_svc != Y).sum()





    fairDf = df[df['appLabel'] == False]
    unfairDf = df[df['appLabel'] == True]

    # print "fairDf", fairDf.values

    # print "unfairDf", unfairDf.values

    # calculate total possible splits of fair data frame relatie to
    # size of unfair dataframe
    splits = len(fairDf) // len(unfairDf)

    for i in range(splits):
        clDf = fairDf[i : i+len(unfairDf)].append(unfairDf)

        # print fairDf.values, unfairDf.values
        print "Classifying %d th split of fair apps with unfair app" % (i)
        print "-" * 79
        classify(clDf)
        print "\n\n"







def main():
    print __doc__

    userInput = getUserInput()
    appDf = loadAppData(userInput['file'])
    appDf = trimDf(appDf)

    prepareClassifier(appDf)



    print "Sample Data"
    print "-" * 79
    print appDf.head()

    print
    print "Data Columns"
    print "-" * 79
    for (i,col) in enumerate(appDf.columns):
        print "%2s %30s %10s" % (i,col, appDf[col].dtype)




if __name__ == '__main__':
    main()
