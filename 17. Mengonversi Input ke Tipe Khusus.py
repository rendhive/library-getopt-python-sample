import sys
import getopt

def valid_float(value):
    try:
        return float(value)
    except ValueError:
        print(f"Kesalahan: '{value}' bukan angka yang valid.")
        sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "f:", ["float="])
    except getopt.GetoptError:
        print('test.py --float <number>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-f", "--float"):
            number = valid_float(arg)
            print(f"Angka yang diberikan: {number}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengonversi argumen ke float dan memvalidasinya.
# Kondisi: Ketika Anda ingin memastikan input sesuai dengan tipe data yang diinginkan.