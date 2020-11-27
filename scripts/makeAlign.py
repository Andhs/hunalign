#!/usr/bin/python

import sys

def collectAlign(batchFile):
    ladder = ""
    batch = open(batchFile, "r")
    num_lines = 0
    line = batch.readline()
    numFile = open(line.split()[0][:-5] + ".numbers")
    while line:
        curFile = open(line.split()[2], "r")
        for aline in curFile[:-1]
            ladder += str(int(aline.split()[0]) + num_lines) + "\t" + str(int(aline.split()[1]) + num_lines) + "\t" + aline.split()[2] + "\n"
        curFile.close()
        line_from_numFile = numFile.readline()
        num_lines += int(line_from_numFile)
        line = batch.readline()
    batch.close()
    numFile.close()
    return ladder

def main() :
    if len(sys.argv) != 2 :
        log("Making a single align file from batch")
        log("")
        log("Usage: makeAlign.py hunalign_batch_file > full align file")
        sys.exit(-1)

    else:
        batchFile = sys.argv[1]

    stdout = collectAlign(batchFile)
    sys.stdout.write(stdout)


if __name__ == '__main__': 
    main()