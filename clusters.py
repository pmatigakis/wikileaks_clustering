from collections import defaultdict

from scipy.sparse import lil_matrix, csr_matrix
from sklearn.cluster import KMeans

def create_document_term_matrix(documents, idf):
    nd = len(documents)
    nt = len(idf)
    
    dtm = lil_matrix((nd, nt))
    
    terms_index = dict([(term, index) for index, term in enumerate(idf.keys())])
    
    for document_index, document in enumerate(documents):
        for term, count in document:
            term_index = terms_index[term]
            dtm[document_index, term_index] = count * idf[term]
    
    return csr_matrix(dtm)

def cluster_documents(n_clusters, doc_term_matrix):
    kmeans = KMeans(n_clusters=n_clusters)

    kmeans = kmeans.fit(doc_term_matrix)

    distances = kmeans.transform(doc_term_matrix)

    results = distances.argmin(axis=1)

    clusters = defaultdict(list)

    for document_index, cluster in enumerate(results):
        clusters[cluster].append((document_index, distances[document_index, cluster]))
        
    return clusters
