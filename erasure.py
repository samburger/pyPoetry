"""
Created on Oct 28, 2014


Given an input text file, generates a random erasure poem formatted in LaTex, ready for compilation.

"""
# -*- coding: utf-8 -*-

import random
import argparse
import subprocess


parser = argparse.ArgumentParser(description='Generates erasure poetry from a source text.')
parser.add_argument('sourceText',help='The .txt file to poetize.')
parser.add_argument('outputName',help='What you want the output file to be called, in quotes.',type=str)
parser.add_argument('probability',help='Probability that a word is erased: a decimal number between 0 and 1.',type=float)
args = parser.parse_args()

text = open(args.sourceText,'r').read() # Open our text file.
words = text.split() # Make list of space-delimited words in source text.
random.seed()
prob_erase = args.probability # Probability that a word will be erased, 0-1.


def is_erased():
    if random.random() <= prob_erase:
        return True
    else:
        return False
erased_list = [is_erased() for word in words] # Generate an isErased value (true or false) for each word.
erased_dict = dict(zip(words,erased_list)) # Map the words to their erased values.

words = ['\censor{' + word + '}' if erased_dict[word]==True else word for word in words] # Censor required words

# Prepare LaTeX document.
result_text = '''\documentclass{{article}}
\usepackage{{censor}}
\\begin{{document}}
\pagenumbering{{gobble}}
\\vspace*{{\\fill}}
{0}
\\vspace*{{\\fill}}
\end{{document}}
'''.format(' '.join(words))

output = open(args.outputName+'.tex','w')
output.write(result_text) # Write LaTeX document.

make_pdf = subprocess.Popen(['pdflatex',args.outputName+'.tex'],shell=False) # Generate PDF (hopefully)

