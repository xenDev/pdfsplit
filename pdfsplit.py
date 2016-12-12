import argparse
import pprint
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import logging

parser = argparse.ArgumentParser(description="Split pdf into multiple files")
parser.add_argument("-i","--input", help="Input file", required=True)
parser.add_argument("-l","--list", help="Comma separated list for splitting")
parser.add_argument("-s","--suffix", help="Suffix for output filename")
parser.add_argument("--log", help="Log Level")


args = vars(parser.parse_args())

if args['log']:
    numericLevel = getattr(logging, args['log'].upper(), None)
    if not isinstance(numericLevel, int):
        raise ValueError('Invalid log level: %s' % args['log'])
    logging.basicConfig(level=numericLevel)

inputFile = args['input']
inputReader=PdfFileReader(open(inputFile, "rb"))

numberOfPages = inputReader.getNumPages()
logging.info("Input file " + inputFile + " has " + str(numberOfPages) + " pages")

splistlist=[]
if args['list']:
    splitlist = [int(n)-1 for n in args['list'].split(',')]
    #Append the last page
    splitlist.append(numberOfPages)
else:
    splitlist=list(range(0,numberOfPages))

logging.debug("Split list is :")
logging.debug(pprint.pformat(splitlist))

suffix='page'
if args['suffix']:
    suffix = args['suffix']
logging.debug("Suffix is " + suffix)

#Get the file basename
inputFileBase = os.path.splitext(inputFile)[0]
for i in range(len(splitlist)-1):
    logging.debug("Starting with page: " + str(splitlist[i]+1))
    outputWriter=PdfFileWriter()
    for j in range(splitlist[i], splitlist[i+1]):
        logging.debug("Adding page " + str(j+1))
        outputWriter.addPage(inputReader.getPage(j))
    outputFileName= inputFileBase + '-' + suffix + str(i+1) + ".pdf"
    logging.info("Writing to file " + outputFileName)
    outputStream = open(outputFileName, "wb")
    outputWriter.write(outputStream)
