import twitter, sys, json

reload(sys)
sys.setdefaultencoding("utf-8")


myApi = twitter.Api(consumer_key='PjYAex5Do7e4ldslfFqj8rcmB',
                  consumer_secret='MHrbXAukQ5wYgyXM9QWX4qys19uzHFo7gL9V3VqKYxJFSWDgK0',
                  access_token_key='84782380-zFrkL16EB71T0gkdQVieyYNa74zIt2brnbom1y2P1',
                  access_token_secret='OsWIkDSET0CefBnMgHRRdYKuxezPZEqr7v9r0vPrH7fay')

query = 'accident OR traffic OR congestion OR roadblock OR slowtraffic'

def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet['id']
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
        print 'Tweet Text: ', tweet['text']
    except:
        pass



def rest_query():
    print 'in rest query'
    file_user_ids = open('M_user_id.txt.txt','w')
    file_tweet_id = open('M_tweet_id.txt','w')
    file_tweets = open('M_tweets_all.txt','w')
    geo = [38.9071923, -77.03687070000001, "500mi"]  # City of Washington DC
    count=0
    MAX_ID = None
    tweets = [json.loads(str(raw_tweet)) for raw_tweet
              in myApi.GetSearch(term = query, geocode = geo, count = 100, result_type='recent', max_id=MAX_ID)]
    for tweet in tweets:
        # print_info(tweet)
        count+=1
        file_user_ids.write(json.dumps(tweet['user']['id']) + '\n')
        file_tweet_id.write(json.dumps(tweet['id'])+'\n')
        file_tweets.write(json.dumps(tweet)+'\n')
    file_tweets.close()
    file_user_ids.close()
    file_tweet_id.close()
    print 'Total Number is ',count
    print 'rest query finished'


def rest_user_timeline():
    print('in timeline')
    users_id= [user.rstrip('\n') for user in open('M_user_id.txt')]
    file_tweet_id = open('D_tweet_ids.txt','w')
    file_tweets = open('D_tweets_all.txt','w')
    count = 0
    for user in users_id:
        tweets = myApi.GetUserTimeline(user)
        # I trimmed it down to 5 tweets per user else I was getting 20weets per user timeline
        # and that would have created 2000 tweets as D'
        for tweet in list(tweets)[0:5]:
        # for tweet in tweets:
            # print_info(tweet
            if str(tweet.id) and str(tweet.text):
                count+=1
                file_tweet_id.write(str(tweet.id)+'\n')
                file_tweets.write(str(tweet)+'\n')
    file_tweets.close()
    file_tweet_id.close()
    print 'Total number is ',count
    print 'timeline finished'

def label_m():
    print 'Labeling Started'
    tweets = [json.loads(raw_tweets.rstrip('\n')) for raw_tweets in open('M_tweets_all.txt')]
    file = open('M_labeled.txt','w')
    for tweet in tweets:
        print query
        print tweet['text']
        first = raw_input('First Label\n')
        print first
        second = raw_input('Second Label\n')
        print second
        complete = str(tweet['id']) + ',' +str(first)+','+str(second)
        file.write(str(complete+'\n'))
        print '************************\n\n'
    print 'Labeling Finished'

def label_d():
    print 'D Labelling Started'
    tweets = [json.loads(raw_tweets.rstrip('\n')) for raw_tweets in open('D_tweets_all.txt','r')]
    file = open('D_labelled.txt','w')
    for tweet in tweets:
        first = raw_input('First Label\n')
        print first
        second = raw_input('Second Label\n')
        print second
        complete = str(tweet['id']) + ',' +str(first)+','+str(second)
        file.write(str(complete+'\n'))

    print 'D Labelling Ended'


def main():
    print "\n\n************ Rest Query ****************\n\n"
    rest_query()
    rest_user_timeline()
    # label_m()
    # label_d()

if __name__ == '__main__':
    main()
