from textblob import TextBlob as TB
testy="Hi i am very happy to meet you. I am Akarshan"
testy="Hi i am not happy at all. Indeed i am very very sad"
testy="Top Sportswomen of India behaving like an IT Cell, copy pasting propaganda tweets blindly. What a shameful thing to see.."
testy="good bad"
testy="I deeply regret some of you"
textsentiment=TB(testy)
a=textsentiment.sentiment_assessments
b=textsentiment.polarity
print(a)