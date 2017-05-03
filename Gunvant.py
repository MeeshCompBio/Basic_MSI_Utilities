"""This takes a GATK.vcf file as input and return the same file, but converst the Chr to just 
numbers with no 0's. This was made for Gunvant by Jean-Michel Michno "Meesh" (mich0391@umn.edu)"""
 
 
#example use
#python3 Gunvant.py your.vcf newname.vcf


import sys
from itertools import takewhile, islice

seqfile = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")
identifierlist = list()
sequenceinfolist = list()

#store all relavent information
for line in seqfile:
    line = line.rstrip()
    #If it is a header line then just write it
    if line.startswith("#"):
        output.write(line+'\n')
    #if not lets cut out out the parts
    else:
        columns = line.split("\t")
        CHR = columns[0].split("Chr")
        #see if it is a scaffold
        if "scaf" in str(CHR): 
            FCHR =str(CHR[0])
        #see if it starts with a 0
        elif CHR[1][0]=="0":
            temp = CHR[1].split("0")
            FCHR =temp[1]
        #if it is 10 or above just grab it
        else:
            FCHR = CHR[1]
        print(FCHR)
        #combine it for printing
        final= str(FCHR)+'\t'+str('\t'.join(columns[1:])+'\n')
        output.write(final)

output.close()
seqfile.close()

