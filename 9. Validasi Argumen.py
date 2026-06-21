import sys
import getopt

def valid_integer(arg):
    try:
        return int(arg)
    except ValueError:
        print(f"Kesalahan: '{arg}' bukan angka yang valid.")
        sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["number="])
    except getopt.GetoptError:
        print('test.py -n <number>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--number"):
            number = valid_integer(arg)
            print(f"Angka yang diberikan: {number}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Memvalidasi argumen yang dimasukkan oleh pengguna, memastikan bahwa argumen tersebut adalah integer.
# Kondisi: Ketika Anda perlu memvalidasi input pengguna untuk memastikan bahwa itu dalam format yang benar.