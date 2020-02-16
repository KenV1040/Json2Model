import sys, requests
from urllib.parse import urlparse
import argparse

def help():
    print("Usage")
    print("python main.py --url <insert api url here>")
    print("-u could also work instead of --url")


def main(argv):
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="Input api url", required=True, dest="url")
    #parser.add_argument('-h', '--help', help="Help", required=False)
    parser.add_argument('-fn', '--fileName', help="Prefered output file name", required=False, dest="fn")

    args = parser.parse_args()
    res = getJsonFromAPI(args.url)
    parseToModel(res, urlparse(args.url), args.fn)


def getJsonFromAPI(apiUrl):
    response = requests.get(apiUrl)
    print("API Call successful")
    if response.headers['Content-type'] != 'application/json':
        print("Not json")
        sys.exit(0)
    return response.json()
    
def parseToModel(resDic, urlParsed, fileName={}):
    listOfKeys = list(resDic.keys())
    print(f"Keys {listOfKeys}")
    if fileName is f.__defaults__[0]:
        print("No file name passed")
        fileName = urlParsed.netloc.replace('.','_') + '_model.dart'
        


if __name__ == "__main__":
    main(sys.argv)