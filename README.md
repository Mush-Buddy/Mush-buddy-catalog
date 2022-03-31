# Mush-buddy-catalog

Python web crawler with Selenium 

### The web crawler is in .ipynb file using anaconda 


### installing selenium
- to use: install selenium on anaconda
-     https://www.tutorialspoint.com/how-to-install-selenium-package-in-anaconda
-     conda install -c conda-forge selenium

### installing anaconda and jupyter
- Install Anaconda and jupyter
-   If you need help: https://test-jupyter.readthedocs.io/en/latest/install.html


### installing chromedriver
- Must havee google chrome as well (app store)
- store chrome driver inside the folder
- https://chromedriver.chromium.org

#### Now one should be able to run

Main function is now inside the wiki_crawler folder titles "MAIN_crawler"
Now, you can open the main file and press run all but *warning*
It will run for 15 hours scraping the web for all the mushrooms in our list


#### other files inside wiki_crawler
- there should exist:
-   tsv
-   pkl
-   catalog.pkl which holds the original list that is not our own
-   
### Structures
- mushroom objects with characteristic traits
- small functions to find specific parts when given a specific website
- one main function that scrapes one page and searches for all the parts in the page
- and an overall function that goes through the list and calls the sub functions for each page
-   this function makes a dictionary and returns it with a list of failed mushrooms

- Other functions
-   conversion the dictionary to tsv
-   conversion tsv to pkl
