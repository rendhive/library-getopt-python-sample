import sys
import getopt

def main(argv):
    version = "1.0"
    try:
        opts, args = getopt.getopt(argv, "v", ["version"])
    except getopt.GetoptError:
        print('test.py --version')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-v", "--version"):
            print(f"Version: {version}")
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menampilkan versi program.
# Kondisi: Ketika Anda ingin memberikan informasi versi dari aplikasi.