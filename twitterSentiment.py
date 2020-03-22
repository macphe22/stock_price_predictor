from SentimentAnalyzer import SentimentAnalyzer
import json
def main():
    sa = SentimentAnalyzer()
    # for each json calculate the sentiment for each day
    files = ['realTimeAAPL.json', 'realTimeAMZN.json', 'realTimeGOOGL.json', 'realTimeMSFT.json', 'realTimeTSLA.json']
    day_sentiment = {}
    for file in files:
        with open(file) as fp:
            for line in fp:
                s = len(line)
                data = json.loads(line)
                date = list(data.keys())[0]
                tweets = data[date]
                score = sa.analyze_day(tweets)
                # now create the dictionary to save all of the stuff and write to a new file
                c = file[8:]
                c_name = c[:-5]
                if date in day_sentiment:
                    if c_name in day_sentiment[date]:
                        day_sentiment[date][c_name] += score
                    else:
                        day_sentiment[date][c_name] = score
                else:
                    day_sentiment[date] = {}
                    day_sentiment[date][c_name] = score




    print(day_sentiment)
    with open('sentimentData.json', 'w') as outfile:
        json.dump(day_sentiment, outfile)
    # json.loads(data)



if __name__ == '__main__':
    main()




