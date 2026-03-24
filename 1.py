def copy_text(source_file_name: str, dest_file_name: str) -> None:
    with open(source_file_name, "r") as source_file, \
         open(dest_file_name, "a") as dest_file:
        
        for line in source_file:
            dest_file.write(line)


def main():
    source_file = "/home/aleksey/Documents/file1"
    dest_file = "/home/aleksey/Documents/file2"
    copy_text(source_file, dest_file)


if __name__ == "__main__":
    main()
