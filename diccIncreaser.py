import sys

def process_file(file_path):
    new_file_path = file_path.rsplit('.', 1)[0] + '2.txt'
    print("Processing...")
    try:
        with open(file_path, 'r', encoding='utf-8') as original, open(new_file_path, 'w', encoding='utf-8') as new_file:
            unique_lines = set()

            for line in original:
                line = line.rstrip('\n')
                unique_lines.add(line)

                for n in range(len(line)):
                    if line[n].isalpha():
                        if line[n].isupper():
                            for i in range(100):
                                unique_lines.add(f"{line}{i:02d}")
                                unique_lines.add(f"{i:02d}{line}")
                            newline = line[:n] + line[n].lower() + line[n+1:]
                            unique_lines.add(newline)
                            for i in range(100):
                                unique_lines.add(f"{newline}{i:02d}")
                                unique_lines.add(f"{i:02d}{newline}")
                        else:
                            for i in range(100):
                                unique_lines.add(f"{line}{i:02d}")
                                unique_lines.add(f"{i:02d}{line}")
                            newline = line[:n] + line[n].upper() + line[n+1:]
                            unique_lines.add(newline)
                            for i in range(100):
                                unique_lines.add(f"{newline}{i:02d}")
                                unique_lines.add(f"{i:02d}{newline}")

                    else:
                        for i in range(100):
                            unique_lines.add(f"{line}{i:02d}")
                            unique_lines.add(f"{i:02d}{line}")

            for unique_line in unique_lines:
                new_file.write(f"{unique_line}\n")

        print(f"File processed successfully: {new_file_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python script.py file.txt")
    else:
        process_file(sys.argv[1])
