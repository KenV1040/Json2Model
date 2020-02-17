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
    print("Getting api...")
    response = requests.get(apiUrl)
    print("API Call successful")
    if response.headers['Content-type'] != 'application/json':
        print("Not json")
        sys.exit(0)
    return response.json()
    
def parseToModel(resDic, urlParsed, fileName={}):
    if type(resDic) == list:
        print("No keys, it's all a list")
        listOfKeys = list(resDic[0].keys())
        resDic = resDic[0]
    else: 
        listOfKeys = list(resDic.keys())
    print(f"Keys {listOfKeys}")
    localFileName = ""
    if fileName is parseToModel.__defaults__[0]:
        localFileName = urlParsed.netloc.replace('.','_') + '_model.dart'
    else:
        localFileName = fileName

    variableName = []
    # Change all keys to lowerCamelCase
    for i in range(0, len(listOfKeys)):
        if "_" not in listOfKeys[i] and "-" not in listOfKeys[i]:
            variableName.append(listOfKeys[i].lower())
            continue
        if "_" in listOfKeys[i]:
            components = listOfKeys[i].split('_')
            variableName.append(components[0].lower() + ''.join(x.title() for x in components[1:]))
        elif "-" in listOfKeys[i]:
            components = listOfKeys[i].split('-')
            variableName.append(components[0].lower() + ''.join(x.title() for x in components[1:]))
    print(variableName)
    className = urlParsed.netloc.replace('.',' ').replace('www.','')
    className = className.title().replace(' ','')

    # Start writing dart file
    thisFile = open(localFileName, "w")
    thisFile.truncate(0)
    thisFile.write("class " + className + " {\n")
    # Allocating variables to key names
    index = 0
    for key in listOfKeys:
        print(type(resDic[key]))
        if type(resDic[key]) == list:
            thisFile.write(f"\tList<dynamic> {variableName[index]} = [];\n")
        elif type(resDic[key]) == str:
            thisFile.write(f"\tString {variableName[index]};\n")
        elif type(resDic[key]) == dict:
            thisFile.write(f'\tMap<String, dynamic> {variableName[index]} = {{}};\n')
        elif type(resDic[key]) == float:
            thisFile.write(f'\tdouble {variableName[index]};\n')
        index += 1
        
    thisFile.write('\n')
    # Creating a fromJson constructor method
    thisFile.write(f"\t{className}.fromJson({{Map<String, dynamic> data}}) {{\n")  
    index = 0
    for key in listOfKeys:
        if type(resDic[key]) == str:
            thisFile.write(f"\t\tthis.{variableName[index]} = data['{key}'] ?? \"\";\n")
        else: 
            thisFile.write(f"\t\tthis.{variableName[index]} = data['{key}'];\n")
        index += 1    
    thisFile.write("\t}\n")

    thisFile.write("}")
    thisFile.close()
    print("Successfuly created model file")


if __name__ == "__main__":
    main(sys.argv)