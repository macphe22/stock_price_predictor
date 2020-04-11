from SentimentAnalyzer import SentimentAnalyzer
import json
def main():
    sa = SentimentAnalyzer()
    # for each json calculate the sentiment for each day
    files = ['AAPL.json', 'AMZN.json', 'GOOGL.json', 'MSFT.json', 'TSLA.json']
    day_sentiment = {}
    for file in files:
        with open(file) as fp:
            for line in fp:
                if line == '\n':
                    continue
                s = len(line)
                data = json.loads(line)
                date = list(data.keys())[0]
                tweets = data[date]
                score = sa.analyze_day(tweets)
                # now create the dictionary to save all of the stuff and write to a new file
                # c = file[8:]
                c_name = file[:len(file) - 5]
                if date in day_sentiment:
                    if c_name in day_sentiment[date]:
                        day_sentiment[date][c_name] += score
                    else:
                        day_sentiment[date][c_name] = score
                else:
                    day_sentiment[date] = {}
                    day_sentiment[date][c_name] = score




    print(len(day_sentiment.keys()))
    with open('historicSentimentData.json', 'w') as outfile:
        json.dump(day_sentiment, outfile)
    # json.loads(data)



if __name__ == '__main__':
    main()




