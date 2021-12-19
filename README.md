# The Office

![The-Office](https://artesettima.it/wp-content/uploads/2021/01/top-of-story-michael-scott-image.jpg)

Repository containing multiple projects regarding NBC's mockumentary 'The Office'.

-- Project status: [Active]

## About & Motivation

I'm a fan of The Office and I wanted to use related data to dive deeper into the data science field and to experiment with some tools and technologies.

## Methods & Results

<!-- (Provide more detailed overview of the project. Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing? Feel free to number or bullet point things here) -->

I started by scraping all the quotes from [this website](https://www.officequotes.net/), building in this way a dataframe and a csv file.

Next, I've computed some basic exploratory analysis with pandas and seaborn.

Contents:

- Web Scraping

Web scraping of all quotes from 'The Office'.

[Website link](https://www.officequotes.net/)

Libraries: requests, BeautifulSoup, Pandas

- Notebooks

<!-- Second, summarize your results concisely. Make use of subheaders where appropriate. -->

## Repository overview

```
├── README.md
├── data
│   ├── the-office_lines.csv
├── web-scraping
│   ├── scraper.py
└── notebooks
    ├── theoffice.ipynb
    ├── x
    └── x
```

## Acknolewdgments & Inspiration

- [Dan Blevins](github.com/danblevins)
- officequotes.net