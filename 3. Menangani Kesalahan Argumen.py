import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hx:", ["help", "exec="])
    except getopt.GetoptError:
        print('test.py -x <value>')
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menangani kesalahan argumen yang diberikan.
# Kondisi: Ketika Anda ingin memberikan umpan balik kepada pengguna jika argumen yang salah dimasukkan.