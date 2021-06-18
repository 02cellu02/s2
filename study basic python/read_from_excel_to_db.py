import sys
import csv
def insert(fname):
    f=open(fname)
    reader =csv.reader(f)
    for i in reader:
        print(i)
    
def main():
    fname=sys.argv[1]
    insert(fname)

main()
