from sklearn.model_selection import GridSearchCV
from sklearn import svm
import numpy as np

stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","\"rt"]

tweets = []
for line in open('labelled_tweet.txt').readlines():
    # items = line.split(',')
    # tweets.append([int(items[0]), items[1].strip()])
    tweets.append(line.strip())

# Extract the vocabulary of keywords
features = dict()
for items in tweets:
    item = items.split(',')
    text = item[1].strip()
    for term in text.split():
        term = term.lower()
        if len(term) > 2 and term not in stopwords:
            if features.has_key(term):
                features[term] = features[term] + 1
            else:
                features[term] = 1

print '**********************************','\n',"Question 2:"
# Removing terms whose frequencies are less than  threshold 14
features = {term: freq for term, freq in features.items() if freq > 14}
print 'Length of the Features', len(features)
print 'Top 10 features in the Data',features
features = {term: idx for idx, (term, freq) in enumerate(features.items())}

print '**********************************','\n',"Question 3:"
X = []
y = []
for items in tweets:
    item = items.split(',')
    text = item[1].strip()
    class_label = int(item[0])
    x = [0] * len(features)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if features.has_key(term):
            x[features[term]] += 1
    y.append(class_label)
    X.append(x)
print 'X=', X
print 'X in a 2-D matrix format:'
print np.array(X)
print 'Length of X:',len(x)
print '1Y=',y
print 'Length of y',len(y)



print '**********************************','\n',"Question 4:"
svc = svm.SVC(kernel='linear')
Cs = range(1, 20)
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)
clf.fit(X, y)
print "SVM Model Accuracy is:" , clf.score(X,y)
print "The Best Parameter for SVM Model" ,clf.best_params_

print '**********************************','\n',"Question 5:"
tweets = []
for line in open('unlabelled_tweets.txt').readlines():
    tweets.append(line)
X = []
for text in tweets:
    x = [0] * len(features)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if features.has_key(term):
            x[features[term]] += 1
    X.append(x)
y = clf.predict(X)
print 'Best Fit',clf.fit(X,y)
print 'Prediction',clf.predict(X)
print 'Summation of y',sum(y)
print 'Length of y',len(y)
with open ('predicted_tweets.txt','w') as answer_result:
    idx=0
    for tweet in tweets:
        answer_result.write(str(y[idx])+ " "+tweet)
        idx=idx+1

print '*****************END****************'
