import streamlit as st
import pandas as pd
import requests
import pickle

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity_func.pkl', 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7a37ce9f0e2cc18f536e7a3ac6d3768&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend_most_relevant_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    highly_recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        get_movie_id = movies.iloc[i[0]].movie_id
        
        # print(movies.iloc[i[0]].title)
        highly_recommended_movie.append(movies.iloc[i[0]].title)
        # fetching poster from movie_id
        recommended_movie_poster.append(fetch_poster(get_movie_id))

        # print(i[0])
    return highly_recommended_movie, recommended_movie_poster


st.title('Movie Recommender')
selected_movie = st.selectbox(
    'Please select any movie',
    (movies['title'].values))


if st.button('Recommend'):
    recommendation, posters = recommend_most_relevant_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
            st.text(recommendation[0])
            st.image(posters[0])
    with col2:
            st.text(recommendation[1])
            st.image(posters[1])

    with col3:
            st.text(recommendation[2])
            st.image(posters[2])
    with col4:
            st.text(recommendation[3])
            st.image(posters[3])
    with col5:
            st.text(recommendation[4])
            st.image(posters[4])
