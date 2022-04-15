import all_functions as af 
import pytest
import project2


def test_files(path = "./yummly.json"):
    data = af.listing_files(path)
    if len(data) == 0:
        return False
    else:
        assert True
        

def test_tfidf_vectorizer():
    dataset = af.tfidf_vectorizer(af.ing_file,'chilli')
    if  len(dataset) == 0:
        return False
    else:
        assert True

def test_train_test_set():
    train_data,test_data = af.train_test_set(af.ing_file)
    if len(train_data) == 0 or len(test_data) == 0:
        return False
    else:
        assert True
        

def test_all():
    test_files()
    test_tfidf_vectorizer()
    test_train_test_set()

if __name__ == "__main__":
    test_all()
