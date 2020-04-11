class SentimentAnalyzer:
    def __init__(self):
        self.positive_words = self.get_words('positive-words.txt')
        self.negative_words = self.get_words('negative-words.txt')

    def get_words(self, file):
        '''
        :param file: filename to be parsed
        :return: Set of words in file
        '''
        filename = 'opinion-lexicon-English/' + file
        fp = open(filename, encoding="ISO-8859-1")
        word_set = set()
        for line in fp:
            try:
                if line[0].isalpha():
                    word_set.add(line.strip())
            except:
                continue
        return word_set

    def analyze_line(self, line):
        '''
        calculates the sentiment score for a line
        :param line: line of text we are trying to assess
        :return: sentiment score for that line
        '''
        score = 0
        line = line.strip().split()
        for word in line:
            if word.lower() in self.positive_words:
                score += 1
            elif word.lower() in self.negative_words:
                score -= 1
        return score

    def analyze_day(self, tweets):
        '''
        Calculates the stocks sentiment for that day
        :param tweets: A list representing the tweets 'text' for that day
        :return: score for that day
        '''
        overall_score = 0
        count = 0
        for tweet in tweets:
            overall_score += self.analyze_line(tweet)
            count += 1
        return overall_score/count
