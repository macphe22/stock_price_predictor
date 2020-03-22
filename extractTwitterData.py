import json
import re

def main():
    filenames_fp = open('filenames.txt')
    count = 0
    for file in filenames_fp:
        twitter_file = '/user/research/ptan/data/Twitter/' + file
        print("Working with file: ", twitter_file)
        if (count % 4) == 0:
            with open(file.strip()) as f:
                # tweets = [json.loads(line) for line in f]
                microsoft_tweets = []
                keywords = [r"[#]?[Mm]icrosoft", r"[#]?(MSFT|msft)", r"[#]?[Ss]urface[ ]*Pro", r"[#]?[Ww]indows([ ]?10)?", "[#]?Microsoft[ ]*Office", "[#]?Xbox", "[#]?[Mm]icrosoft[ ]*[Ss]urface[ ]*[Ss]tudio"]
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
                            for keyword in keywords:
                                # print(keyword)
                                regex = re.compile(keyword)
                                if regex.search(tweet['text']):
                                    microsoft_tweets.append(tweet)
                        except KeyError:
                            continue
                        # print(tweet['text'])
                microsoft_dict = {}
                for tweet in microsoft_tweets:
                    created_at = tweet['created_at'].split()
                    # print(created_at)
                    date = ''
                    for i in range(3):
                        date += created_at[i] + ' '
                    date += created_at[5]
                    if date in microsoft_dict:
                        microsoft_dict[date].append(tweet['text'])
                    else:
                        microsoft_dict[date] = [tweet['text']]
                # print(microsoft_dict)
                json_object = json.dumps(microsoft_dict)
                twitter_outfile = open('MicrosoftTweets.json', 'a')
                if microsoft_dict:
                    twitter_outfile.write(json_object)
                    twitter_outfile.write('\n')
                twitter_outfile.close()
                count += 1


if __name__ == '__main__':
    main()