import argparse
import pinter as pig


def main():
    parser = argparse.ArgumentParser(description="Pick up intersection of pairs")
    parser.add_argument("-i", "--input-files")
    parser.add_argument("-o", "--output-file")

    args = parser.parse_args()

    dataset = pig.load_files(args["input-files"])
    dataset.create_intersection()
    dataset.to_dat(args["output-file"])


if __name__ == "__main__":
    main()
