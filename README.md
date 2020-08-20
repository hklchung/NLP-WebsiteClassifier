[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)
![spacy 2.3.2](https://img.shields.io/badge/spacy-2.3.2-green.svg?style=plastic)
![nltk 3.4.5](https://img.shields.io/badge/nltk-3.4.5-green.svg?style=plastic)
![boilerpy3 1.0.2](https://img.shields.io/badge/boilerpy3-1.0.2-green.svg?style=plastic)
![textblob 0.15.3](https://img.shields.io/badge/textblob-0.15.3-green.svg?style=plastic)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=plastic)

<br />
<p align="center">
  <a href="https://github.com/hklchung/NLP-WebsiteClassifier">
    <img src="https://cdn.onlinewebfonts.com/svg/img_504359.png" height="100">
  </a>

  <h3 align="center">Website Classifier</h3>

  </p>
</p>

<p align="center">
  Classify web pages with NLP
    <br />
    <a href="https://github.com/hklchung/NLP-WebsiteClassifier"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hklchung/NLP-WebsiteClassifier">View Demo</a>
    ·
    <a href="https://github.com/hklchung/NLP-WebsiteClassifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/hklchung/NLP-WebsiteClassifier/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact](#contact)
* [Known Issues](#known-issues)

<!-- ABOUT THE PROJECT -->

## About the Project
In this project we built a function that leverages various Natural Language Processing (NLP) techniques to extract web content from a user provided URL and classify the web content based on a list of known topics. For simplicity, We will be using boilerpy3 to help us extract only the relevant text data from a given URL, apply transfer learning with Spacy's english language model for word similarity comparison and finally nltk for lammetization.

The idea is to leverage the function built here to support other work such as feature generation for modelling work and insight analytics. 

<!-- GETTING STARTED -->

## Getting Started
To get started, please follow the below guidelines on prerequisites and installation.

<!-- PREREQUISITES -->

### Prerequisites
* Spacy==2.3.2
* NLTK==3.4.5
* Boilerpy3==1.0.2
* TextBlob==0.15.3
* Pandas==1.0.3
* Numpy==1.18.2

<!-- INSTALLATION -->

### Installation
1. Fork and star this repo ;)
2. Create a folder on your machine for your project
2. Inside the folder right-click and select Git Bash Here
3. Git clone this repo into the folder by running the below command
```sh
git clone https://github.com/hklchung/NLP-WebsiteClassifier.git
```

<!-- USAGE -->

## Usage
1. First run everything inside main.py --this will help you load all the required packages and load the functions needed
2. If you never had Spacy before, you may have to download the Spacy English language model first by running the below in Git Bash or Terminal:
```sh
python -m spacy download en_core_web_md
```
3. Run this in console: nltk.download('popular')
4. Update the list of topics if needed
5. Run this in console: classify_web(url, topics = topics)

Sentiment analysis capability has also been added to support users to understand the sentiment in web pages. You can retrieve sentiment analysis results by changing the analyse_sentiment argument to True in the function. 
  
<!-- CONTRIBUTING -->

## Contributing
I welcome anyone to contribute to this project so if you are interested, feel free to add your code.
Alternatively, if you are not a programmer but would still like to contribute to this project, please click on the request feature button at the top of the page and provide your valuable feedback.

<!-- CONTACT -->

## Contact
* [Leslie Chung](https://github.com/hklchung)

<!-- KNOWN ISSUES -->

## Known Issues
* Websites that lack any text content will not return any results

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hklchung/NLP-WebsiteClassifier.svg?style=flat-square
[contributors-url]: https://github.com/hklchung/NLP-WebsiteClassifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hklchung/NLP-WebsiteClassifier.svg?style=flat-square
[forks-url]: https://github.com/hklchung/NLP-WebsiteClassifier/network/members
[stars-shield]: https://img.shields.io/github/stars/hklchung/NLP-WebsiteClassifier.svg?style=flat-square
[stars-url]: https://github.com/hklchung/NLP-WebsiteClassifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/hklchung/NLP-WebsiteClassifier.svg?style=flat-square
[issues-url]: https://github.com/hklchung/NLP-WebsiteClassifier/issues
