import sys
import getopt

def main(argv):
    timeout = 10  # Default timeout
    try:
        opts, args = getopt.getopt(argv, "t:", ["timeout="])
    except getopt.GetoptError:
        print('test.py -t <timeout>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-t", "--timeout"):
            timeout = int(arg)

    print(f"Timeout yang diatur: {timeout} detik")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menetapkan batas waktu dari argumen.
# Kondisi: Ketika Anda ingin memungkinkan pengguna untuk mengatur batas waktu untuk operasi.