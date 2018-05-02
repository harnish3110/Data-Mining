# coding: utf-8
import numpy as np
from hmmlearn import hmm
import types
import ast



class markovmodel:
    #transmat: None
    def __init__(self, transmat = None, startprob = None):
        self.transmat = transmat
        self.startprob = startprob
    # It assumes the state number starts from 0
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
    means = np.array([[np.mean(data[s])] for s in range(ns)])
    covars = np.tile(np.identity(1), (ns, 1, 1))
    for s in range(ns):
        covars[s, 0] = np.std(data[s])
    return mm.startprob, mm.transmat, means, covars


def convert_sequences_to_list(filename):
    list = []
    list2 = []
    for line in open(filename).readlines():

        list_new = []
        list_new2 = []
        line = ast.literal_eval(line)

        for idx, city in enumerate(line):
            if 'Boston' == city[0]:
                list_new.append(0)
                list_new2.append([city[1]])
            elif 'Washington D.C.' == city[0]:
                list_new.append(1)
                list_new2.append([city[1]])
            elif 'Philadelphia' == city[0]:
                list_new.append(2)
                list_new2.append([city[1]])
            elif 'New York City' == city[0]:
                list_new.append(3)
                list_new2.append([city[1]])
            elif 'Seattle' == city[0]:
                list_new.append(4)
                list_new2.append([city[1]])

        list.append(list_new)
        list2.append(list_new2)

    return list2, list


X, y = convert_sequences_to_list('HW9_Q4_training.txt')


label = {0: "Boston", 1: "Washington D.C.", 2: "Philadelphia", 3: "New York City", 4: "Seattle"}

print X
print y

# Predict the latent cities of training sequences

startprob, transmat, means, covars = estimate_parameters(X, y)
model = hmm.GaussianHMM(5, "full")
print model
model.startprob_ = startprob
model.transmat_ = transmat
model.means_  = means
model.covars_ = covars

f = open('HW9_Q4_predictions.txt','a+')
f1 = open('HW9_Q4_testing.txt','r')
for idx, seq in enumerate(f1.readlines()):
    seq = seq.replace("\n","").replace("[","").replace("]","").replace(" ","")
    x= seq.split(",")
    x = [[float(i)] for i in x]
    y = model.predict(x)
    predicted_labels = [label[s] for s in y]
    print predicted_labels
    f.write(str(predicted_labels) + '\n')
f.close()
f1.close()
