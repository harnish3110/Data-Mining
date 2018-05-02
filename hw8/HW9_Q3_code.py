

import numpy as np
import copy
from ast import literal_eval

def get_all_sequences(m, n):
    i = 1
    S = []
    for j in range(n):
        S.append([j])
    while i < m:
        S1 = []
        for s in S:
            for j in range(n):
                s1 = copy.deepcopy(s)
                s1.append(j)
                S1.append(s1)
        S.extend(S1)
        i = i + 1
    S = [item for item in S if len(item) == m]
    return S


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
        n = len(obs)
        if len(obs) > 0:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = obs[-1]
                for i in comb:
                    prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            return max_seq
        else:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = -1
                for i in comb:
                    if prev == -1:
                        prob = prob * self.startprob[i]
                    else:
                        prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            return max_seq

def filetolist(rev_label,fileName):
    y_list=[]
    with open(fileName) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    for line in content:
        line = line.replace('[','')
        line = line.replace(']','')
        line = line.replace('\"','')
        temp= line.split(',')
        temp = [i.strip() for i in temp]
        temp = [rev_label.get(item,item) for item in temp]
        y_list.append(temp)
    return y_list

def main():

    label = {0:'Albany',1:'Boston',2:'Washington D.C.',3:'Philadelphia',4:'New York City', 5:'Seattle'}
    rev_label = { v:k for k,v in label.iteritems()}
    y=filetolist(rev_label,'HW9_Q3_training.txt')
    mm = markovmodel()
    mm.fit(y)
    y_test = filetolist(rev_label,'HW9_Q3_testing.txt')
    print 'Prediction: '
    with open('HW9_Q3_predictiion.txt','w') as file:
        for test in y_test:
            pred = mm.predict(test, 5)
            print pred
            file.write(str([label[s] for s in pred]))
            file.write('\n')

if __name__ == '__main__':
    main()





