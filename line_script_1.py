from hashlib import md5


def generate_str_hash(path):
    with open(path, 'rb') as f:
        current_file = f
        while True:
            current_line = current_file.readline()
            if not current_line:
                break
            line_hash = md5(current_line).hexdigest()
            yield line_hash


for i in generate_str_hash("D:\\Netology\\encode.SCH"):
    print(i)




