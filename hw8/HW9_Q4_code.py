

import numpy as np
from hmmlearn import hmm
import warnings, os

warnings.filterwarnings("ignore")

class markovmodel:
    def __init__(self, transmat = None, startprob = None):
        self.transmat = transmat
        self.startprob = startprob
    def fit(self, X):
        ns = max([max(items) for items in X]) + 1
        self.transmat  = np.zeros([ns, ns])
        self.startprob = np.zeros([ns])
        for items in X:
            n = len(items)
            self.startprob[items[0]] += 1
            for i in range(n-1):
                self.transmat[items[i], items[i+1]] += 1
        self.startprob = self.startprob / sum(self.startprob)
        n = self.transmat.shape[0]
        d = np.sum(self.transmat, axis=1)
        for i in range(n):
            if d[i] == 0:
                self.transmat[i,:] = 1.0 / n
        d[d == 0] = 1
        self.transmat = self.transmat * np.transpose(np.outer(np.ones([ns,1]), 1./d))

    def predict(self, obs, steps):
        pred = []
        n = len(obs)
        if len(obs) > 0:
            s = obs[-1]
        else:
            s = np.argmax(np.random.multinomial(1, self.startprob.tolist(), size = 1))
        for i in range(steps):
            s1 = np.random.multinomial(1, self.transmat[s,:].tolist(), size = 1)
            pred.append(np.argmax(s1))
            s = np.argmax(s1)
        return pred

# In[28]:

def hmm_predict_further_states(ghmm, obs, steps):
    y = ghmm.predict(obs)
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    return mm.predict([y[-1]], steps)

def hmm_predict_future_features(ghmm, obs, steps):
    y = ghmm.predict(obs)
    pred = []
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    sts = mm.predict([], steps)
    for s in sts:
        mean = ghmm.means_[y[-1]]
        cov = ghmm.covars_[y[-1],:]
        x = np.random.multivariate_normal(mean,cov,1)
        pred.append(x[0].tolist())
    return pred

# X: sequence of observations
# y: sequence of latent states
def estimate_parameters(X, y):
    mm = markovmodel()
    mm.fit(y)
    data = dict()
    for i in range(len(y)):
        for s, x in zip(y[i], X[i]):
            if data.has_key(s):
                data[s].append(x)
            else:
                data[s] = [x]
    ns = len(data.keys())
    # means = np.array([[np.mean(data[s])] for s,q in data.iteritems()])
    means = np.array([[np.mean(data[s])] for s in range(ns)])
    covars = np.tile(np.identity(1), (ns, 1, 1))
    # for s,q in data.iteritems():
    for s in range(ns):
        covars[s, 0] = np.std(data[s])
    return mm.startprob, mm.transmat, means, covars


def main():
    filepath= os.path.dirname(__file__) +'/'
    print filepath
    label = {0:'Boston',1:'Washington D.C.',2:'Philadelphia',3:'New York City',4:'Seattle'}
    rev_label = { v:k for k,v in label.iteritems()}
    y=[]
    X=[]
    with open(filepath+'HW9_Q4_training.txt') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    for line in content:
        line = line.replace('[','')
        line = line.replace(']','')
        line = line.replace('\'','')
        temp= line.split(',')
        temp = [i.strip() for i in temp]
        temp = [rev_label.get(item,item) for item in temp]
        #print len(temp)
        y.append(temp[::2])
        #print [float(m) for m in temp[1::2]]
        #np.append(X,[float(m) for m in temp[1::2]])
        q=[]
        for T in temp[1::2]:
            t = [float(T)]
            q.append(t)

        # q=([float(t)] for t in temp[1::2])
        # X.append([float(m) for m in temp[1::2]])
        X.append(q)

    # print X

    # print y
    # print X
    print np.shape(X)
    print np.shape(y)
    print len(label)

    startprob, transmat, means, covars = estimate_parameters(X, y)
    model = hmm.GaussianHMM(5, "full")
    model.startprob_ = startprob
    model.transmat_ = transmat
    model.means_  = means
    model.covars_ = covars
    print 'Model: \n',model
    print 'Predicted: '
    for x in X:
        y = model.predict(x)
        print [label[s] for s in y]


    # Task 2: Suppose we have testing seqeunces of spendings, we now predict the latent cities of these sequences
    print 'Testing Started: '
    with open('HW9_Q4_testing.txt') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    with open('HW9_Q4_predictions.txt','w') as file:
        for line in content:
            line = line.replace('[','')
            line = line.replace(']','')
            line = line.replace('\"','')
            temp= line.split(',')
            temp = [float(i) for i in temp]
            x=[]
            for T in temp:
                t = [float(T)]
                x.append(t)
            print x
            y = model.predict(x)
            predicted_labels = [label[s] for s in y]
            print predicted_labels
            file.write(str(predicted_labels)+'\n')

if __name__ == '__main__':
    main()
