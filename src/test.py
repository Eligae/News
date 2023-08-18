import json
from textblob import TextBlob
with open('.\\src\\articleTest.json', 'r') as f:
    json_data = json.load(f)
    msg = json_data["message"]["result"]["translatedText"]
    
    blob = TextBlob(msg)
    sentimentScore = blob.sentiment.polarity
    print(sentimentScore)


