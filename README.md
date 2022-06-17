
# Movie Recommedation System

In this project I have built a content based movie recommender system. The algorithm recommends products that are similar to the ones that a user has liked in the past. This similarity (generally cosine similarity) is computed from the data we have about the items as well as the user’s past preferences.


## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/62332164/174352179-e1ec9546-fb62-469c-9bcd-2a209e33b058.png)


## Demo

![preview](https://user-images.githubusercontent.com/62332164/174352149-b983f586-34e0-44ca-89be-46e93d4b2518.gif)


## Working
Content Based Filtering - They suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person liked a particular item, he or she will also like an item that is similar to it.
## Cosine Similarity
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.


![img2](https://user-images.githubusercontent.com/62332164/174352186-65509629-09ca-44aa-a182-a54a6cc59ccd.png)


## Dataset
The TMDB 5000 movies dataset to build the model

You can collect dataset from https://www.kaggle.com/tmdb/tmdb-movie-metadata