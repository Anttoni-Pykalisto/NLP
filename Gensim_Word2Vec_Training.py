from Finding import Finding
from gensim.models import Word2Vec
from os import listdir
from os.path import isfile, join

training_files = ['TrainingText/' + f for f in listdir('TrainingText/') if isfile(join('TrainingText/', f))]

all_finding = []
all_text = []
text = ''

index = 0
for f in training_files:
    with open(f, "r", encoding="utf-8") as f:
        line = f.readline()
        text += line
    finding = Finding(index, text)
    all_finding.append(finding)
    all_text.append(finding.sentences)
    index += 1

# build vocabulary and train model
model = Word2Vec(
    all_text,
    size=150,
    window=10,
    min_count=2,
    workers=10)

model.train(all_text, total_examples=len(all_text), epochs=10)

words = list(model.wv.vocab)

print(str(words))