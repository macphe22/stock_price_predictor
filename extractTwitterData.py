import json
import re

def collect_company_tweets(keywords, tweet, company_tweets):
    # company_tweets = []
    # print(tweet['text'])
    for keyword in keywords:
        # print(keyword)
        regex = re.compile(keyword)
        try:
            if regex.search(tweet['text']):
                # add the tweet to the dictionary
                created_at = tweet['created_at'].split()
                date = ''
                for i in range(3):
                    date += created_at[i] + ' '
                date += created_at[5]
                if date in company_tweets:
                    company_tweets[date].append(tweet['text'])
                else:
                    company_tweets[date] = [tweet['text']]
                # company_tweets.append(tweet)
                break
        except KeyError:
            return
    # return company_tweets


def write_to_json(company_tweets, name):
    outfile = open(name+'.json', 'a')
    for key, value in company_tweets.items():
        json_object = json.dumps({key: value})
        outfile.write(json_object)
        outfile.write('\n')
    outfile.close()



def main():
    filenames_fp = open('filenames.txt')
    count = 0
    microsoft_tweets = {}
    apple_tweets = {}
    amzn_tweets = {}
    googl_tweets = {}
    tsla_tweets = {}
    keywords = [r"[#]?[Mm]icrosoft", r"[#]?(MSFT|msft)", r"[#]?[Ss]urface[ ]*Pro", r"[#]?[Ww]indows([ ]?10)?",
                "[#]?Microsoft[ ]*Office", "[#]?Xbox", "[#]?[Mm]icrosoft[ ]*[Ss]urface[ ]*[Ss]tudio"]
    am_keywords = [r'[#]?[Aa]mazon', r'[#]?(AMZN|amzn)', r'[#]?[Kk]indle', r'[#]?[Aa]mazon[ ]*[Ww]eb[ ]*[Ss]ervice', r'[#]?[Pp]rime']
    app_keywords = [r'iPhone', r'[#]?Macbook', r'[Aa]pple[ ]?[Mm]usic', r'[Aa]irpods( [Pp]ro)?', r'iMac',
                    r'(AAPL|aapl)']
    googl_keywords = [r'[Gg]oogle [Pp]ixel', r'[Gg]oogle[d]?', r'(GOOGL|googl)']
    tsla_keywords = [r'(TSLA|tsla)', r'[Mm]odel ([Ss]|[Xx])', r'[Tt]esla']
    for file in filenames_fp:
        twitter_file = '/user/research/ptan/data/Twitter/' + file
        print("Working with file: ", twitter_file, '{:d}/1000'.format(count))
        if count % 4 == 0:
            with open(file.strip()) as f:
                # tweets = [json.loads(line) for line in f]
                for line in f:
                    # print(line)
                    if line != "\n":
                        try:
                            tweet = json.loads(line)
                        except:
                            continue
                        # print(tweet)
                        try:
                            # print(tweet['text'])
                            word_set = set()
                            for word in tweet['text']:
                                word_set.add(word)
                            collect_company_tweets(keywords, tweet, microsoft_tweets)
                            collect_company_tweets(app_keywords, tweet, apple_tweets)
                            collect_company_tweets(am_keywords, tweet, amzn_tweets)
                            collect_company_tweets(googl_keywords, tweet, googl_tweets)
                            collect_company_tweets(tsla_keywords, tweet, tsla_tweets)
                            # for keyword in keywords:
                            #     # print(keyword)
                            #     regex = re.compile(keyword)
                            #     if regex.search(tweet['text']):
                            #         microsoft_tweets.append(tweet)
                        except KeyError:
                            continue
        count += 1
        if count > 1000:
            print("File left off on:", file)
            break

    write_to_json(microsoft_tweets, 'MSFT')
    write_to_json(apple_tweets, 'AAPL')
    write_to_json(amzn_tweets, 'AMZN')
    write_to_json(tsla_tweets, 'TSLA')
    write_to_json(googl_tweets, 'GOOGL')



if __name__ == '__main__':
    main()