from pyhanlp import *

TermFrequency = JClass('com.hankcs.hanlp.corpus.occurrence.TermFrequency')
TermFrequencyCounter = JClass('com.hankcs.hanlp.mining.word.TermFrequencyCounter')
# 不显示词性
HanLP.Config.ShowTermNature = False

# 可传入自定义字典 [dir1, dir2]
segment = DoubleArrayTrieSegment()
# 激活数字和英文识别
segment.enablePartOfSpeechTagging(True)

#去掉停用词
def load_from_file(path):
    """
    从词典文件加载DoubleArrayTrie
    :param path: 词典路径
    :return: 双数组trie树
    """
    map = JClass('java.util.TreeMap')()  # 创建TreeMap实例
    with open(path,encoding='utf-8') as src:
        for word in src:
            word = word.strip()  # 去掉Python读入的\n
            map[word] = word
    return JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(map)

trie = load_from_file('stopwords.txt') #停词表，自己往里面加！我还没加全！
## 去掉停用词
def remove_stopwords_termlist(termlist, trie):
    return [term.word for term in termlist if not trie.containsKey(term.word)]

if __name__ == '__main__':
    counter = TermFrequencyCounter()
    with open ("yspl123-207.txt",encoding='utf-8') as f: #这里是要分词的文件
        try:
            a=f.read()
        except UnicodeEncodeError as e:
            pass
    termlist = segment.seg(a)
    counter.add(a)
    for termFrequency in counter:  # 遍历每个词与词频
        print("%s=%d" % (termFrequency.getTerm(), termFrequency.getFrequency()))
    print(counter.top(50))  # 取 top N #这个是关键词（自带算法算的）

    print(termlist)#停词前的分词
    print(remove_stopwords_termlist(termlist, trie)) #这个是朴素的没处理过的只加了停词表的分词，用这个算TFIDF
