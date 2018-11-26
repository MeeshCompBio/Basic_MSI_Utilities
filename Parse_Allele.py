"""This sctip will take a gff file as input and parce out the longest
   transcripts  in gff format for formatting for exon mapping"""

import sys
import getopt


def usage():
    print("""\n
        This is the usage function:
        python3 Parse_Allele.py -i <input_file> -o <output_file>
            -i or input_file:  The name of your VCF input file
            -o or output_file: The name of your output file
            -g:                Output Ref or Alt base at each position instead
                               of a number (i.e G instead of 0/0).
            --filter: <int>    Filter through positions where the number of
                               homozygous Ref or Alt alleles are larger than
                               the specified number
        \n""")


try:
    opts, args = getopt.getopt(sys.argv[1:],
                               "i:o:gfph",
                               ["input_file=",
                                "output_file=",
                                "filter=",
                                "help",
                                ]
                               )
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

base_call = False
limit = False

for opt, arg in opts:
    if opt in ("-i", "--input_file"):
        input_file = arg
    elif opt in ("-o", "--output_file"):
        output_file = arg
    elif opt == "-g":
        base_call = True
    elif opt in ("--filter"):
        filter_num = int(arg)
        limit = True
    elif opt in ("-h", "--help"):
        usage()
        sys.exit(2)
    else:
        assert False, "unhandled option"


# open file for reading, writing
vcf_file = open(input_file, "r")
out_file = open(output_file, "w")


for line in vcf_file:
    line = line.strip()
    if line.startswith("#CHROM"):
        print("These are your headers""\n", line)
        # print(line, file=out_file)
    elif line.startswith("#"):
        continue
    else:
        fields = line.split("\t")
        Ref = fields[3]
        Alt = fields[4]
        Ref_allele_freq = 0
        Alt_allele_freq = 0
        for idx, field in enumerate(fields):
            if idx < 9:
                continue
            else:
                # subset the genotype call
                geno = field.split(":")[0]
                if base_call is False:
                    # subset based on genotype call
                    fields[idx] = geno
                    if geno == "0/0":
                        Ref_allele_freq += 1
                    elif geno == "1/1":
                        Alt_allele_freq += 1
                else:
                    # check to see what the call is and pull the allele
                    if geno == "0/0":
                        fields[idx] = Ref
                        Ref_allele_freq += 1
                    elif geno == "1/1":
                        fields[idx] = Alt
                        Alt_allele_freq += 1
                    elif geno == "0/1":
                        fields[idx] = str(Ref)+"/"+str(Alt)
                    elif geno == "1/0":
                        fields[idx] = str(Alt)+"/"+str(Ref)
                    elif geno == "./.":
                        fields[idx] = "NA"
                # print(Ref_allele_freq)
        # print(Ref_allele_freq)
        output = "\t".join(str(x) for x in fields)
        if limit is False:
            print(output, file=out_file)
        else:
            if Ref_allele_freq >= filter_num and \
               Alt_allele_freq >= filter_num:
                print(output, file=out_file)

vcf_file.close()
out_file.close()
