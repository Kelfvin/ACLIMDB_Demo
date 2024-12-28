import kagglehub


def main():
    # Download latest version
    path = kagglehub.dataset_download("yuexincui/acllmdb", path="./data")
    print("Path to dataset files:", path)


if __name__ == "__main__":
    main()
