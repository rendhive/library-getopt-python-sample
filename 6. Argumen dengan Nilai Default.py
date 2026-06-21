import sys
import getopt

def main(argv):
    directory = '.'
    try:
        opts, args = getopt.getopt(argv, "d:", ["directory="])
    except getopt.GetoptError:
        print('test.py -d <directory>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--directory"):
            directory = arg

    print(f"Direktori yang diberikan: {directory}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menyediakan nilai default pada argumen.
# Kondisi: Ketika Anda ingin menentukan nilai awal tetapi masih membiarkan pengguna untuk mengubahnya.