import re

def create_document_vectors(cables):
    terms_re = re.compile(r"\w+")

    documents = [[term for term in terms_re.findall(cable.content.lower())
                  if term.isalpha() and
                  len(term) > 1]
                for cable in cables]

    documents = [map(lambda term: (term, document.count(term)), sorted(set(document))) for document in documents]
    
    return documents
