# The Office

![The-Office](/figures/michael-scott_quote.png)

**The Office** is an American mockumentary sitcom television series that depicts the everyday work lives of office employees at the Scranton, Pennsylvania, branch of the fictional Dunder Mifflin Paper Company.

## About

This project was executed in two distinct phases. Initially, I aimed to delve into and analyze the characteristics and sentiments of all the lines spoken by each character in the show. To achieve this, I began by scraping all the lines and quotes from [this website](https://www.officequotes.net/) using BeautifulSoup. This process allowed me to construct a dataframe and generate a CSV file. Subsequently, I conducted exploratory data analysis using pandas and seaborn, followed by sentiment analysis using the VADER package and Power BI.

![The-Office](/figures/dashboard-powerbi.png)

![The-Office](/figures/report_sentiment-powerbi-final.png)

In the subsequent phase, I aimed to leverage the dataset I had created to experiment with the [NanoGPT model](https://github.com/karpathy/nanoGPT), which was introduced by Andrej Karpathy. In [this tutorial](https://youtu.be/kCc8FmEb1nY), Karpathy walks through the process of constructing from scratch a baby GPT model, NanoGPT, in code and from the ground up and explains what is going on under the hood and what is at the core of chatGPT.

The methodology consists in training a small transformer-based language model. The original repository provides two options to train a baby GPT model: (1) a character-level transformer model, which basically models how characters follow each other and which character is going to come next; and (2) a word-based transformer model that predicts which term will come next.

* `model.py`, defines the GPT model
* `train.py`, train the model on any given text
* `prepare.py`, processes the data and convert it into a binary format for the training purpose
* `config`, folder with files where you can save all (hyper)parameters that are relevant to training
* `sample.py`, generate the sample text using the trained model

In this scenario, I've used all the scraped lines to build a text generator. Unlike the initial approach, I opted for the .csv file instead of the .txt file. I proceeded to train the model and subsequently experimented with it to generate various texts and ideas. While the results are intriguing, it’s important to note that they stem from a small model. The primary objective was experimentation rather than achieving optimal output. However, with a larger model, increased training capacity, and additional resources, this approach has the potential to yield significantly better results.

![The-Office](/figures/nanoGPT-output_b.png)

## Repository Overview

```
├── README.md
├── data
├── figures
├── nanoGPT
├── notebooks
└── web-scraping
```