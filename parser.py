'''This file read the xml file from the corpus using sax parser'''
import xml.sax
import re
from collections import defaultdict
from Stemmer import Stemmer

docID = dict()

class PageHandler(xml.sax.ContentHandler):
	flag = 1
	idf = 1
	def __init__(self):
		self.currentData = ""
		self.title = ""
		self.id = ""
		self.text = ""

	def startElement(self, tag, attributes):
		self.currentData = tag
		if self.currentData == "page":
			PageHandler.flag = 1
			PageHandler.idf = 1

	def endElement(self, tag):
		if self.currentData == "id" and PageHandler.idf == 1:
			print self.id
			PageHandler.idf = 0
		elif self.currentData == "title":
			print self.title
		elif self.currentData == "text":
			#print self.text
			self.text = ""


	def characters(self, content):
		if self.currentData == "id" and PageHandler.flag == 1:
			self.id = content.encode('utf-8')
			PageHandler.flag = 0
		elif self.currentData == "title":
			self.title = content.encode('utf-8')
		elif self.currentData == "text":
			self.text += content.encode('utf-8')

if( __name__ == "__main__"):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	Handler = PageHandler()
	parser.setContentHandler( Handler )
	parser.parse("wiki-search-small.xml")
	print docID
