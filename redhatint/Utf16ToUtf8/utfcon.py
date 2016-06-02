import sys

inp = raw_input("Enter:\t")  
try:							               			#utf-16 input is taken
	utf16_dec = int(inp,16)
except:
	print "Bad input....Try again."
	sys.exit(0)						                    #calculating decimal value of utf-16 input
if utf16_dec <= 127:                          			#checking if decimal value lies in range between 0 to 127
	print "Utf-8 represention: " + inp[-2:]

elif utf16_dec <=255:
	utf8 = unichr(utf16_dec).encode('utf-8')			#conversion of utf-16 to utf-8
	utf8 =repr(utf8)
	utf8 = utf8.replace('\\x','').strip("''")
	print "Utf-8 represention: " + utf8

else:													# if input is not in utf-8 range [0..255]
	print "The input cannot be represented in Utf-8 format, Please specify a valid input."


#Test Case 1
#Enter: a2
#Utf-8 represention: c2a2

#Test Case 2
#Enter: 0024
#Utf-8 represention: 24
