#*********************************************************************************
#* Project: promoter.py
#* Description: Convert hit file into a 0-1 matrix
#* Name: Yating Liu
#*********************************************************************************

#!/usr/bin/env python3
import csv


def read(filename):
  seq_set = set()
  motif_set = set()
  with open(filename) as f:
    for line in f:
      line = line.strip()
      if line[0] == '>':
        line = line[1:]
        motif_set.add(line)
      else:
        seq_set.add(line)
  return seq_set


def matrix(filename):
  seq_set = read(filename)
  #print "matrix()", filename
  with open(filename) as f:
    seq_list = list(seq_set)    
    count = -1
    cov_seq = []
    cov_seq.append(seq_list)
    tmp_seq = [0]*len(seq_set)
    motif = []
    for line in f:  
      line = line.strip() 
      if line[0] == '>':
        count = count + 1
        line = line[1:]
        motif.append(line)
        if count > 0:
          tmp_seq = [motif[count-1]] + tmp_seq
          cov_seq.append(tmp_seq)
          tmp_seq = [0]*len(seq_set) 
      else:
        i = seq_list.index(line)
        tmp_seq[i] = 1
    tmp_seq = [motif[count]]+ tmp_seq
    cov_seq.append(tmp_seq)
  return cov_seq

def write(input, output, b=True):
  """
  convert hits file into csv matrix.

  use white-space instead of comma when b==True.
  """
  import csv 
  a = matrix(input)
  with open(output,'wt') as f:
    if b :
      writer = csv.writer(f, delimiter=' ')
      pass
    else:
      writer = csv.writer(f)
      pass
    writer.writerows(a[1:])
    pass
  pass
     
def modify(filename, out1, out2):
  write(filename, out1)
  write(filename, out2, True)
  pass
