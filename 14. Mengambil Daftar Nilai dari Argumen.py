import sys
import getopt

def main(argv):
    values = []
    try:
        opts, args = getopt.getopt(argv, "v:", ["values="])
    except getopt.GetoptError:
        print('test.py -v <value1,value2,...>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-v", "--values"):
            values = arg.split(',')

    print("Nilai yang diterima:", values)

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengambil daftar nilai yang dipisahkan oleh koma.
# Kondisi: Ketika Anda ingin menerima data dalam format list dari pengguna.