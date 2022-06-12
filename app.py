import streamlit as st
import pandas as pd
import requests
import pickle
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red;'>Movie Recommender System</h1>", unsafe_allow_html=True)

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity_func.pkl', 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7a37ce9f0e2cc18f536e7a3ac6d3768&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_overview(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7a37ce9f0e2cc18f536e7a3ac6d3768&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    over_view = data['overview']
    return over_view

def fetch_date(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7a37ce9f0e2cc18f536e7a3ac6d3768&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    release_date = data['release_date']
    return release_date

def fetch_rating(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7a37ce9f0e2cc18f536e7a3ac6d3768&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    rating = data['vote_average']
    return rating

def recommend_most_relevant_movie(movie):
    highly_recommended_movie = []
    recommended_movie_poster = []
    recommended_movie_overview = []
    recommended_movie_release=[]
    recommended_movie_runtime = []
    recommended_movie_rating= []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    for i in movie_list[1:6]:
        get_movie_id = movies.iloc[i[0]].movie_id
        # print(movies.iloc[i[0]].title)
        highly_recommended_movie.append(movies.iloc[i[0]].title)
        # fetching poster from movie_id
        recommended_movie_poster.append(fetch_poster(get_movie_id))
        recommended_movie_overview.append(fetch_overview(get_movie_id))
        recommended_movie_rating.append(f'Rating: {fetch_rating(get_movie_id)}')
        recommended_movie_release.append(f'Released On: {(fetch_date(get_movie_id))}')

        # print(i[0])
    return highly_recommended_movie, recommended_movie_poster,recommended_movie_overview,recommended_movie_rating,recommended_movie_release


st.title('What to Watch???🍿🍿🍿🍿')
selected_movie =  st.selectbox(
    'Please select any movie',
    (movies['title'].values))


if st.button('Recommend'):
    recommendation, posters,recommended_movie_overview,recommended_movie_rating,recommended_movie_release = recommend_most_relevant_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
            st.subheader(recommendation[0])
            st.image(posters[0])
            st.caption(recommended_movie_overview[0])
            st.text(recommended_movie_rating[0])
            st.text(recommended_movie_release[0])

    with col2:
            st.subheader(recommendation[1])
            st.image(posters[1])
            st.caption(recommended_movie_overview[1])
            st.text(recommended_movie_rating[1])
            st.text(recommended_movie_release[1])

    with col3:
            st.subheader(recommendation[2])
            st.image(posters[2])            
            st.caption(recommended_movie_overview[2])
            st.text(recommended_movie_rating[2])
            st.text(recommended_movie_release[2])
    with col4:
            st.subheader(recommendation[3])
            st.image(posters[3])            
            st.caption(recommended_movie_overview[3])
            st.text(recommended_movie_rating[3])
            st.text(recommended_movie_release[3])
    with col5:
            st.subheader(recommendation[4])
            st.image(posters[4])
            st.caption(recommended_movie_overview[4])
            st.text(recommended_movie_rating[4])
            st.text(recommended_movie_release[4])
