# Scraper for the Financial Times

Learning web scraping with beautiful soup.

### Set up

Dependencies 

- python
- bs4 (beautiful soup)

Check you have python installed

```bash
python --version
```

Install beautiful soup if not installed

```bash 
pip install bs4
```

### Run scraper 

Run the scraper and optionally pass command-line flags.

The default behaviour is to print the extracted article titles to the standard output.

```bash
python main.py [--test] [--mode] 
```

Scraping modes

```bash
# Print extracted article titles
python main.py

# Save extracted article titles to a summary file
python main.py --save-articles
```

Testing the scraper using user provided html files

```bash
# At least one html file must be provided when using the '--test' flag
# Print mode
python main.py --test [file1.html, ... , fileN.html]

# Save mode
python main.py --test --save-articles [file1.html, ..., fileN.html]
```


### Feature checklist
Key features
- [x] Grab all main stories that have the attribute `data-trackable-context-story-link="heading-link"`
- [x] Also extract titles and links to main stories 
- [x] Make a request to the website using the urllib library
- [x] Make a request to the /robots.txt endpoint to check if scraping is permitted

Output modes 
- [x] Add option to save parsed articles to a summary file 
- [x] Add option to print parsed articles to the terminal
- [x] Add option to make a test run using existing html files

More features
- [x] Print and save article titles in lexical order
- [x] Print the current datetime each time the scraper is run
- [ ] Add option to save articles links in addition to article titles

Data storage
- [ ] Save the result of each scrape in its own file named with its date
- [ ] Store files in the cloud using AWS S3 buckets
- [ ] Save results in a database
- [ ] Automate the scraper so it runs at scheduled times each day

Data analysis
- [ ] Find how many times different countries/groups of countries are mentioned in article titles across a fixed period of time.  
- [ ] Sentiment analysis of article titles using the VADER lexicon
- [ ] Maintain a monthly word count and determine the top 100 most frequent words used in article titles for each month.
### Sample article html structure

```html 
<a
data-trackable="heading-link"
data-trackable-context-story-link="heading-link"
href="/content/2a23cc70-3c3a-4e18-9020-a9bab70b07a3"
class="link"
target="\_self"
aria-describedby=""

> <span
    placeholder="headlineIndicator"
    class="headline-indicator"
    ><span
      class="icon icon--opinion icon--scale-3"
    >
      <span
        class="o-normalise-visually-hidden"
        >opinion content. </span
      ></span
    ><span
      class="text text--color-black text-display--scale-3 text--weight-600"
      id=""
      >The FT View.
    </span></span
> <span
    class="text text--color-black text-display--scale-3 text--weight-500"
    id=""
    >Tough economic realities await
    Britain’s next leader</span
> </a
```
