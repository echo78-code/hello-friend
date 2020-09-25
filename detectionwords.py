print ('')

def detectwhat(param):
    keywords = ['what\'s', 'what']
    for word in keywords:
        if(word in str(param)):
            return 'found'

# def removeStopwords(param):
#     stopwords = ['is', 'am', 'are', 'in', 'right now', 'what', 'what\'s']
#     querywords = param.split()
#     resultwords  = [word for word in querywords if word.lower() not in stopwords]
#     result = ' '.join(resultwords)
#     return result
