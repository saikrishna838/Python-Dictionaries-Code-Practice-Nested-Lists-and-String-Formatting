def print_char_count(line):
    line = line.lower()
    unique_chars = set(line)
    unique_chars.discard(" ")
    
    for char in sorted(unique_chars):
        msg = "{char}: {count}"
        print(msg.format(char = char, count = line.count(char)))
        

line = input()
print_char_count(line)