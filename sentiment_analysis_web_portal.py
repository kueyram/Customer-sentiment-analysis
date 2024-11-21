#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Setting up the Streamlit interface
st.title("Customer Sentiment Analysis of Restaurant Reviews")
st.write(
    "Enter a restaurant review to get a sentiment prediction (Positive/Negative)."
)

# Input field for the review
review_text = st.text_area("Enter the Review:")

# Button to trigger the prediction
if st.button("Predict Sentiment"):
    if review_text:
        result = predict_sentiment(review_text)
        st.write(f"The sentiment of the review is: **{result}**")
    else:
        st.write("Please enter a review.")

