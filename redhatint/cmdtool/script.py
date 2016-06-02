import click
from HTMLParser import HTMLParser
import hashlib
import pycountry
from textblob import TextBlob
import os
from sgmllib import SGMLParser
import htmlentitydefs

""" 
     	Usage:
     	
     	1. Install the script by pointing to the diretory containing this script by typing this cmd in terminal
     		$ pip install --editable .
     	2.To execute extract-command type in terminal
     		$ extract-text
     	3.To execute generate-resource command type (leaving the --language option chooses the deafult 
     																					translation lang hindi)
     		$ generate-resource --language nameoflang
     		Eg- generate-resource --language hindi
     	4.To execute display-html command type (leaving the --language option chooses the deafult 
     																					translation lang hindi)
     		$ display-html --language nameoflang
     		Eg- diasplay-html --language hindi    """

@click.command()
def extract_text():

	curr_path = os.path.dirname(os.path.abspath(__file__))
	html_doc = open(curr_path + '/example.html','r').read()
	result_file = open(curr_path + '/example.properties','w')
	
	class BaseHTMLProcessor(SGMLParser):
		def handle_data(self, data):
			#if "\n" not in data:
				key = hashlib.sha224(data).hexdigest()
				value = data
				ans = key + "=" + data + "\n"
				result_file.write(ans)

	parser = BaseHTMLProcessor()
	parser.feed(html_doc)
	print "The output file can be located at : " + curr_path + '/example.properties'

@click.command()
@click.option('--language', default='Hindi')
def generate_resource(language):
	try:
		curr_path = os.path.dirname(os.path.abspath(__file__))
		language = language.title()
		source = open(curr_path + '/example.properties','r').readlines()
		
		try:
			lang_code = pycountry.languages.get(name=language)
		except:
			print "Unknown language.Try Again!"
			return 0
		
		lang_code = str(lang_code.iso639_1_code)
		dest_path = curr_path + '/example.' + language.lower()
		dest = open(dest_path,'w')
	
		for line in source:
			try:
				if "=" in line:                # if line is not blank
					inp = line.split("=")
					key = inp[0]
					value = inp[1]
					value1 = TextBlob(value)                     # value to be translated
					nvalue = value1.translate(to=lang_code)      # transalated value
					ans = key + "=" + str(nvalue) + "\n"
					dest.write(ans)
					
			except Exception as e:
				if "string unchanged" in str(e): #if text is unchanged like 12 remains 12
					ans = key + "=" + str(value1)
					dest.write(ans)
				elif "empty response" in str(e): # if text is a new line
					ans =key + "=" + str(value1)
					dest.write(ans)					
				else:
					print repr(value1)
					print "Exception: " + str(e)
		print "The output file can be located at: " + dest_path
	except Exception as e:
		print "Exception: " + str(e)


@click.command()
@click.option('--language', default='Hindi')			
def display_html(language):
	language = language.title()
	try:
		lang_code = pycountry.languages.get(name=language)
	except:
		print "Unknown language.Try Again!"
		return 0
	class BaseHTMLProcessor(SGMLParser):
		def reset(self):
			self.pieces = []
			SGMLParser.reset(self)

		def unknown_starttag(self, tag, attrs):
			strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
			self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
		def unknown_endtag(self, tag):

			self.pieces.append("</%(tag)s>" % locals())
		def handle_charref(self, ref):

			self.pieces.append("&#%(ref)s;" % locals())
		def handle_entityref(self, ref):

			self.pieces.append("&%(ref)s" % locals())
			if htmlentitydefs.entitydefs.has_key(ref):
				self.pieces.append(";")
		def handle_data(self, text):
			try:
				
				try:
					data = open(curr_path + '/example.properties','r').readlines()
				except:
					print "Ckeck if extract-text command is executed properly."
				
				for line in data:
					if text in line:
						key = line.rsplit("=")[0]
						break
				try:
					data1 = open(curr_path + '/example.'+language.lower(),'r').readlines()
				except:
					print "Ckeck if extract-text and generate-resource command is executed properly."
				for line in data1:
					if key in line:
						trans_data = line.rsplit("=")[1]
						break
				self.pieces.append(trans_data)
			except :
				self.pieces.append(text)
		def handle_comment(self, text):
			self.pieces.append("<!--%(text)s-->" % locals())
		def handle_pi(self, text):
			self.pieces.append("<?%(text)s>" % locals())
		def handle_decl(self, text):
			self.pieces.append("<!%(text)s>" % locals())
		def output(self):
			return "".join(self.pieces)
	curr_path = os.path.dirname(os.path.abspath(__file__))
	source_path = curr_path + '/example.html'
	htmlSource = open(source_path,'r').read()
	parser = BaseHTMLProcessor()
	parser.feed(htmlSource)
	dest_path = open(curr_path + '/transalted.html','w')
	dest_path.write(parser.output())
	print "The transalted html file is located at: " + curr_path + '/translated.html'



	
