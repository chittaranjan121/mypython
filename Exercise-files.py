import os
from datetime import datetime
directory='Exercise'
filenames=os.listdir(directory)

for filename in filenames:
    print(filename)
    if 'txt' in filename:
        filepath=os.path.join(directory,filename)

        with open(filepath,'r') as file:
            content=file.read()
            words=content.split()
            word_counts=len(words)
            print(word_counts)
        day=datetime.now().strftime("%A")
        new_filename=f'{filename[:-4]}--{word_counts}--{day}.txt'

        new_filepath=os.path.join(directory,new_filename)
        os.rename(filepath,new_filepath)
        print(f"Renamed is done for {filename} to new file name {new_filename}")







