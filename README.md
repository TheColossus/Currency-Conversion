Hello There.

This is my first big(ish) project that I made using python. It's a web scraping program that takes data from https://finance.yahoo.com/currencies/ and stores them in a dictionary. Then it asks the viewer a few questions regarding converting between two currencies, and the amount they would like to convert. It outputs the equivalent value in the desired currency.

I learned some things while making this project. Firstly, I had to learn how to use Selenium Webdriver, an API that allows a program to natively browse the web. In this project, I used a Chrome webdriver. Originally, I planned on using a different API, namely Beautiful Soup, as I found it very easy to understand. Upon trying this however, it became apparent that it would not work due to one main reason, the fact that the data I wanted to scrape was dynamic.

At the time, I did not know of static and dynamic elements of webpages, so I was stumped, but upon doing further research, I concluded that the real time currency values I was trying to scrape were dynamic, as they were continually being updated from some backend server-side stuff (I think). 

To my understanding, Beautiful Soup does not work since when the page is requested through the requests library, it does not execute any Javascript since it does not read the interactions between the DOM and Javascript. All Beautiful Soup does is pull the data out of HTML and XML files and makes it pythonic, so it would work well for static pages, but not dynamic.

Anyways, I had to instead use Selenium, which opens up the browser natively through the program, allowing the dynamic elements to load and be read.

Other than learning to use Selenium, I think I better understand dictionaries and when I should be using them as opposed to other structures such as lists.

This project is pretty bare in the sense that there is no user interface and no exception handling. As I am busy with college right now, this is a task for another day.

Thanks for listening to me ramble. :)
