import argparse
from pinter.dataset import load_files


def main():
    parser = argparse.ArgumentParser(description="Pick up intersection of pairs")
    parser.add_argument("-i", "--input-files", nargs="+", default=[], required=True)
    parser.add_argument("-o", "--output-file", required=True)

    args = parser.parse_args()

    dataset = load_files(args.input_files)
    dataset.create_intersection()
    dataset.to_dat(args.output_file)


if __name__ == "__main__":
    main()
