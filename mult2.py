# ECE 2524 Homework 3 Problem 1 Sumit Kumar

import fileinput
import sys
import argparse

f=0
ans=1
ib=0
inn=0
parser = argparse.ArgumentParser(description='Process some numbers')



parser = argparse.ArgumentParser()

parser.add_argument('--ignore_non_numeric', action='store_const',const=1,default=0)

parser.add_argument('--ignore_blank', action='store_const',const=1,default=0)

parser.add_argument('input', nargs='*', type=argparse.FileType('r'), default=1)


args = parser.parse_args()

#################################################

if args.ignore_blank==1 :
	print "ignore blank activated"
	ib=1
if args.ignore_non_numeric==1 :
	print "ignore non numeric activated"
	inn=1

if args.input != 1:
   print "we have a file"
   for line in fileinput.input():

	try:
    		var1 = line
		str=var1.strip()
		if not str.strip() and ib==1:
                	continue
		elif not str.strip():
			print "Use --ignore_blank"
			break
		else:
			x= float(str)
			ans=ans*x

	except EOFError:
		print "\nEnd of file command has been received!"
		print "\nHere is your answer :", ans
		break

	except ValueError as e:
		if inn==1:
			continue
		else:
			print e
			sys.exit(1)
	
############################################################################
else:
	print "Enter numbers to multiply"
	

	while f==0:	
		try:
			var1 = raw_input("Enter Number: ")
			str=var1.strip()
			if not str.strip() and ib==1:
                		continue
			elif not str.strip():
				print "Use --ignore_blank"
				break
			else:
				x= float(str)
				ans=ans*x

		except EOFError:
			print "\nEnd of file command has been received!"
			print "\nHere is your answer :", ans
			break

		except ValueError as e:
			if inn==1:
				continue
			else:
				print e
				sys.exit(1)


