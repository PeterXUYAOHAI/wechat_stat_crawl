import itchat
import jieba

itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

friends_count = len(friends)

provinces = []
signatures = []

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1

    NickName = i["NickName"]
    Province = i["Province"]
    Signature = i["Signature"]

    provinces.append(Province)
    signatures.append(Signature)

print "male: " + str(male/float(friends_count)*100)+"%"
print "female: " + str(female/float(friends_count)*100)+"%"

print ""
print ""

provinces_count = {}
unique_p = list(set(provinces))
for u in unique_p:
    provinces_count[u] = provinces.count(u)

sorted_province =  sorted(provinces_count.items(), key=lambda x:x[1],reverse=True)

for p in sorted_province[0:20]:
    print p[0] +" "+ str(p[1]/float(friends_count)*100)+"%"

signatures_str = ""
for s in signatures:
    signatures_str += s
    signatures_str += " "

signatures_str = signatures_str.replace("span", "").replace("class","").replace("emoji","")

wordlist = jieba.cut(signatures_str, cut_all=True)
word_text = " ".join(wordlist)
word_text = " ".join(word_text.split())
print word_text

word_count = {}
unique_w = list(set(word_text.split()))
for u in unique_w:
    word_count[u] = word_text.count(u)

sorted_word = sorted(word_count.items(), key=lambda x:x[1],reverse=True)
for s in sorted_word:
    if len(s[0]) == 1:
        continue
    print s[0]+" "+str(s[1])

