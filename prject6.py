from flask import *
from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='049840520ee14a2f850a7cfabdcc52dd')



app=Flask(__name__)
@app.route("/")
def hee():
    return render_template("newsa.html")


@app.route("/weather1",methods = ["POST","GET"])
def hee1():
    keyword=request.form["keyword"]
    top_headlines = newsapi.get_top_headlines(q=keyword,
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')
    articles=top_headlines["articles"]
    return render_template("newsa.html",result=articles)





if __name__=='__main__':
    app.run()
