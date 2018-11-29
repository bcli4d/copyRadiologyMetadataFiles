import argparse
import json
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(description="Build DICOM image metadata table")
    parser.add_argument("-v", "--verbosity", action="count", default=2, help="increase output verbosity")
    parser.add_argument("-z", "--zips", type=str, help="file of from:to pairs",
                        default='./zipFileNames')

    return parser.parse_args()

def copyFiles(args,fromTo):
    fromToDict = json.loads(fromTo[0])
    froms = fromToDict.keys()
    for from_ in froms:
        print("{} {} {} {}".format('gsutil','cp',from_,fromToDict[from_]))
        subprocess.call(['gsutil','cp',from,fromTo[from]])

def deleteFiles(args, fromTo):
    fromToDict = json.loads(fromTo[0])
    froms = fromToDict.keys()
    for from_ in froms:
        print("{} {} {}".format('gsutil', 'rm',from_))
        subprocess.call(['gsutil','rm',from_])


def loadZips(args):
    with open(args.zips) as f:
        fromTo = f.read().splitlines()
    return fromTo


if __name__ == '__main__':

    args = parse_args()

    # Initialize work variables from previously generated data in files
    fromTo = loadZips(args)

    copyFiles(args,fromTo)
    deleteFiles(args,fromTo)
