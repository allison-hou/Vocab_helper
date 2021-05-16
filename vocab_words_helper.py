FILE_PATH = 'en.txt'
OUTPUT_PATH = 'output.txt'

with open(FILE_PATH) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines.sort()

with open(OUTPUT_PATH, 'w') as f:
    f.write('\n'.join(lines)) 
