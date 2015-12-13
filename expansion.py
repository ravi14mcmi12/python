import re
import string
text = input("Enter the string for expenssion:")
print(text)
expStr = ""
uSet = string.printable
udigits = string.digits
ulower = string.ascii_lowercase
upper = string.ascii_uppercase
len_text = len(text)
all_index =  [m.start() for m in re.finditer('-', text)]
for i in range(len_text):
	#print(ch)
	ch=text[i]
#	if(text[0] or text[len_text-1] == "-"):
#		print(text)
#		break
	if( (ch == "-") and (i ==  0 or i == len_text-1 ) ):
		expStr =expStr + ch
		continue
	elif(ch == "-"):
		position = i 
		print(position)
		b4_ch = text[position - 1]
		af_ch = text[position + 1]
		#print(type(b4_ch),type(af_ch))
		#if(type(b4_ch) != type(af_ch) ):
		if( (b4_ch in udigits and af_ch in udigits)
                  or (b4_ch in ulower and af_ch in ulower)
		 or (b4_ch in upper and af_ch in upper) ) :
			index1 = uSet.index(b4_ch)
			index2 = uSet.index(af_ch)
			if index1 <= index2:
				newStr = uSet[(index1+1):(index2)]
			else:
				newStr =(uSet[(index2-1):(index1)])
				newStr = newStr[::-1]
			expStr = expStr + newStr
		else:
			expStr = expStr + ch
		#ch = text[ch+1]
		#print(expStr)
	else:
		expStr = expStr + ch
	#else:(text[i] == "-"):
	#	i = i+1
	
		#print(expStr)
print(expStr)
 
