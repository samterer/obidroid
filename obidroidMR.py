from mrjob.job import MRJob
from sentClassifier import sentClassify
import os,re
from cPickle import load



class ObidroidReview(MRJob):
	# INPUT_PROTOCOL = RawValueProtocol

	@staticmethod
	def getFeatures(rev):
		

		revsent = sentClassify(rev)
		revLength = len(rev)
		cap = len(re.findall('([A-Z])+\w',rev))
		exclam = len(re.findall('!',rev))
		return [revsent, [revsent,revLength,cap,exclam]]




	def getRecord(self, _, record): #Mapper 1
		record = record.split(',')

		appid = record[0]
		features = ObidroidReview.getFeatures(record[1])


		yield appid, features


	def performAction(self,appid,appfeature): #Reducer 1
		yield appid, list(appfeature)




	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]



if __name__ == '__main__':
    ObidroidReview.run()