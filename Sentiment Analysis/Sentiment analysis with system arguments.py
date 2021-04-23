import nltk
import sys
import pyperclip
a = sys.argv[1]
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
scores = sid.polarity_scores(a)
count = scores['compound']
if count > 0:
    body = "Thats good! We appreciate the feedback. Expect another response from a support rep soon"
    pyperclip.copy(body)
elif count < 0:
    body = "We\'re sorry to hear that!. We just forwarded your request to the appropriate person in support, expect a response shortly"
    pyperclip.copy(body)
else:
    body = "We are forwarding your question to the appropriate person in support, Will get back to you shortly"
    pyperclip.copy(body)

