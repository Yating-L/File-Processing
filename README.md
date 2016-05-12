# File-Processing

### promoter.py

  Extract promoter regions of a gene list from the gff file and write into a faste file.
  
### format_v2.py

  Convert a hit file into a 0-1 matrix
  
  <pre>
  hit file format: 
  \>motif1
    Seq1
    Seq2
  \>motif2
    Seq2
    Seq3
  </pre>
  <pre>
  0-1 matrix format:
          Seq1  Seq2  Seq3
  motif1    1     1     0
  motif2    0     1     1
  </pre>

  
