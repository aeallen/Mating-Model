#!/usr/bin/env python

import os
import sys

inputs = []
for i in range(len(sys.argv)):
        if i > 0:
                inputs.append(sys.argv[i])

filename = inputs[0]
iterations = int(inputs[1])

command = 'sbatch -o output.txt -t 120:00:00 -J ' + inputs[2] + ' --wrap="python ./' + filename + '"'

for i in range(iterations):
        os.system(command)
