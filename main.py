import sys


def help():
    print("Usage")
    print("python main.py --url <insert api url here>")
    print("-u could also work instead of --url")


def main(argv):
    apiUrl = ""

    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    
    if sys.argv[1] == "--help" or sys.argv[1] == '-h':
        help()
        sys.exit(0)
    elif sys.argv[1] == "--url" or sys.argv[1] == "-u":
        if len(sys.argv) != 3:
            print("Missing url value")
        else: 
            apiUrl = sys.argv[2]
            print(f"APIUrl: {sys.argv[2]}")
    else:
        help()
        sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)