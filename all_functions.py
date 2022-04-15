import json
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics.pairwise import cosine_similarity

id = []
cuisine = []
dataset = []
train_data = []
test_data = []
ing_file = []
predicted_cuisine = ''

def listing_files(path):
    with codecs.open( path,encoding = 'utf-8') as fle:
        data = json.load(fle)
    dat = len(data)
    for i in range(0,dat):
        id.append(data[i]["id"])
    for i in range(0,dat):
        cuisine.append(data[i]["cuisine"])
    ingredients_data = [data[i]["ingredients"] for i in range(0,len(data))]
    for i in ingredients_data:
        s = ' '.join(i)
        for ele in range(len(i)):
            s = s + ' ' + i[ele]
        ing_file.append(s.encode('utf-8'))

    return (ing_file)
    
def tfidf_vectorizer(transform_data,input_data):
    transform_data.append(str(input_data))
    tfidf = TfidfVectorizer(min_df=1)
    transform_data_features = tfidf.fit_transform(transform_data)
    transform_data_features = transform_data_features.todense()
    global t_dat
    t_dat = transform_data_features
    
    return ((transform_data_features))

def train_test_set(dataset):
    train_data = dataset[:len(dataset)-1]
    test_data = dataset[len(dataset)-1]
    return (train_data,test_data)


def train_model(train_data,cuisine,z ):
    knn = KNeighborsClassifier(n_neighbors=z)
    knn_final = knn.fit(train_data,cuisine)
    return knn_final

def Cuisine_predictor(test_data,knn_final,z):
    predicted_cuisine = knn_final.predict(test_data)
    
    p_cuisine = {'Predicted_cuisine': predicted_cuisine[0], 'Score': knn_final.predict_proba(test_data).max(), 'Closest' : []}
    score,match_id = knn_final.kneighbors(test_data)
    for i in range(len(match_id[0])):
        X =cosine_similarity(t_dat[match_id[0][i]],t_dat[-1])
        p_cuisine['Closest'].append({'ID' : (str(id[match_id[0][i]])) , 'Score' : "{:.2f}".format(((X[0][0])))})
    
    return p_cuisine, match_id








