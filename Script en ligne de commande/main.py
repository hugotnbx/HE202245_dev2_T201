import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_dir', metavar='dir', required=True, help='Dossier contenant des fichiers et dossiers')
    parser.add_argument('--output_dir', metavar='dir', help='Dossier où un fichier ou dossier doit être déplacé')
    parser.add_argument('--move', action='store_true', help='Déplace un fichier ou un dossier')
    parser.add_argument('--sort_content', action='store_true', help='Trie les fichiers et dossiers d\'un dossier')

    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    dir_content = os.listdir(input_dir)

    if args.sort_files and args.input_dir and args.output_dir:
        for element in dir_content:
            split_element = element.split('.')

            if len(split_element) > 1:
                extension = split_element[1]
                element_path = os.path.join(input_dir, element)
                folder = os.path.join(output_dir, extension)

                os.makedirs(folder, exist_ok=True)
                shutil.move(element_path, os.path.join(folder, element))


if __name__ == "__main__":
    main()
