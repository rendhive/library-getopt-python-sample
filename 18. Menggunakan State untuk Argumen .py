import sys
import getopt

def main(argv):
    status = 'inactive'
    try:
        opts, args = getopt.getopt(argv, "s:", ["status="])
    except getopt.GetoptError:
        print('test.py -s <status>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--status"):
            status = arg

    print(f"Status yang diatur: {status}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengatur status melalui argumen.
# Kondisi: Ketika Anda memerlukan pengaturan status dalam program berbasis argumen.