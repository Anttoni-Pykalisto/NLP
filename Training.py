from Finding import Finding
from os import listdir
from os.path import isfile, join

positiveFiles = ['TrainingText/positiveReviews/' + f for f in listdir('TrainingText/positiveReviews/') if isfile(join('TrainingText/positiveReviews/', f))]

text = ""

with open(positiveFiles[0], "r", encoding="utf-8") as f:
    line = f.readline()
    text += line

finding = Finding(0, text)

print("Finding of ID: " + str(finding.id))
print("Has text: " + str(finding.tokens))