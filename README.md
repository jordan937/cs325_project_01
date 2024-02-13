
    This is a python script for web scrapping. Using a text file with a list of URLs as input, it extracts the desired data(in this case the plain text of the article). It uses the Beautiful Soup library for parsing HTML content. The Requests library is used to take the HTML code by using HTTP requests. Then outputs each data from the URLs into separate files.

Installations Needed:
    Beautiful Soup Library
    Requests Library
    Python version 3.XX

Instructions:
    To use this software with the installations you need to use the command "conda env create -f requirement.yml" using the requirements.yml file in the repository to get the environment. You will also need a text file with URL links (one per line). The amount of links does not matter you can add/remove what you want. However if you would want to add or change it should be noted these articles were taken from the same site's section. So their layout of the articles would be the same. Which is the assumption this program uses to operate as seen on line 9. It is looking for the same id used in all the URLs. So if you wanted to change the urls they must have the same layout, and minor changes must be made to line 9-17. Besides the input you would also need to run the python file. The output will be separate files each containing the article text that was taken from a URL. The number of files corresponds with the number of files, in addition the names of the files depends on the order of the input list. For example, first URL on the list is article1.txt while the second is article2.txt and so on.
