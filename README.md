# Customer Sentiment Analysis for Restaurant Reviews

This project uses machine learning to analyze customer reviews and predict whether the sentiment is positive or negative. The model is built using a dataset of restaurant reviews and is deployed through a simple web interface built with Streamlit.

---

## 🗂️Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

---

## Overview

This project allows users to input restaurant reviews and get a prediction on whether the sentiment of the review is positive or negative. It uses a pre trained machine learning model to make predictions based on the input text.

The model is trained using a dataset of restaurant reviews with ratings. We created a web interface using Streamlit where users can input their reviews and see the result.

---

## Requirements

Make sure you have the following libraries installed before running the project:

- Python 3.x
- `streamlit` - for the web interface
- `scikit-learn` - for machine learning
- `pandas` - for handling data

To install the required libraries, you can use the following command:

```bash
pip install streamlit scikit-learn pandas
```

---

## 🛠️Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/restaurant-sentiment-analysis.git
```

2. Navigate into the project directory

```bash
cd restaurant-sentiment-analysis
```

3. Once you've set up the project and installed the requirements, you can run the Streamlit app with the following command:

```bash
streamlit run sentiment_analysis_web_portal.py
```

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE tab on the top for more details.

---