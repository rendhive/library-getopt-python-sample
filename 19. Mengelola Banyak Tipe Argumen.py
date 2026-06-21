import sys
import getopt

def main(argv):
    args = {}
    try:
        opts, args = getopt.getopt(argv, "p:q:", ["param1=", "param2="])
    except getopt.GetoptError:
        print('test.py -p <param1> -q <param2>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-p", "--param1"):
            args['param1'] = arg
        elif opt in ("-q", "--param2"):
            args['param2'] = arg

    print(f"Parameter 1: {args.get('param1')}")
    print(f"Parameter 2: {args.get('param2')}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengelola beberapa argumen dari command line.
# Kondisi: Ketika Anda ingin mengelompokkan beberapa parameter dalam satu aplikasi.