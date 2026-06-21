import sys
import getopt

def main(argv):
    group = "default"
    try:
        opts, args = getopt.getopt(argv, "g:", ["group="])
    except getopt.GetoptError:
        print('test.py -g <group>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-g", "--group"):
            group = arg

    print(f"Grup yang dipilih: {group}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menerima grup sebagai argumen.
# Kondisi: Ketika Anda ingin melakukan pengelompokan pada argumen.