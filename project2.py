import argparse
import all_functions as af
import json
import sys
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--N", type = int, required= True, help = "N nearest foods")
    args_parser.add_argument("--ingredients", required = True, help = "Please enter the ingredients", nargs = "*", action = "append")
    args = args_parser.parse_args()
    af.listing_files(path = 'yummly.json')
    dataset = af.tfidf_vectorizer(af.ing_file,args.ingredients)
    train_data,test_data = af.train_test_set(dataset)
    af.train_test_set(dataset)
    knn_final = af.train_model(train_data,af.cuisine,args.N)
    af.Cuisine_predictor(test_data,knn_final,args.N)
    af.ing_file.pop()
    p_cuisine,match_id = af.Cuisine_predictor(test_data,knn_final,args.N)
    final_op = json.dumps(p_cuisine, indent=4)
    sys.stdout.write(final_op)
    