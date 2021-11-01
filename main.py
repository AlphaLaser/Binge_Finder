from imdb import IMDb
import streamlit as st
from bokeh.models.widgets import Div
from PIL import Image


logo = Image.open(r'images/Binge_Finder.png')
st.image(logo)

st.markdown("<br>", unsafe_allow_html=True)

ia = IMDb()



search = st.text_input("Enter Movie name or prefix : ")


others = ia.search_movie(search)


# Sidebar Start

m = st.sidebar.markdown("""
<style>
div.stButton > button:first-child {
    width : 95% ;
    align: center;
    border-radius : 10px ;
    height: 100px ;

}
</style>
""", unsafe_allow_html=True)

m = st.markdown("""
<style>
    st.form.submit_button{

        background-color : blue ;

    }
}
</style>
""", unsafe_allow_html=True)
title = st.sidebar.header('Navigator 🧭')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
# st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('What it does and Usage'):
    js = "window.open('https://light-feeling-5c3.notion.site/Usage-Guide-919d7c6ab66d41c981319b9ab8a3a137')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if st.sidebar.button('Github'):
    js = "window.open('https://github.com/AlphaLaser/ParaTools')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
title = st.sidebar.header('Contact Us 📞')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
# st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('E-Mail'):
    js = "window.open('mailto:aditmagotra@gmail.com')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if st.sidebar.button('Whatsapp'):
    js = "window.open('https://api.whatsapp.com/send?phone=919958877036')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


# Sidebar End
st.header(f"Most popular recommendation : \n")
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
if len(others) != 0 :
    others.pop(0)


    movies = ia.search_movie(search)
    movie = movies[0]
    id = movie.movieID
    movie_id_recog = ia.get_movie(id, info=['main', 'plot'])



    # st.header(f"Most popular recommendation : \n")
    # st.markdown("<br>",unsafe_allow_html=True)
    # st.markdown("<br>",unsafe_allow_html=True)

    st.success(movie)

    my_expander = st.expander(label='See Details')
    with my_expander:

        st.markdown("<hr>", unsafe_allow_html=True)

        st.subheader('\nPlot : \n')
        st.markdown("<br>", unsafe_allow_html=True)
        try :


            plot = (movie_id_recog['plot'][0])
            st.write(plot)
        except :

            st.write("Sorry bro, those peeps didn't add a plot ¯\_(ツ)_/¯")

        st.markdown("<hr>", unsafe_allow_html=True)

        st.subheader('\nGenres : \n')
        st.markdown("<br>", unsafe_allow_html=True)

        try :
            

            genres = (movie_id_recog['genre'])

            for i in genres :
                st.text(f'• {i}')

        except:
            
            st.write("Aww man, they didn't add genres for this one")





st.markdown("<hr>",unsafe_allow_html=True)


st.header("\nSimilar movies : \n")
st.markdown("<br>",unsafe_allow_html=True)

movie_titles = []

for i in others :
    a = i['title']
    movie_titles.append(a)




    processed_others = []

    for i in movie_titles:
        if i not in processed_others:
            processed_others.append(i)


    if processed_others[-1] != movie :
        print(movie, processed_others[-1])
        st.info(processed_others[-1])

