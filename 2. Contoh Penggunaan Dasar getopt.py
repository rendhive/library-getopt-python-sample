import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:", ["help", "name="])
    except getopt.GetoptError:
        print('test.py -n <name>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('test.py -n <name>')
            sys.exit()
        elif opt in ("-n", "--name"):
            print(f"Nama: {arg}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengambil argumen nama dan menampilkannya.
# Kondisi: Ketika Anda ingin memberikan dokumentasi dan pemrosesan argumen sederhana.