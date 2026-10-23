import argparse
def main():
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
if __name__ == "__main__":
    main()
