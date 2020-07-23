import wordcloud
import nltk as nl
# import imageio

# w = wordcloud.WordCloud()
# w.generate('we,earth,rip,tooth,you,unity,intial')
# w.to_file('output.jpg')


#导入外部数据文件,list转换为str
# mk = imageio.imread('car.jpg')
f= open('movies.csv',encoding = 'utf-8')
txt = f.read()
txtlist = nl.word_tokenize(txt)
txtlist = ''.join(txtlist)

# 生成词云
wc = wordcloud.WordCloud(
        max_words=100,
        width=2000,
	    height=1200,
        # background_color='white',
        # mask = mk,
        # scale= 10
)

wc.generate(txtlist)
wc.to_file('output.jpg')

