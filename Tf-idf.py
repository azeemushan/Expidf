

import sys
import os

class tfidf:
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}

    def addDocument(self, doc_name, list_of_words):
        # building a dictionary
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(w, 0.) + 1.0
            self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

        # normalizing the dictionary
        length = float(len(list_of_words))
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length

        # add the normalized document to the corpus
        self.documents.append([doc_name, doc_dict])

    def similarities(self, list_of_words):
        """Returns a list of all the [docname, similarity_score] pairs relative to a list of words."""

        # building the query dictionary
        query_dict = {}
        for w in list_of_words:
            query_dict[w] = query_dict.get(w, 0.0) + 1.0

        # normalizing the query
        length = float(len(list_of_words))
        for k in query_dict:
            query_dict[k] = query_dict[k] / length

        # computing the list of similarities
        sims = []
        for doc in self.documents:
            score = 0.0
            doc_dict = doc[1]
            for k in query_dict:
                if doc_dict.has_key(k):
                    score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
            sims.append([doc[0], score])

        return sims

Doc1="In this lecture we discuss search-based evolutionary approaches to software modularization The following items will be discussed in this lecture Hill-climbing modularization approaches Simulated annealing algorithms Genetic-based algorithms Learning automataThe hill-climbing algorithm starts with a random initial solution within the search space A new solution is produced by modifying the initial one If the new solution is better than the previous one with respect to a given optimization function , it is accepted and the process continues in order to obtain a better solution The algorithm continues until no better solution is obtained When applied to the modularization problem the modularization quality is used as the optimization function However a major drawback of the hill-climbing algorithm is that it can become trapped in a local optima Hence many improved versions of the hill-climbing algorithm have been introduced to overcome this problem"
Doc1.split()
Doc1=TfIdf()
Obj.addDocument("doc", Doc1)
Obj.printDocs()
Obj.printCorpusDict()
print("Now similarities: ") 
Obj.similarities(Doc1)

