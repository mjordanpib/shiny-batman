import urllib
import re

class URL:
	"""Basic webpage, identified by url. Return the data of the webpage"""
	def __init__(self, url):
		self.url = url

	def openURL(self):
		opener = urllib.FancyURLopener({})	
		self.url = opener.open(self.url)
		self.data = self.url.read()

	def readURL(self):
		return self.data

def checkNode(lastNode, currentNode):
	if currentNode > lastNode:
		updateNone(currentNode)
		print "Hay un nuevo post"
	else:
		updateNone(lastNode)
		print "No hay nuevos post"

def updateNone(node):
	nodeText = open("node.txt", "w")
	nodeText.write(node)
	nodeText.close
	return node

google = URL("http://ingenieroaburrido.com")
google.openURL()

nodeURL = str(google.readURL())

nodeObject = re.search("<div id=\"node-(.*?)\" ", nodeURL).group(1)
nodeText = open("node.txt").read()

checkNode(nodeText,nodeObject)
