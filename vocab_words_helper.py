import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        print('[USAGE] python vocab_words_helper.py <input_file_path> <output_file_path> <question_output_path>')      
       
    FILE_PATH = args[1]
    OUTPUT_PATH = args[2]
    QUESTION_PATH = args[3]
    
    with open(FILE_PATH) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines.sort()

    with open(OUTPUT_PATH, 'w') as f:
        f.write('\n'.join(lines)) 
    
    with open(QUESTION_PATH, 'w') as f:
        questions = []
        for line in lines:
            questions.append(line[0] + '_____' + line[-1])
        f.write('\n'.join(lines))
