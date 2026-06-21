import sys
import getopt

def main(argv):
    sources = []
    try:
        opts, args = getopt.getopt(argv, "f:", ["from="])
    except getopt.GetoptError:
        print('test.py -f <source>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-f", "--from"):
            sources.append(arg)

    print("Sumber yang diterima:", sources)

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengumpulkan input dari beberapa sumber.
# Kondisi: Ketika Anda ingin menerima beberapa argumen dari pengguna sebagai sumber.