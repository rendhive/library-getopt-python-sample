import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    # Handle actual arguments
    print("Semua argumen diterima:", args)

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menangani kesalahan ketika penyimpanan argumen tidak valid.
# Kondisi: Ketika Anda ingin memberikan umpan balik detail tentang kesalahan.