from argparse import ArgumentParser
from datetime import datetime

from sklearn.preprocessing import normalize

from database import create_session
from models import Cable
from documents import create_document_vectors
from terms import calculate_term_frequencies, calculate_idf
from clusters import create_document_term_matrix, cluster_documents
from reports import create_report
from settings import database_name, username, password

def parse_arguments():
    parser = ArgumentParser()

    parser.add_argument("origin", help="Cable origin")
    parser.add_argument("start_date", help="Start date")
    parser.add_argument("end_date", help="End date")
    parser.add_argument("n_clusters", type=int, help="Number of clusters")
    parser.add_argument("output", help="Output folder")

    return parser.parse_args()

def main():
    args = parse_arguments()

    origin = args.origin
    start_date = datetime.strptime(args.start_date, "%Y/%m/%d")
    end_date = datetime.strptime(args.end_date, "%Y/%m/%d")
    n_clusters = args.n_clusters
    output= args.output

    #get the cable data
    session = create_session(database_name, username, password)

    cables = session.query(Cable).filter(Cable.origin==origin,
                                         Cable.date>=start_date, 
                                         Cable.date<end_date).all()
    nd = len(cables)

    #create the document vectors
    document_vectors = create_document_vectors(cables)

    #calculate term document frequencies
    df = calculate_term_frequencies(document_vectors)

    #calculate inverted term document frequencies
    idf = calculate_idf(df, nd)

    #create document-term matrix
    document_term_matrix = create_document_term_matrix(document_vectors, idf)

    #calculate clusters
    document_term_matrix = normalize(document_term_matrix)
    clusters = cluster_documents(n_clusters, document_term_matrix)

    #create report
    create_report(output, cables, clusters)

if __name__ == "__main__":
    main()
