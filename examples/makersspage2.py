Usage = """ """

from rss.rssclass import rssfeed
from pyweb.webclass import webpage

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

def main():

	RSS = rssfeed()
	RSSWebpage = webpage()

	RSS.setPatterns(["star formation", "star-formation", "Star formation", "Star Formation", "Star-Formation", "star-Formation", "starformation", "Starformation"])

	#RSS.getPapersTitle()
	RSS.getPapersSummary()
	Papers = RSS._summary_papers
	#RSS.getPapersKeyword()
	#Papers = RSS._keyword_papers

	for paper in Papers:
		RSSWebpage.addBody("<h3><b>%s</b></h3>" % paper["title"])
		RSSWebpage.addBody(paper["summary"])
		RSSWebpage.addBody(paper["author"])
		RSSWebpage.addBody(paper["link"], link=True)
		RSSWebpage.addBody("<hr><hr>")
		RSSWebpage.addBody("\n")

	if len(Papers)==0:
		print "Nothing Found"
		RSSWebpage.addBody("Nothing was found with pattern: %s" % (RSS._patterns))
	
	RSSWebpage.setTitle("arXiv feeds for: %s" % (RSS._date))
	RSSWebpage.buildPage("newfeeds_sfr.html")

	savename = "arxiv_feed_%s_%s.rss" % ("sfr", RSS._date)
	RSS.writeFeedToFile(savename)

if __name__ == "__main__":

		main()
