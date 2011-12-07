#!/usr/bin/python

Usage = """RSS feed class to select papers of a specific pattern from e.g., arXiv."""

import feedparser, re, datetime, pickle

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

class rssfeed(object):
		
	def __init__(self, weburl="http://arxiv.org/rss/astro-ph", patterns=["gamma-ray", "Gamma-ray", "Gamma-Ray", "burst"]):
		self._weburl = weburl
		self._patterns = patterns
		self._title_papers = []
		self._summary_papers = []
		self._keyword_papers = []
		self._date = datetime.date.today()
		self._feed = []

	def setPatterns(self, patterns):
		if type(patterns) != type([]):
			print "Please set as list"
		else:
			self._patterns = patterns

	def writeFeedToFile(self, outname):
		# save the dictionary to file
		if self._summary_papers != []:
			Papers = [i for i in self._summary_papers]
		else:
			Papers = []

		if self._keyword_papers != []:
			for i in self._keyword_papers:
				Papers.append(i)

		try:
			outputfile = open(outname, "w")
			suc = pickle.dump(Papers, outputfile)
			outputfile.close()
		except:
			print "Error saving feed."
			#print suc
			return(2)
	
	def loadFeedFromFile(self, inname):

		try:
			inputfile = open(inname, "r")
			feed = pickle.load(inputfile)
			inputfile.close()
		except:
			print "Error loading feed."
			return(1)

		self._feed = feed

	def getPapersTitle(self):
		
		# load the feed
	        feed = feedparser.parse(self._weburl)
	        titleofinterest = []

		# collect items that fit the patterns selected
	        for item in feed["items"]:
	                title = item["title"]

	                for pattern in self._patterns:
	                        if re.search(pattern, title):
	                                titleofinterest.append(item)

		self._title_papers = titleofinterest


	def getPapersSummary(self):

		# load the feed
                feed = feedparser.parse(self._weburl)
		summaryofinterest = []

		# collect the items that fit the patterns selected
		for item in feed["items"]:
			summary = item["summary"]
			
			for pattern in self._patterns:
				if re.search(pattern, summary):
					summaryofinterest.append(item)

		self._summary_papers = summaryofinterest


	# Redundant for arXiv
	def getPapersKeyword(self):

		# load the feed
		feed = feedparser.parse(self._weburl)
		keywordofinterest = []

		# collect the items that fit the patterns selected
		for item in feed["items"]:
			keyword = item["keywords"]
		
			for pattern in self._patterns:
				if re.search(pattern, keyword):
					keywordofinterest.append(item)

		self._keyword_papers = keywordofinterest

if __name__ == "__main__":

	print Usage	
