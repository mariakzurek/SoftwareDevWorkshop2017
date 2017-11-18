# -*- coding: utf-8 -*-
#
# PrintNumbers.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# Fibonacci is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Software Development in Science Workshop 2017
#        Python GitHub project example
#

"""
Usage:
  PrintNumbers.py -h --help
  PrintNumbers.py [--fibonacci|--factorial] <numberOfTerms>

Options:
  -h --help       Print usage.
  --fibonacci     Print the fibonacci sequence.
  --factorial     Print the factorial.
"""

from docopt import docopt
from Parameters import *
import math

#
# FIBONACCI
#
def FibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        return(FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2))
 
def ComputeFibonacciSequence(n):
    sequence = []
    for i in range(n):
        sequence.append( FibonacciRecursion(i))
    return(sequence)

#
# FACTORIAL
#
def ComputeFactorial(n):
    return(math.factorial(n))

#
# FUNCTION TABLE
#
functionTable = { CONST_FUNC_CODE_FIBONACCI : ComputeFibonacciSequence,
                  CONST_FUNC_CODE_FACTORIAL : ComputeFactorial,
                }

#
# MAIN ENTRY
#
if __name__ == '__main__':
    # Process command line parameters.
    params = Parameters(docopt(__doc__, version = CONST_VERSION))
    params.PrintParameters()

    # Call corresponding function with <functionIndex> from FUNCTION TABLE.
    result = functionTable[params.functionIndex](params.numberOfTerms)

    # Print results depending on the executed function.
    if params.functionIndex == CONST_FUNC_CODE_FIBONACCI:
        print('Fibonacci Sequence for n = ' + str(params.numberOfTerms) + ':', result)
    elif params.functionIndex == CONST_FUNC_CODE_FACTORIAL:
        print('Factorial: ' + str(params.numberOfTerms) + '! =', str(result))
