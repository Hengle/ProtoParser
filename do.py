#-*- coding: utf-8 -*-

import sys
import os
import shutil
import codes
from parser import Parser

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT_PATH = os.path.join(MODULE_PATH, "temp")
INPUT_PATH = os.path.join(MODULE_PATH, "test/messages")

USAGE = "python do.py [input_path] [output_path]"

def convert(name, srcPath, dstPath, module):
	fd = module.files.get(srcPath)
	if fd is None:
		pa = Parser(module, srcPath)
		if not pa.parse():
			return False
		fd = pa.fd

	
	return True

def main():
	outputPath = OUTPUT_PATH
	inputPath = INPUT_PATH

	if len(sys.argv) > 1: inputPath = sys.argv[1]
	if len(sys.argv) > 2: outputPath = sys.argv[2]

	if os.path.exists(outputPath):
		shutil.rmtree(outputPath)

	os.mkdir(outputPath)

	module = codes.Module()
	module.searchPath = [inputPath]

	files = os.listdir(inputPath)
	for fname in files:
		name, ext = os.path.splitext(fname)
		if ext != ".proto": continue

		srcPath = os.path.join(inputPath, fname)
		dstPath = os.path.join(outputPath, name)
		print "generate:", fname
		convert(fname, srcPath, dstPath, module)

if __name__ == "__main__":
	main()