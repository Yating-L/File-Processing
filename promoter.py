#*********************************************************************************
#* Project: promoter.py
#* Description: Extract promoter regions of a gene list from the gff file
#*              and write into faste file
#* Name: Yating Liu
#*********************************************************************************


#!/usr/bin/env python3


def ReverseComplement(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])
    
genefile = open("background_copy.txt", "r")
searchfile = open("GCA_000012005.1_ASM1200v1_genomic.gff", "r")
fa = open("neg2_seq.fa","w")
notfound = open("neg2_notnotfound.txt","w")
chromosome = open("chromosome.fasta", "r").read().replace('\n','')
#print(chromosome[0:100])
print("\n")
#test = ReverseComplement(chromosome[0:100])
#print(test)
for line in genefile:
  gene = line.replace('\n','')
  genename = "Name=" + gene
  searchfile.seek(0)
  found = 0
  for line2 in searchfile:
    if genename in line2:
      #fa.write(line2)
      start = line2[24:]
      #print(start)
      found = 1
      s = start.split()
      if (s[3] == '+'):
        start_p = int(s[0])-1001
        if (start_p < 0):
          start_p = 0
        end_p = int(s[0])-2
        fa.write('>' + gene + '+' + str(start_p) + '-' + str(end_p) + '\n')
        ss = chromosome[start_p:end_p].replace('\n','')
      else:
        start_p = int(s[1])+999
        end_p = int(s[1])
        if (start_p > 4369231):
          start_p = 4369231
        fa.write('>' + gene + '-' + str(start_p) + '-' + str(end_p) + '\n')
        ss = chromosome[end_p:start_p].replace('\n','')
        ss = ReverseComplement(ss)
      fa.write(ss + '\n')
  if (found == 0):
    notfound.write(gene + '\n')
      
      
notfound.close()     
fa.close()
genefile.close()
searchfile.close()

  
  
