import nltk
from nltk.corpus import stopwords
import string
import pyterrier as pt
import pandas as pd
import json

if not pt.started():
      pt.init()

nltk.download('punkt')
nltk.download('wordnet')
dataframes1 = []
dataframes2 = []
dataframes3 = []

with open('./data/results_album1.jsonl', 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        df = pd.DataFrame([json_obj])
        dataframes1.append(df)


df1 = pd.concat(dataframes1, ignore_index=True)

with open('./data/results_album2.jsonl', 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        df = pd.DataFrame([json_obj])
        dataframes2.append(df)


df2 = pd.concat(dataframes2, ignore_index=True)


with open('./data/results_album3.jsonl', 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        df = pd.DataFrame([json_obj])
        dataframes3.append(df)


df3 = pd.concat(dataframes3, ignore_index=True)

df = pd.concat([df1, df2, df3], ignore_index=True)



album_name = df.album.values
artist_name = df.artist.values

description = df.description.values
print(df)

df['genres_concatenated'] = df['genre'].apply(lambda x: ', '.join(x))
generes_type = df.genres_concatenated.values
df['text'] = df['album'] + ' ' + df['artist'] + ' ' + df['genres_concatenated'] + ' ' + df['description']
df['text'] = df['text'].str.lower().str.replace(r'\s+', ' ', regex=True)

df['docno'] = "d" + df.index.astype(str)

df = df[['docno', 'text']]

df.to_csv('./docs1.csv', index=False)

indexer = pt.DFIndexer("./index_3docs", overwrite=True)
index_ref = indexer.index(df["text"], df["docno"])
index_ref.toString()

index = pt.IndexFactory.of(index_ref)

#lets see what type index is.
type(index)

print(index.getCollectionStatistics().toString())

for kv in index.getLexicon():
    print("%s  -> %s " % (kv.getKey(), " ".join(kv.getValue().toString().split())))

"""INVERTED INDEX"""

word_ = "javelin"
pointer = index.getLexicon()[word_]
for posting in index.getInvertedIndex().getPostings(pointer):
    print(posting.toString() + " doclen=%d" % posting.getDocumentLength())

br = pt.BatchRetrieve(index, wmodel="BM25")
# br.search("javelin")

# br.search("Tender")

# br.search("Golden Apples of the Sun")

bm25 = pt.BatchRetrieve(index, wmodel="BM25")

# bm25.search("Blonde Redhead")

def get_album(docid):
  id = int(docid[1:])
  return album_name[id].replace('Album', '')

def retriever_album(df):
  album = []
  for i in range(df.shape[0]):
    docid = df.loc[i, 'docno']
    album.append(get_album(docid))
  df['Album'] = album
  return df

def get_artist(docid):
    id = int(docid[1:])
    return artist_name[id].replace('Artist', '')

def get_genres(docid):
    id = int(docid[1:])
    return generes_type[id].replace('Genre', '')
  
def get_description(docid):
    id = int(docid[1:])
    return description[id].replace('Description', '')


def retriever_artist(df):
  artist = []
  for i in range(df.shape[0]):
    docid = df.loc[i, 'docno']
    artist.append(get_artist(docid))
  df['Artist'] = artist
  return df


def retrieve_query(query):
    # Assuming index, pt, get_artist, get_album, get_genres, and get_description are defined/imported
    bm25 = pt.BatchRetrieve(index, num_results=30, wmodel="BM25")
    queries = pd.DataFrame([["q1", query]], columns=["qid", "query"])
    results = bm25.transform(queries)

    artist = []
    album = []
    genres = []
    description = []
    link = []
    link_image = []
    for i in range(results.shape[0]):
        docid = results.loc[i, 'docno']
        artist.append(get_artist(docid))
        album.append(get_album(docid))
        genres.append(get_genres(docid))
        description.append(get_description(docid))
    results['Artist'] = artist
    results['Album'] = album
    results['Genres'] = genres
    results['Description'] = description
    df_result = pd.DataFrame()
    df_result = results[['Artist', 'Album', 'Genres', 'Description']]
    print(df_result)
    return df_result

    
retrive = retrieve_query("blonde redhead")

"""For album"""

bm25 = pt.BatchRetrieve(index, num_results =10, wmodel="BM25")
queries = pd.DataFrame([["q1", "tomb mold"], ["q2", "blonde redhead"]], columns=["qid", "query"])
results = bm25.transform(queries)
retriever_album(results)

"""For artist"""

bm25 = pt.BatchRetrieve(index, num_results =10, wmodel="BM25")
queries = pd.DataFrame([["q1", "golden apples of the sun"], ["q2", "afternoon x"]], columns=["qid", "query"])
results = bm25.transform(queries)
retriever_artist(results)

# pt.io.write_results(results, "res_bm25.txt", format='trec')

# Cluster

