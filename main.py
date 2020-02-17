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
    if (args.fn is None):
        parseToModel(res, urlparse(args.url))
    else:
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
    localFileName = ""
    if fileName is parseToModel.__defaults__[0]:
        localFileName = urlParsed.netloc.replace('.','_') + '_model.dart'
    else:
        localFileName = fileName
    
    for key in listOfKeys:
        print(type(resDic[key]))
        if type(resDic[key]) == list:
            print(f"{key} Is list")
        elif type(resDic[key]) == str:
            print(f"{key} Is list")

    thisFile = open(localFileName, "w")
    className = urlParsed.netloc.replace('.',' ')
    className = className.title().replace(' ','')
    thisFile.write("class " + className + " {\n")
    for key in listOfKeys:
        if type(resDic[key]) == list:
            thisFile.write(f"\tList<dynamic> {key} = [];\n")
        elif type(resDic[key]) == str:
            thisFile.write(f"\tString {key};\n")
    thisFile.write(f"\t{className}.fromJson({{Map<String, dynamic> data}}) {{\n")  
    for key in listOfKeys:
        thisFile.write(f"\t\tthis.{key} = data['{key}'];\n")      
    thisFile.write("\t}\n")
    thisFile.write("}")
    thisFile.close()
    print("Successfuly created model file")


if __name__ == "__main__":
    main(sys.argv)