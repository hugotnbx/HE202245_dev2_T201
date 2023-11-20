import argparse
import os
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trie les fichiers d'un répertoire")
    parser.add_argument("--input-dir", metavar="dir", default=".", help="Contient les fichiers à ranger")
    parser.add_argument("--output-dir", metavar="dir", default=".", help="Dossier dans lequel seront rangés les dossiers")

    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    dir_content = os.listdir(input_dir)

    for file in dir_content:
        elements = file.split(".")

        if len(elements) > 1:
            extension = elements[1]
            file_path = os.path.join(input_dir, file)
            folder = os.path.join(output_dir, extension)

            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, file))
