from tap import parser
import sys
import json
from os.path import exists

def main():
    args = sys.argv[1:len(sys.argv)]

    summary = {'summary' : []}
    i = 0

    parser = parser.Parser()

    for file in args:
        if exists(file):
            for line in parser.parse_file(file):
                try:
                    total = line.expected_tests
                    summary['summary'].append({'filename' : file, 'total' : 0, 'passed' : 0, 'skipped' : 0, 'failed' : 0})
                except:
                    pass

                try:
                    result = None
                    if line.skip == True:
                        summary['summary'][i]['skipped'] += 1
                        summary['summary'][i]['total'] += 1
                    elif line.ok == True:
                        summary['summary'][i]['passed'] += 1
                        summary['summary'][i]['total'] += 1
                    else:
                        summary['summary'][i]['failed'] += 1
                        summary['summary'][i]['total'] += 1
                except:
                    pass
        i+=1

    print(json.dumps(summary))