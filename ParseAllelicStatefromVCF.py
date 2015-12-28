"""This takes a GATK.vcf file as input, the numer of samples, and the name of your desired
 ouput file and returns you a .csv file with the allelic state for each sample"""
 
 
#example use
#python3 your.vcf 3 output.csv


import sys
from itertools import takewhile, islice

seqfile = open(sys.argv[1], "r")
#output = open(sys.argv[2], 'w')
NumberSamples = int(sys.argv[2])

#pull out the headers
header = list()
with seqfile as f:
    start = sum(1 for _ in takewhile(lambda x: x[0] == "#", f)) - 1
    f.seek(0)
    data = next(islice(f, start, start+1))
    data = data.rstrip()
    data = data[1:]
    columns = data.split("\t")
    print(NumberSamples)
    sampleID = columns[-NumberSamples:]
    Data = columns[0:-NumberSamples]
    for l in Data:
        header.append(l)
    for j in sampleID:
      #if you want to trim your headers, slice j in the next line j[start:stop]
        cut = j
        header.append(cut)

#print out your headers
print("These are your headers""\n",header)



seqfile = open(sys.argv[1], "r")
identifierlist = list()
sequenceinfolist = list()

#store all relavent information
for line in seqfile:
    line = line.rstrip()
    if line.startswith("#"):
        continue
    else:
        sequenceinfolist.append(line)





var = [[] for _ in range(len(header))]
# parse our the file
for line in sequenceinfolist:
    columns = line.split("\t")
    for i in range(len(header)):
        if i < 9:
            var[i].append(columns[i])
        else:
          #this line slices out the allele state
            var[i].append(columns[i][0:3])

output = open(sys.argv[3], "w")

output.write(','.join(header))
output.write('\n')

PLIST= list()

for j in range(len(var[1])):
    final = []
    for i in var:
        final.append(i[j])
    #make output comma seperated
    output.write(','.join(final)+'\n')



output.close()
seqfile.close()
