#this file first creates the path for the output files that where specified
#then it calls the openFile using modA if urls is not null it loops through the result
#each loop it gets the article text by using the classes in modB then writes the result into the corresponging output file

from module_1 import function_01 as modA
from module_2 import function_02 as modB
import os

class ProjectManager:


    def FindPath(self):

        # Get the directory of the current folder
        # Ex: c:\Users\16187\cs325\project_01\CS325_p2
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the path from current folder to the input text file/output file
        self.output_raw = os.path.join(script_dir, "data", "raw")
        self.output_processed = os.path.join(script_dir, "data", "processed")
        
    

    def FindArticle(self):

        #calls openFile to open input file then assigns list of urls into the variable
        urls = modA.FileManager.openFile()

        if urls:
            # cycling through the urls and it's index calling the Webscrap function each time;
            for index, url in enumerate(urls):

                # assigns the article's paragraphs
                content = modB.WebScrap.article(url)
                raw_content = modB.WebScrap.rawArticle(url)

                if content:
                    #inputs the urls data into the corresponding output file
                    modA.FileManager.writeFile(self.output_processed, content, index, self.output_raw, raw_content)


def main():

    obj = ProjectManager()
    obj.FindPath()
    
    obj.FindArticle()
    
if __name__=="__main__":
    main()
