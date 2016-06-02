# test

Ques1
 Command tools
 
 Usage:
     	
     	1. Install the script by changing the directory to redhatint/cmdtool and then type this cmd in terminal
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
     		Eg- diasplay-html --language hindi 
     		
Ques 2
 Uth-16 to Utf-8 conversion
 
  Usage :
      1. Got to directory redhatint/Utf16ToUtf8
      2 To run the file
          $ python utfcon.py
      #Test Case 1
          Enter: a2
          Utf-8 represention: c2a2

      #Test Case 2
          Enter: 0024
          Utf-8 represention: 24
