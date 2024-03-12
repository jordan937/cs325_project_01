#follows the Single Responsibility Principle which makes the code easier to understand, maintain, and modify
#FileManager's responsibility is to manage the files but seperates the tasks of opening/writing a file
#openFile is called to the input file open the file then stores all the lines in a list and returns it
#writeFile is called the path to the output file stores that data for that folder, index which is only used to name the files...
    #and content which is the article text that is written into the designated file


import os
class FileManager:

    def openFile():
        # Read the list of URLs from the text file
        # note: stores urls in input text file into variable "urls" as a list
        with open("url.txt", 'r') as file:
            urls = (file.readlines())
    
        return urls
    
    def writeFile(outputFile, content, index, outputRaw, content_raw):

        with open(os.path.join(outputFile, f'article{index + 1}.txt'), 'w') as content_file:
                # writes article text into assigned text file
                content_file.write(content)

        with open(os.path.join(outputRaw, f'raw{index + 1}.txt'), 'w') as raw_file:
            raw_file.write(content_raw)
    