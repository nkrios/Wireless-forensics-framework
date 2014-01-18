#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
def show_all_destination():
	command=notation.libc+ " -r "+notation.pack_file+notation.sortd
	print("Destinations")
	print("============")
	execute=os.popen(command).read()
	print(execute)
def show_all_source():
	print("Sources")
        print("=======")
	command=notation.libc+ " -r "+notation.pack_file+notation.sorts
	execute=os.popen(command).read()
	print(execute)

def show_all_association_requests():
	command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.associations_req + notation.sort_source_dest
	execute=os.popen(command).read()
	source,dest=execute.split(",")
	print"Source"+"\t\t\t\t\t\t"+"Destination"
	print source+"\t\t====>\t\t"+dest
	
def show_all_Deauth():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.deauth+notation.sort_source_dest
        execute=os.popen(command).read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
    	print"Source"+"\t\t\t\t\t\t"+"Destination"
	while(j>=0):
		k=line[j]
		source,dest=k.split(",")
        	print source+"\t\t====>\t\t"+dest
		j=j-1

def show_high_data():
	command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.data+notation.sort_data_count
	execute=os.popen(command). read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
	a=j
	max_bit=0
	int(max_bit)
	print("No.of Packets\tSource\t\t\tDestination")
	print("=============\t======\t\t\t===========")
	while(j>=0):
                k=line[j]
                bits,source,dest=k.split(",")
		if(int(bits)>max_bit):
			max_bit=int(bits)
		j=j-1
	while(a>=0):
		b=line[a]
		bits1,source1,dest1=b.split(",")
                if(int(bits1)==max_bit):
			print(Fore.RED+Back.BLACK+bits1+"\t\t"+source1+"\t"+dest1+Style.RESET_ALL)
		else:
                	print bits1+"\t\t"+source1+"\t"+dest1
		a=a-1
	




	
