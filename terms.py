from collections import defaultdict
from math import log

def calculate_term_frequencies(documents):
    df = defaultdict(int)

    for document in documents:
        for term, count in document:
            df[term] += 1
            
    return df

def calculate_idf(df, nd):
    idf = dict([(term, log(nd / float(count))) for term, count in df.items()])
    
    return idf
