
#!/bin/bash

#This script with take the base name of the files your are interested in, the output directory, and the sequencing adapter
#and combine all the forward and reverse reads into two files


set -euo pipefail

#sample base file name
FILE="$1"
#output directory
OUT="$2"
#Adapter seq
ADAPT="$3"

#combine all files with your base name, anything, R1, anything, .fastq
cat ${FILE}*[R][1]*fastq \
> "${OUT}${FILE}_${ADAPT}_R1.fastq"


cat ${FILE}*[R][2]*fastq \
> "${OUT}${FILE}_${ADAPT}_R2.fastq"
