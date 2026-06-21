import sys
import getopt

def main(argv):
    debug = False
    try:
        opts, args = getopt.getopt(argv, "d", ["debug"])
    except getopt.GetoptError:
        print('test.py --debug')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--debug"):
            debug = True

    if debug:
        print("Mode debug aktif.")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengonfigurasi argumen yang berfungsi sebagai toggle untuk mode tertentu.
# Kondisi: Ketika Anda ingin memberikan opsi bagi pengguna untuk mengaktifkan atau menonaktifkan fitur.