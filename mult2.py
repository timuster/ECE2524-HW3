# ECE 2524 Homework 3 Problem 1 Sumit Kumar

import fileinput
import sys
import argparse

infloop=0
ans=1
ib=0
inn=0

parser = argparse.ArgumentParser(description='Process some numbers')

parser.add_argument('--ignore_non_numeric', action='store_const',const=1,default=0)

parser.add_argument('--ignore_blank', action='store_const',const=1,default=0)

parser.add_argument('input', nargs='*', type=str)

args = parser.parse_args()


if args.ignore_blank==1 :
	print "Ignore blank activated."
	ib=1

if args.ignore_non_numeric==1 :
	print "Ignore non numeric activated."
	inn=1

if len(args.input) > 0:
	for line in fileinput.input(args.input):
       		try:
			var1 = line
			ans=ans*float(var1)

		except ValueError as e:
			
			if not var1.strip() and ib==1:
				continue
			elif not var1.strip():
				print ans
				print "An empty line was found. Resetting answer.\nYou may use --ignore_blank to ignore empty lines."
				ans = 1
				continue
			if inn==1:
				continue
			else:
				print e
				print "You may use --ignore_non_numeric to ignore non numeric characters."
			sys.exit(1)
	
			
	print ans

#### WHEN FILES ARE NOT PROVIDED, REVERTS TO MANUAL INPUT
else: 
  
	print "Enter numbers to multiply"
	

	while infloop==0:	
		try:
			var1 = raw_input("Enter Number: ")
			if not var1.strip() and ib==1:
                		continue
			elif not var1.strip():
				print "Use --ignore_blank"
				break
			else:
				x= float(var1)
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
				print "You may use --ignore_non_numeric"
				sys.exit(1)


