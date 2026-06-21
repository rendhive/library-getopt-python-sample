import sys
import getopt

def main(argv):
    exec_name = ''
    try:
        opts, args = getopt.getopt(argv, "e:", ["exec="])
    except getopt.GetoptError:
        print('test.py --exec <command>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-e", "--exec"):
            exec_name = arg

    print(f"Command yang dijalankan: {exec_name}")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Mengambil argumen command melalui opsi.
# Kondisi: Ketika Anda ingin memungkinkan pengguna menjalankan perintah atau argumen opsional.