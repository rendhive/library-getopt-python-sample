import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        print('test.py')
        sys.exit(2)

    print("Argumen lain yang diterima:", args)

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mencetak semua argumen lain yang diterima.
# Kondisi: Ketika Anda ingin melihat semua argumen setelah penguraian.