# Test Driven Learning Project.
# Desenvolva TDD e programação com TDD e programação!
# Módulo novice.
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Paulo Henrique Rodrigues Pinheiro <paulo@sysincloud.it>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

CC=cc
FLAGS=-Wall -ansi -pedantic -g

solved.o: solved.c
	$(CC) -c $^ $(FLAGS) -o $@

lists.o: lists.c
	$(CC) -c $^ $(FLAGS) -o $@

unittest: unittest.c solved.o lists.o
	$(CC) $^ $(FLAGS) -o $@

.PHONY: clean all test

clean:
	rm -f solved solved.o lists.o unittest

all: clean test

test: unittest
	./unittest
