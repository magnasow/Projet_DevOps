import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
import plotly.express as px
import matplotlib.pyplot as plt
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_option_menu import option_menu
from scraper import scrape_data
from scraper1 import scrape1_data
from scraper2 import scrape2_data
from scraper3 import scrape3_data  # Vérifiez le chemin d'accès correct
from PIL import Image
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie


equipe_lottie = (
    "https://lottie.host/9cd5bf39-5edd-4df5-be53-15b120c737ef/IZD0sRPpiY.json")

try:
    logo = Image.open("images/logo.png")
    board = Image.open("images/board.webp")

    dakarvente = Image.open("images/dakarvente.PNG")
    base64 = Image.open("images/base64.PNG")
    matplob = Image.open("images/matplob.png")
    pandas = Image.open("images/pandas.PNG")
    python = Image.open("images/python.PNG")
    streamlit = Image.open("images/streamlit.png")
    tableau = Image.open("images/tableau.png")
    equipe_ = Image.open("images/equipe.gif")
except FileNotFoundError as e:
    st.error(f"Erreur : {e}. Assurez-vous que les fichiers d'images sont présents dans le répertoire 'images'.")


st.set_page_config(page_icon="🧊", layout="wide")
# Style
st.markdown(
    """
    <style>
    .block-container {
            max-width:100%;   
            margin: 0 auto;                                
    } 
    
    .e1nzilvr4 hr{
        padding-top:0px;
        margin-top: 0px;
        margin-bottom: 0px;
        border:1px solid #46626e;
    }
    
    .st-emotion-cache-1nm0mzy e1nzilvr4 hr{
        margin-top: 0;
        margin-bottom: 0;
    }
    div.st-emotion-cache-1kyxreq e115fcil2{
        width:150px;
        border:solid 1px red;
        
    }
    div.st-emotion-cache-asc41u {
       margin: 0px 0px 0px 0px;
        padding: 0px 0px 0px 0px;
    }
        
    div.st-emotion-cache-1nm0mzy h1{
        font-size:10px;
        padding: 0px 0px 0px 0px;
    }
    div.st-emotion-cache-1nm0mzy p{
        margin-top:5%; 
    }
    div.st-emotion-cache-1v0mbdj img{
        border-radius: 10px 100px / 120px;
        margin-bottom:0px;
        padding-bottom:0px;
    }
          
    .css-1l02zno {
        text-align: center !important;
    }
    h1 {
    background-color: purple; /* Le fond de la page sera noir */
    color: white; /* Le texte de la page sera blanc */
    text-align: center;
    }
    .home-text {
        color: black !important;
        font-size: 20px !important;
    }
    .blue-text {
        color: blue !important;
    }
    .bold {
        font-weight: bold;
    }
    .dot {
        color: black;
        font-size: 24px;
        margin-right: 5px;
    }
    
    
      
    div.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am{
        width:200px;     
        font-color:white;
    }
    div.st-emotion-cache-116nhdx.e116k4er3
    {
        width:100px;
        font-color:white;
    }
    div.st-emotion-cache-116nhdx.e116k4er3
    {
        background-color:red;
        font-color:white;
        font-weight:bold;
    }
    
    div.st-ak.st-as.st-ar.st-am.st-cq.st-cr.st-cs.st-ct.st-az.st-b0.st-b1.st-b2.st-cu.st-b4.st-b5.st-an.st-ao.st-cv.st-cw.st-ae.st-af.st-ag.st-cx.st-ai.st-aj.st-b7.st-b8.st-b9.st-ba.st-bb.st-cy.st-cz{
        background-color:red;
        font-color:white;
        font-weight:bold;
    }
    
    div.st-as.st-am.st-d0.st-b4.st-b5.st-ae.st-af.st-ag.st-cx.st-ai.st-aj.st-b6.st-bb.st-cv.st-cw{
        background-color:red;
         font-color:white;
        font-weight:bold;
    }
    
    div.st-emotion-cache-76z9jo.e116k4er2 button{
        background-color:red;
        font-color:white;
        font-weight:bold;
    }
    
    div.step-up.st-emotion-cache-1hsryq0.e116k4er1{
        font-color:white;
        font-weight:bold;
    }
    
    div.row-widget.stButton button{
        border:0px;
    }
    
    div.ios-iframe-bug-wrap{
        background-color:white;
    }
    div.st-emotion-cache-1nm0mzy.e1nzilvr4 ul{
        list-style-type: none;
        font-family:sans-serif;
        
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
# Interface utilisateur
left_column, right_column = st.columns([0.3, 2])
with st.container():
    with left_column:
        logo = logo.resize((115, 115))
        st.image(logo)
    with right_column:
        st.write(
            """
           L'Application(**DATA SCRAPER APP**) Data Miner peut extraire des données d'une seule page ou parcourir un site et extraire des données de plusieurs pages telles que les détails d'annonces de Dakar.com, les marques, les prix, adresses, lien des images d'annonces,
            en toute souplesse.
            """
        )
st.write("---")
# Fonction pour charger et afficher les données


def load_and_display_data(df, title):
    st.write(f"### {title}")  # Titre des données
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)  # Pagination
    gb.configure_side_bar()  # Barre latérale
    gridOptions = gb.build()
    AgGrid(df, gridOptions=gridOptions, theme='streamlit')

    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Télécharger les données",
        data=csv,
        file_name=f"{title}.csv",
        mime='text/csv'
    )

# Fonction pour afficher la page d'accueil

# Fonction pour afficher les graphiques

def plot_graphs(df, title, y_label, colors):
    #colors = ['green', 'blue', 'orange', 'purple']
    fig, ax = plt.subplots()
    df.plot(kind='bar', color=colors, ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Marque")
    ax.set_ylabel(y_label)
    ax.set_xticklabels(df['marque'], rotation=45)
    st.pyplot(fig)


def download_data_page():
    st.subheader(" Téléchargement des données extraites")
    st.write(
        ":large_red_square:  Téléchargez les données collectées à partir des sites web grâce au Web Scraper.")
    st.write("---")
    st.write("")

    # Boutons pour afficher les données
    if st.button('🚗 Rubrique Vehicule data'):
        load_and_display_data(pd.read_csv('data/URL_1.csv'),
                              'Données  Rubrique Vehicule')

    if st.button('🏍 Motocycle data'):
        load_and_display_data(pd.read_csv(
            'data/URL_2.csv'), 'Données Rubrique Motocycle')

    if st.button('🚕 Location Vehicule data'):
        load_and_display_data(pd.read_csv('data/URL_3.csv'),
                              'Données Rubrique Location Vehicule')

    if st.button('📱 Telephone data'):
        load_and_display_data(pd.read_csv(
            'data/URL_4.csv'), 'Données Rubrique Telephone')

    st.write("---")
# Fonction pour afficher la page de scraping


def scrape_data_page():
    st.subheader(
        "Web Scraping avec Python BeautifulSoup (SelectByClass, SelectByAttribute)", anchor=None)
    st.write(
        "Nous obtenons des données à partir de pages web en utilisant Beautiful Soup.")

    # Ajouter un sélecteur pour choisir le type de données à scraper
    options = ["TELEPHONES", "RUBRIQUE VEHICULE",
               "MOTOCYCLES", "LOCATION DE VOITURES"]
    choice = st.selectbox(
        ":large_red_square: Choisissez le type de données à scraper", options)

    num_pages = st.number_input(
        ":large_blue_square:  Selectionnez le nombre de pages à scraper", min_value=1, value=1)

    # Bouton de scraping
    if st.button("SCRAPER"):
        if choice == "TELEPHONES":
            url_phones = "https://dakarvente.com/annonces-categorie-telephones-32.html?page={}"
            df = scrape_data(url_phones, num_pages)
            if not df.empty:
                st.session_state['scraped_data'] = df
                st.session_state['title'] = "DONNÉES: TÉLÉPHONES PORTABLES À VENDRE"
            else:
                st.write(
                    "No data extracted from the webpage. Please check the URL.")

        elif choice == "RUBRIQUE VEHICULE":
            url_vehicles = "https://dakarvente.com/annonces-rubrique-vehicules-2.html?page={}"
            df = scrape1_data(url_vehicles, num_pages)
            if not df.empty:
                st.session_state['scraped_data'] = df
                st.session_state['title'] = "DONNÉES: VÉHICULES"
            else:
                st.write(
                    "No data extracted from the webpage. Please check the URL.")

        elif choice == "MOTOCYCLES":
            url_motos = "https://dakarvente.com/annonces-categorie-motos-3.html?page={}"
            df = scrape2_data(url_motos, num_pages)
            if not df.empty:
                st.session_state['scraped_data'] = df
                st.session_state['title'] = "DONNÉES: MOTOS À VENDRE"
            else:
                st.write(
                    "No data extracted from the webpage. Please check the URL.")

        elif choice == "LOCATION DE VOITURES":
            url_loc_vehicule = "https://dakarvente.com/annonces-categorie-location-de-vehicules-8.html?page={}"
            df = scrape3_data(url_loc_vehicule, num_pages)
            if not df.empty:
                st.session_state['scraped_data'] = df
                st.session_state['title'] = "DONNÉES: LOCATION DE VOITURES"
            else:
                st.write(
                    "No data extracted from the webpage. Please check the URL.")
    st.write("---")
    # Affichage des données si elles sont présentes dans l'état de session
    if 'scraped_data' in st.session_state and 'title' in st.session_state:
        load_and_display_data(
            st.session_state['scraped_data'], st.session_state['title'])
        # Bouton pour réinitialiser l'état et fermer la fenêtre de résultats
        if st.button("FERMER LES DONNÉES"):
            del st.session_state['scraped_data']
            del st.session_state['title']

# Fonction pour afficher la page d'accueil


def home():
    with st.container():
        st.image(board)
    st.write("---")
    with st.container():
        cl1, cl2, cl3, cl4, cl5, cl6 = st.columns(6)
        with cl1:
            st.image(dakarvente.resize((100, 24)))
        with cl2:
            st.image(base64.resize((100, 24)))
        with cl3:
            st.image(matplob.resize((100, 24)))
        with cl4:
            st.image(pandas.resize((100, 24)))
        with cl5:
            st.image(python.resize((100, 24)))
        with cl6:
            st.image(streamlit.resize((100, 24)))


# Fonction pour afficher la page d'évaluation avec le formulaire KoBoToolbox


def evaluation():
    st.subheader("Formulaire d'evaluation de l'application")
    c1, c2, c3 = st.columns([0.3, 3, 0.3])
    with c1:
        st.empty()
    with c2:
        components.iframe("https://ee.kobotoolbox.org/i/aSu6LaRZ",
                          width=800, height=1200)
    with c3:
        st.empty()
    st.write("---")


def dashbord():
    st.write("---")
    c1, c2, c3 = st.columns([0.3, 3, 0.3])
    with c1:
        st.empty()
    with c2:
        st.image(tableau)
    with c3:
        st.empty()

    # Chargez et affichez les données nettoyées
    data_files = [
        ('datacleaned/cleaned_URL_1.csv', 'Cinq marques de véhicules les plus vendues', 'Prix des véhicules'),
        ('datacleaned/cleaned_URL_2.csv', 'Cinq marques de motos les plus vendues', 'Prix des motos'),
        ('datacleaned/cleaned_URL_3.csv', 'Cinq marques de location de véhicules les plus populaires', 'Prix des locations de véhicules'),
        ('datacleaned/cleaned_URL_4.csv', 'Cinq marques de téléphones les plus vendues', 'Prix des téléphones')
    ]
    colors = ['green', 'blue', 'orange', 'purple']
    # Affichage des graphiques en deux lignes de deux colonnes
    for i, (file, title, y_label) in enumerate(data_files):
        
        df = pd.read_csv(file)
        if i % 2 == 0:
            cols = st.columns(2)
        with cols[i % 2]:
            plot_graphs(df, title, y_label, colors[i])
        if i % 2 == 1:
            st.write("---")

def plot_top_brands(df, title):
    st.write(f"## Top 5 Brands in {title}")

    # Calculer les cinq marques les plus vendues
    top_brands = df.apply(df['BRAND'].nlargest(5))

    # Créer un sous-DataFrame avec les données des cinq marques les plus vendues
    top_brands_data = df[df['BRAND'].isin(top_brands.index)]

    # Tracer un diagramme à barres pour chaque marque avec la variation de prix
    fig = px.bar(top_brands_data, x='BRAND', y='PRICE', color='BRAND', barmode='group', title='Variation des prix par marque')
    st.plotly_chart(fig)


def equipe():
    st.subheader(" Notre Équipe")
    c1, c2, c3 = st.columns([0.3, 3, 0.3])
    with c1:
        st_lottie(equipe_lottie, key="equipe_img")
    with c2:
        st.markdown(
            """            
            - :large_purple_square: MARIETA SOW
            - :large_green_square: NGARTOUBAM NGARNGOMDJE
            - :large_yellow_square: ALIOUNE BADARA AMAR
            - :large_blue_square: NAMBAYE JOSUE FRANKYS
            """
        )
    with c3:
        st.empty()
    st.write("---")


selected = option_menu(
    menu_title=None,
    options=["ACCUEIL", "BEAUTIFULSOUP", "WEB SCRAPER",
             "DASHBORD", "EVALUATION", "EQUIPE"],
    icons=["house", "book", "code", "bar-chart", "star", "microsoft-teams"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "font-size": "96%",
            "font-weight": "bold",
            "font-family": "sans-serif",
            "display": "flex",
            "justify-content": "space-between",
            "flex-wrap": "nowrap",
            "border": "2px",
            "border-color": "green",
        },
        "icon": {"color": "green", "font-size": "15px"},
    }
)

# Afficher le contenu en fonction de l'option sélectionnée
if selected == 'WEB SCRAPER':
    download_data_page()
elif selected == 'BEAUTIFULSOUP':
    scrape_data_page()
elif selected == 'ACCUEIL':
    home()
elif selected == 'DASHBORD':
    dashbord()
elif selected == 'EVALUATION':
    evaluation()
elif selected == 'EQUIPE':
    equipe()
