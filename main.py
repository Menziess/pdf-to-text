
import argparse
import PyPDF2
import os

def get_args():
  parser = argparse.ArgumentParser('app')
  parser.add_argument('path', type=str)
  return parser.parse_args()


def open_pdf_pages(path):
    abspath = os.path.abspath(path)
    with open(abspath, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        for page in pdf.pages:
            yield page


def write_text(filename, text):
    if text:
        with open(filename, 'w') as f:
            f.writelines(text)


def main(path):

    pages = open_pdf_pages(path)

    folder = 'pages'
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, page in enumerate(pages):
        filename = f'{folder}/page{i}.txt'
        print(f"Writing text to {filename}")
        write_text(filename, page.extractText())

    print("Done.")


if __name__ == "__main__":
    args = get_args()
    try:
        main(args.path)
    except KeyboardInterrupt:
        print("You stopped the program.")
