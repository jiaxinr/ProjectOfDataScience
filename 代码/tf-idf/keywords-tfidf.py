import datetime
import math
import os
import sys

import jieba
import re


def segment(sentence, cut_all=True):
    sentence = re.sub('[a-zA-Z0-9]', '', sentence.replace('\n', ''))  # 过滤
    sentence = sentence.replace('用户：', '')
    sentence = sentence.replace('点赞数：', '')
    return jieba.lcut(sentence, cut_all=cut_all)  # 分词


def getStopWords(path):  # 获取停用词表
    swlist = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            swlist.append(line)
    return swlist


def calTFIDF(inputdir):  # 根据语料库目录计算每一个词的词频和TF-IDF
    documents = MyDocuments(inputdir)
    stopwords = getStopWords(path='my_stopwords.txt')  # 获取停用词表
    # 排除中文标点符号
    ignored = stopwords + ['', ' ', '', '。', '：', '，', '）', '（', '！', '?', '”', '“', '!', '？', '[', ']', '][', '.', '～', '·', '\"', ',']
    id_freq = {}  # 统计一个词的频数
    txt_freq = {}  # 统计一个词是否出现在这个文档里
    isInFile = {}  # 用来标记这个词是否出现在文件中
    i = 0  # 总文档数
    for doc in documents:
        # 每次进入一个新文档，isInFile这个标记就要全部置为false
        for key in isInFile:
            if isInFile[key]:   #如果不是false的话就置为false
                isInFile[key] = False
        doc = (x for x in doc if x not in ignored)
        for x in doc:  # 统计每个词的词频
            if not (isInFile.get(x, False)): #如果这个词是在所有文档中第一次出现，把他加入进去并默认置为false；如果这个词在这个文档中是第一次出现，把他加进去并默认置为false
                isInFile[x] = True
                txt_freq[x] = txt_freq.get(x, 0) + 1  # 如果出现在某个文档中这个词在文档中的出现数目+1
            id_freq[x] = id_freq.get(x, 0) + 1
        if i % 1000 == 0:  # 每隔1000篇输出状态
            print('Documents processed: ', i, ', time: ',
                  datetime.datetime.now())
        i += 1

    # 计算逆文档频率并且存储
    outputfile = "IDF.txt"
    with open(outputfile, 'w', encoding='utf-8') as f:
        total = sum(id_freq.values())  # 所有词的总value数，也就是所有词的总词数
        for key, value in id_freq.items():
            # TF-IDF的log是以二为底
            tf = value / total  # tf是对每一个词词频的归一化
            idf = math.log(i / (txt_freq.get(key, 0) + 1), 2)  # 注意要在分母上加一个1以避免0的情况
            f.write(key + ' ' + str(value) + ' ' + str(tf) + ' ' + str(idf) + ' ' + str(tf * idf) + '\n')


def printTopK(tfidf, select_words, topK):
    for i in range(0, topK):
        word = select_words[i]
        freq = tfidf.freq[word]
        tf_freq = tfidf.tf_freq[word]
        idf_freq = tfidf.idf_freq[word]
        tfidf_freq = tfidf.tfidf_freq[word]
        print(word + " " + "Freq = " + str(freq) + "  " + "TF = " + str(tf_freq) + "  "
              + "IDF = " + str(idf_freq) + "  " + "TF-IDF = " + str(tfidf_freq))


class MyDocuments(object):  # 实现高效读取文本并且进行分词
    def __init__(self, dirname):
        self.dirname = dirname
        if not os.path.isdir(dirname):
            print(dirname, '- not a directory!')
            sys.exit()

    def __iter__(self):
        for dirfile in os.walk(self.dirname):
            for fname in dirfile[2]:
                try:
                    text = open(os.path.join(dirfile[0], fname),
                                'r', encoding='utf-8').read()
                    yield segment(text)
                except UnicodeDecodeError as e:
                    pass


class TFIDFLoader(object):
    def __init__(self, idf_path):
        self.idf_path = idf_path
        self.freq = {}  # 词频
        self.tf_freq = {}  # tf
        self.mean_tf = 0.0  # tf均值
        self.idf_freq = {}  # idf
        self.mean_idf = 0.0  # idf均值
        self.tfidf_freq = {}  # tfidf
        self.load_idf()

    def load_idf(self):  # 从文件中载入idf，对这个idf文件的每一行（词语和idf值的一一对应）输入到一个字典中
        # 这个字典就是self.idf_freq这个对象
        cnt = 0
        with open(self.idf_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    word, freq, tf, idf, tfidf = line.strip().split(' ')
                    cnt += 1
                except Exception as e:
                    pass
                self.freq[word] = int(freq)
                self.tf_freq[word] = float(tf)
                self.idf_freq[word] = float(idf)
                self.tfidf_freq[word] = float(tfidf)

        print('Vocabularies loaded: %d' % cnt)
        # self.mean_idf = sum(self.idf_freq.values()) / cnt


class TFIDF(object):
    def __init__(self, idf_path):
        # 分别获取Loader的每个属性
        self.idf_loader = TFIDFLoader(idf_path)
        self.freq = self.idf_loader.freq
        self.tf_freq = self.idf_loader.tf_freq
        self.idf_freq = self.idf_loader.idf_freq
        self.tfidf_freq = self.idf_loader.tfidf_freq
        # self.mean_idf = self.idf_loader.mean_idf

    def extract_keywordsInSentence(self, sentence, topK=30):
        # 分词
        seg_list = segment(sentence)

        freq = {}
        for w in seg_list:
            freq[w] = freq.get(w, 0.0) + 1.0  # 统计词频
        if '' in freq:
            del freq['']
        total = sum(freq.values())  # 总词数

        for k in freq:  # 计算 TF-IDF
            freq[k] *= self.idf_freq.get(k) / total

        tags = sorted(freq, key=freq.__getitem__, reverse=True)  # 排序，reverse=true标志着是降序排序

        if topK:  # 返回topK
            return tags[:topK]
        else:
            return tags

    def extract_keywordsInCorpus(self, topK=20):
        tags = sorted(self.tfidf_freq, key=self.tfidf_freq.__getitem__, reverse=True)

        return tags[:topK], topK


if __name__ == '__main__':
    inputdir = "D:\\NJU\大二上\数据科学基础\大作业\Coding\评论数据\微博评论分时段\微博评论分时段\评论至122"
    calTFIDF(inputdir)
    idffile = "IDF.txt"
    tfidf = TFIDF(idffile)
    select_words, topK = tfidf.extract_keywordsInCorpus()  # 获得的topK个关键词
    printTopK(tfidf, select_words, topK=10)
