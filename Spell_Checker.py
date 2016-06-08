import re, collections,string

def words(text):
    return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
        #print(f)
    return model
file=open('dict.txt')
NWORDS = train(words(file.read()))

alphabet = string.ascii_lowercase

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b for a, b in splits for c in alphabet]
#   print(splits)
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(print(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS))

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    #print(known_edits2(word))
    return set(known([word]) or known(edits1(word)) or known_edits2(word) or [word])
    #return  max(candidates, key=NWORDS.get)

print("Enter Word:  ")
print(correct("parsanlit"))