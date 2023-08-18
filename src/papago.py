import var
import os
import sys
import urllib.request
from textblob import TextBlob

# client data var에 저장
def clientData(clientId, clientSecret):
    var.clientId = clientId
    var.clientSecret = clientSecret

def toEng(text):
    encText = urllib.parse.quote(text)
    data = var.data + encText
    request = urllib.request.Request(var.NaverOpenAPIUrl)
    request.add_header("X-Naver-Client-Id", var.clientId)
    request.add_header("X-Naver-Client-Secret", var.clientSecret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return rescode

def sentimental(msg):
    blob = TextBlob(msg)
    sentimentScore = blob.sentiment.polarity
    return sentimentScore
