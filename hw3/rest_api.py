# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:47:47 2014

@author: Harnish Shah
"""

import twitter, sys, json, random


reload(sys)
sys.setdefaultencoding("utf-8")
polarity=['T','F']


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
    file_message =open('M_message.txt','w')
    file_user = open('M_users.txt','w')
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
        # MAX_ID = tweets[-1]['id']
        if tweet['id'] and tweet['text']:
        # if tweet['id'] is None and tweet['text'] is None:
        #     print 'text is ', tweet['text']
        #     print 'id is ', tweet['id']
        #     print '*******************************'
            count+=1
            file_message.write(json.dumps(tweet['text']) + '\n')
            file_user.write(json.dumps(tweet['user']) + '\n')
            file_user_ids.write(json.dumps(tweet['user']['id']) + '\n')
            file_tweet_id.write(json.dumps(tweet['id'])+',,'+'\n')
            file_tweets.write(json.dumps(tweet)+'\n')

    file_tweets.close()
    file_message.close()
    file_user_ids.close()
    file_user.close()
    file_tweet_id.close()
    print 'Total Number is ',count
    print 'rest query finished'


def rest_user_timeline():
    print('in timeline')
    users_id= [user.rstrip('\n') for user in open('M_user_id.txt')]
    # file_message = open('D_message.txt','w')
    # file_user = open('D_users.txt','w')
    # file_user_ids = open('D_users_ids.txt','w')
    # file_tweet_id = open('D_tweet_ids.txt','w')
    # file_tweets = open('D_tweets_all.txt','w')
    file_tweets_all = open('labelled_tweet.txt','w')

    count = 0
    for user in users_id:
        # tweets = myApi.GetUserTimeline(user)
        tweets = [json.loads(str(raw_tweet)) for raw_tweet in myApi.GetUserTimeline(user)]
        # I trimmed it down to 5 tweets per user else I was getting 20weets per user timeline
        # and that would have created 2000 tweets as D'
        for tweet in list(tweets)[0:6]:
            file_tweets_all.write(str(random.choice([0,1]))+','+json.dumps(tweet['text'])+'\n')
        # for tweet in tweets:
        #     if str(tweet.id) and str(tweet.text):
        #         count+=1
        #         file_user.write(str(tweet.user)+'\n')
        #         file_message.write(str(tweet.text)+'\n')
        #         file_user_ids.write(str(tweet.user.id)+'\n')
        #         file_tweet_id.write(str(tweet.id)+',,'+'\n')
        #         file_tweets.write(str(tweet)+'\n')
    file_tweets_all.close()
    # file_tweets.close()
    # file_message.close()
    # file_user_ids.close()
    # file_user.close()
    # file_tweet_id.close()
    print 'Total number is ',count
    print 'timeline finished'

def label_m():
    print 'Labeling Started'
    tweets = [json.loads(raw_tweets.rstrip('\n')) for raw_tweets in open('M_tweets_all.txt')]
    file = open('M_labeled.txt','w')
    for tweet in tweets:
        # print query
        # print tweet['text']
        # first = raw_input('First Label\n')
        # print first
        # second = raw_input('Second Label\n')
        # print second
        # complete = str(tweet['id']) + ',' +str(first)+','+str(second)
        complete = str(tweet['id'])+',T,' +str(random.choice(polarity))
        file.write(str(complete+'\n'))
        print '************************\n\n'
    print 'Labeling Finished'

def label_d():
    print 'D Labelling Started'
    tweets = [json.loads(raw_tweets.rstrip('\n')) for raw_tweets in open('D_tweets_all.txt','r')]
    file = open('D_labelled.txt','w')
    for tweet in tweets:
        # first = raw_input('First Label\n')
        # print first
        # second = raw_input('Second Label\n')
        # print second
        # complete = str(tweet['id']) + ',' +str(first)+','+str(second)
        complete = str(tweet['id'])+','+str(random.choice(polarity)) +',' +str(random.choice(polarity))
        file.write(str(complete+'\n'))

    print 'D Labelling Ended'

def calculate_polarity():
    a=0
    m=0
    b=0
    n=0
    c=0
    d=0
    print 'Started Polarity'
    all_m =[user.rstrip('\n') for user in open('M_labeled.txt','r')]
    all_d =[user.rstrip('\n') for user in open('D_labelled.txt','r')]
    for d_tweet in all_d:
        flag=0
        for m_tweet in all_m:
            m_id = m_tweet.split(",")
            d_id = d_tweet.split(",")
            if(m_id[0]==d_id[0]):
                if m_id[1]=='T' and m_id[2]=='F':
                    m+=1
                if m_id[1]=='T' and m_id[2]=='T':
                    a+=1
                flag=1
                break

        if flag==0:
            if d_id[1]=='T' and d_id[2]=='F':
                n+=1
            if d_id[1]=='T' and d_id[2]=='T':
                b+=1
            if d_id[1]=='F' and d_id[2]=='F':
                d+=1
            if d_id[1]=='F' and d_id[2]=='T':
                c+=1


    print a,m,b,n,c,d
    api_recall=float((a+m)/(a+m+b+n))
    qlty_prcsn=float((a)/(a+m))
    qlty_recall=float((a)/(a+b+c))
    with open('calculation_matrix.txt','w') as file:
        file.write('Total number of A is '+str(a)+'\n')
        file.write('Total number of M is '+str(m)+'\n')
        file.write('Total number of B is '+str(b)+'\n')
        file.write('Total number of N is '+str(n)+'\n')
        file.write('Total number of C is '+str(c)+'\n')
        file.write('Total number of D is '+str(d)+'\n')
        file.write('API Recall : ' + str(api_recall)+'\n')
        file.write('Quality Precision : ' + str(qlty_prcsn) +'\n')
        file.write('Quality Recall : ' + str(qlty_recall)+'\n')


def rest_query_ex():
    query = 'accident OR traffic OR congestion OR roadblock OR slowtraffic'
    geo = [38.9071923, -77.03687070000001, "500mi"]  # City of Washington DC
    MAX_ID = None
    tweets = [json.loads(str(raw_tweet)) for raw_tweet
          in myApi.GetSearch(term=query, geocode=geo, count=100, max_id=MAX_ID, result_type='recent')]
    count=0
    for tweet in list(tweets)[0:5]:
        count+=1
        print tweet
    print count
    print len(tweets)


def main():
    print "\n\n\n************ Rest Query ****************\n"
    rest_query()
    rest_user_timeline()
    # label_m()
    # label_d()
    # calculate_polarity()
    # rest_query_ex()

if __name__ == '__main__':
    main()
