import sys
import getopt

def main(argv):
    filename = "output.txt"
    try:
        opts, args = getopt.getopt(argv, "f:", ["file="])
    except getopt.GetoptError:
        print('test.py -f <filename>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-f", "--file"):
            filename = arg

    with open(filename, 'w') as file:
        file.write("Ini adalah output ke file.\n")
    print(f"Output disimpan ke {filename}.")

if __name__ == "__main__":
    main(sys.argv[1:])
# Fungsi: Menyimpan hasil dari argumen ke dalam file.
# Kondisi: Ketika Anda membutuhkan keluaran program untuk disimpan dalam file