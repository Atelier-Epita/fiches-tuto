import argparse
import os

import frontmatter
import markdown
import pdfkit

file_path = os.path.dirname(os.path.realpath(__file__))
ressources_path = "https://github.com/Atelier-Epita/fiches-tuto/raw/main/static/"

def process(path: str, output: str):
    with open(path) as f:
        metadata, content = frontmatter.parse(f.read())

        content = markdown.markdown(content)

        html = ""
        with open(file_path + "/document.html") as document:
            html = document.read()

        html = html.replace("%title%", metadata['title']) \
            .replace("%content%", content) \
            .replace("../static/", ressources_path)

        pdfkit.from_string(html, output, options={
            "margin-top": "5", "margin-bottom": "5", "margin-left": "0", "margin-right": "0",
            "dpi": "300"})

    print(f"Processed {os.path.basename(path)}.")


def get_pdf_path(outdir: str, original_file: str):
    return outdir.rstrip("/") + "/" + os.path.splitext(os.path.basename(original_file))[0] + ".pdf"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-o', '--out', nargs='?', help='Output directory', default="./", type=str)
    parser.add_argument('-f', '--file', nargs='?', help='File to process', type=str)
    parser.add_argument('-d', '--dir', nargs='?', help='Directory to process', type=str)

    args = parser.parse_args()

    if args.file is None and args.dir is None:
        print("At least --file or --dir must be provided.")
        exit(1)
    elif args.file is not None and args.dir is not None:
        print("--file and --dir must not be present at the same time.")
        exit(1)

    if not os.path.exists(args.out):
        os.makedirs(args.out)

    if args.file is not None:
        process(
            args.file,
            get_pdf_path(str(args.out), str(args.file))
        )
    else:
        for file in os.listdir(args.dir):
            extension = os.path.splitext(file)[1]
            if extension in [".md", ".yaml", ".yml"]:
                path = str(args.dir).rstrip("/") + "/" + file
                outpath = get_pdf_path(str(args.out), str(file))
                process(path, outpath)
