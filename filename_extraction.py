import os

def main():
    with open('filenames.txt', 'w') as f:
        for dirpath, dirnames, files in os.walk('.'):
            for file in files:
                if file == '150427105828' or file == '150427105932':
                    f.write(file)
                    f.write('\n')



if __name__ == '__main__':
    main()