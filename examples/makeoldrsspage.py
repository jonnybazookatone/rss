Usage = """ """

import glob
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

	RSSOldWebpage = webpage()

	# Load the RSS feed from file
	RSSfeeds = glob.glob('/home/user/workspace/journaltools/*grb*.rss')
	print "Found feeds: %s" % (RSSfeeds)
	
	for RSSfilename in RSSfeeds:

		RSS = rssfeed()
		RSS.loadFeedFromFile(RSSfilename)
		print RSS._feed
		
		for paper in RSS._feed:
			RSSOldWebpage.addBody("<h3><b>%s</b></h3>" % paper["title"])
			RSSOldWebpage.addBody(paper["summary"])
			RSSOldWebpage.addBody(paper["link"], link=True)
			RSSOldWebpage.addBody("<hr><hr>")
			RSSOldWebpage.addBody("\n")
	
	RSSOldWebpage.setTitle("arXiv feeds for: %s" % (RSS._date))
	RSSOldWebpage.buildPage("oldfeeds_grb.html")

	savename = "arxiv_feed_%s.rss" % ("grbold")
	RSS.writeFeedToFile(savename)

if __name__ == "__main__":

		main()
