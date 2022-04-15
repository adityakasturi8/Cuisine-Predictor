> # Cuisine Predictor
### Author : Aditya K Kasturi 

__About:__
- Assume you are a data scientist for a hotel chain in this exercise. This hotel chain's food is well-known for its diversity and flavor. According to your marketing department, modifying the menu can increase success by 15%. As the primary data scientist, you are tasked with increasing menu income. You must assist hotel personnel with meal planning and preparation in order to do this. The goal of this project is to help the Executive Chef better understand the large menu set by providing a cuisine predictor.

__Libraries and Packages Used:__
- sys
- codecs
- sklearn
- KNNClassifier
- argparse
- pytest

__system requirements:__
- An instance wiht min of 8gb memory is required.
### Assumptions 
- The Yummly.json shall be available to use.
_ Assuming that the ingredient spelling is accurate.

### Bugs
- For Example: if i put --N 5 , and add ingredients. If there are not many cuisine with the mentioned ingredients, the model might print the given --N value.
- If the ingredient is misspelled the neighbour score is zero.
 ### Description

__How to install and use this packages:__
0. Require prior installation of python, pipenv, and pip
2. gitclone my repository ```https://github.com/adityakasturi8/cs5293sp22-project2.git```
3. cd into the project directory ```cs5293sp22-project2```
4. install python package pipenv by typing ```pip install pipenv```
5. run unit test using ```pipenv run python -m pytest```
6. run the project2.py file using the below instructions

__Running the Program:__
- The program can be run by utilizing the commandline.
- To run the program, run the project2.py file 
- The project2.py can be run by using the following command: 
- You can change the -N and --ingredient value
  ```
  pipenv run python project2.py --N 5 --ingredient paprika
  ``` 
__Dataset:__
- For this project, the dataset has be acquired from dropbox 
- The dataset can be found on ```https://www.dropbox.com/s/f0tduqyvgfuin3l/yummly.json```

__Result:__
- When we give --N and --ingredient values, Example: --N 5 --ingredient chilli, it will give us the predicted cuisine and nearby cusine Id and their score. Sample Output can be found below. 
```

{
    "Predicted_cuisine": "mexican",
    "Score": 0.6,
    "Closest": [
        {
            "ID": "26698",
            "Score": "0.64"
        },
        {
            "ID": "3371",
            "Score": "0.60"
        },
        {
            "ID": "8133",
            "Score": "0.59"
        },
        {
            "ID": "17491",
            "Score": "0.58"
        },
        {
            "ID": "5006",
            "Score": "0.58"
        }
    ]
}

```
__Functions:__

- In the project2.py file, There are six functions:

0. __project2.py__ :  The project2.py file calls all the functions from all_functions.py and executes the flow of the project.
                  The project2.py has all different funtions imported from the all_funtions.py, it contains the following functions
                  ```

                 listing_files(path)

                 tfidf_vectorizer(transform_data,input_data)
                 
                 train_test_set(dataset)

                 train_model(train_data,cuisine,z )

                 KNN_distance(test_data,knn_final,z)

                 Cuisine_predictor(test_data,knn_final,z)

                  ```
1. __listing_files(path)__ : This function extrcts the data of id, ingredients, and cuisine in the form of a list 

2. __tfidf_vectorizer(transform_data,input_data)__: This function vertorizes the data and returns the converted fetures of that data.

3. __train_test_set(dataset)__: This function trains the training dataset

4. __train_model(train_data,cuisine,z )__:  The training data were generated based on the main data file and the data(--N) as well as ingredients would be provided y the user.

5. __KNN_distance(test_data,knn_final,z)__: K-NEarest Neighbor (KNN) model is utilized to extract the data and predict the future predictions.

6. __Cuisine_predictor(test_data,knn_final,z)__: We use the K-Nearest Neighbor Classifier model to predict the cuisine from the input ingredients and the closest as well as the nearest neighbors.


__Test_Cases__:
- Every test funtion is tested with a passing case
1. for ```test_files(path)``` one passing case is tested with checking if the input file is returning or not 
2. for ```test_tfidf_vectorizer()```  one passing case is tested if the data of ingredients entered by user is returning or not
3. for ```test_train_test_set()``` One passing case is tested by checking if the train and test dataset is satisfied
4. for ```test_all()``` One passing case is tested by checking all the test functions are accessible or not 
