import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        print('test.py --help')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Contoh penggunaan: test.py [options]')
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menampilkan pesan bantuan.
# Kondisi: Ketika Anda ingin memberikan panduan kepada pengguna tentang cara menggunakan program.