import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
      st.title("Bienvenu sur le contenu réservé aux pilotes émérites")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options

 # Ajout d'une barre latérale
with st.sidebar:
    st.button("Déconnexion")

    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":

    st.write("Bienvenue **root**")
    st.write("Bienvenue sur la page d'accueil !")
    st.header("La futur !!! version améliorer, chassis plus perfomant, angle de chasse modifié pour etre plus sur l'avant")
    st.header("Elle est fin prete pour la piste")
    st.image("/Users/julien-thomasfassinot/Documents/WCS/VSD/Streamlit partie 2/MT09.jpeg", caption="Voici la bete", use_container_width=True)


elif selection == "Photos":

    st.write("Bienvenue sur la page des 'tous motards' ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("numero uno")
        st.image("https://cdn2.yamaha-motor.eu/prod/product-assets/2024/MT09DX/2024-Yamaha-MT09DX-EU-Icon_Performance-360-Degrees-001-03.jpg", caption="Voici la bete", use_container_width=True)

    with col2:
        st.header("le tracteur")
        st.image("https://www.ktmmalaysia.com/wp-content/uploads/2021/03/PHO_BIKE_90_RE_1290-sdr-21-or-90re_SALL_AEPI_V1.png", caption="Voici la fusée", use_container_width=True)

    with col3:
        st.header("L'A2")
        st.image("https://storage.kawasaki.eu/public/kawasaki.eu/en-EU/model/16ER650F_44SBEIDRS2CG_C.png", caption="Voici celle qui prend le plus d'angle", use_container_width=True)

if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')



  




