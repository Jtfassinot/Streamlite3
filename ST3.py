import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données des utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Initialisation de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",  # Nom du cookie
    "cookie_key",  # Clé du cookie
    30  # Durée de vie du cookie (en jours)
)

# Appel à la méthode login avec la localisation de la page spécifiée
authenticator.login("Connexion", location="main")

# Vérification de l'état de l'authentification
if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        # Si l'utilisateur est authentifié, afficher la page d'accueil
        st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

        # Menu de navigation
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos"],  # Options du menu
            icons=["house", "image"],  # Icônes pour chaque option
            default_index=0  # Page par défaut
        )

        if selection == "Accueil":
            st.write("Bienvenue sur la page d'accueil !")
        elif selection == "Photos":
            st.write("Bienvenue sur mon album photo")

        # Ajouter un bouton de déconnexion
        authenticator.logout("Déconnexion")

    elif st.session_state["authentication_status"] is False:
        # Si l'authentification a échoué
        st.error("Nom d'utilisateur ou mot de passe incorrect")

    elif st.session_state["authentication_status"] is None:
        # Si l'utilisateur n'a pas encore saisi ses informations
        st.warning("Veuillez remplir les champs nom d'utilisateur et mot de passe")

else:
    # Si le statut d'authentification n'est pas encore défini
    st.warning("Veuillez vous connecter")


