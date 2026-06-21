import sys
import getopt

def main(argv):
    names = []
    try:
        opts, args = getopt.getopt(argv, "n:", ["name="])
    except getopt.GetoptError:
        print('test.py -n <name1> -n <name2>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--name"):
            names.append(arg)

    print(f"Daftar nama: {names}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengoleksi beberapa argumen nama.
# Kondisi: Ketika Anda ingin mengumpulkan beberapa nilai untuk diproses.