from nltk.corpus import wordnet

def synonym(words):
   synonyms = []
   #word = 'search'
   for word in words:
      # print(word)
      for synonym in wordnet.synsets(word):
         for item in synonym.lemmas():
            if word != synonym.name() and len(synonym.lemma_names()) > 1:
               synonyms.append(item.name())
      else:
         synonyms.append(word)
   return(set(synonyms))

# put = ["update","change"]

# put_synonym_words=synonym(put)
# put_synonym_words.add("update")
# print(put_synonym_words)
# print((set(put_synonym_words)))
# for i in ((set(put_synonym_words))):
#    print(i)

# get = ["see","search","observe","get","identify","detect","view"]
# post = ["add","include","upload"]
# put = ["update","change"]
# delete = ["remove", "delete"]
# print(synonym(delete))
#print("upload" in synonym(post))
# import nltk
# from nltk.corpus import stopwords

# stops = set(stopwords.words('english'))
# print(stops)
# print("want" in stops)
