#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Clustering
==========
Cluster the data after extracting features from them
"""
from __future__ import division
from optparse import OptionParser
from pprint import pprint
from classifier import getAnalysisData
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as mpl
from scipy.spatial import distance
from nltk import cluster
from nltk.cluster import util
from nltk.cluster import api


def getUserInput():
    optionparser = OptionParser()


    optionparser.add_option('-d', '--dir', dest='directory')


    (option, args) = optionparser.parse_args()

    if not option.directory:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'dir' : option.directory }




def buildColumnData(data):
    """
        [{'avgRating': 4.051,
      'hasDeveloperEmail': True,
      'hasDeveloperWebsite': True,
      'hasPrivacy': True,
      'installRange': 30000000.0,
      'price': 0.0,
      'revlength': 10},
     'fair']
    """

    avgrating       = []
    hasDevEmail     = []
    hasDevWeb       = []
    hasPrivacy      = []
    install         = []
    price           = []
    revlength       = []
    label           = []

    for row in data:
        avgrating.append(row[0]['avgRating'])
        install.append(row[0]['installRange'])
        price.append(row[0]['price'])
        revlength.append(row[0]['revlength'])

        hasDevEmail.append(bool(row[0]['hasDeveloperEmail']))
        hasDevWeb.append(bool(row[0]['hasDeveloperWebsite']))
        hasPrivacy.append(bool(row[0]['hasPrivacy']))

        label.append(row[1])

    n_avgrating       = np.array(avgrating  )
    n_hasDevEmail     = np.array(hasDevEmail,   dtype="bool" )
    n_hasDevWeb       = np.array(hasDevWeb,     dtype="bool" )
    n_hasPrivacy      = np.array(hasPrivacy,    dtype="bool" )
    n_install         = np.array(install    )
    n_price           = np.array(price      )
    n_revlength       = np.array(revlength  )
    n_label           = np.array(label      )

    # pprint(n_hasPrivacy)
    return {
        'avgrating'      : avgrating,
        'hasDevEmail'    : hasDevEmail,
        'hasDevWeb'      : hasDevWeb,
        'hasPrivacy'     : hasPrivacy,
        'install'        : install,
        'price'          : price,
        'revlength'      : revlength,
        'label'          : label,
    }




def clusterer(data):
    pprint(data)


    clusterer = cluster.GAAClusterer(num_clusters=4)

    vectors = []
    for row in data:
        for k, v in data[0][0].iteritems():
            vectors.append(np.array(v))

    clusters = clusterer.cluster(vectors, True)

    print 'Clusterer:', clusterer
    print 'Clustered:', vectors
    print 'As:', clusters
    clusterer.dendrogram().show()



def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)

    dataframe = buildColumnData(data)

    clusterer(dataframe)







if __name__ == '__main__':
    main()