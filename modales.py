import dash_bootstrap_components as dbc
from dash import html

# --- HEADER MODALS ---
# Réglages Profils
modal_profils = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Réglages Profils")),
    dbc.ModalBody(html.P("Choix de l'image de profil, bibliothèque de sons, etc.")),
], id="modal-profils", is_open=False)

# Volume
modal_volume = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Réglage du Volume")),
    dbc.ModalBody(html.Div("Jauge de volume à intégrer ici (ex: dcc.Slider)")),
], id="modal-volume", is_open=False)

# Interface Admin (Verrou)
modal_admin = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Interface d'Administration")),
    dbc.ModalBody(
        dbc.Tabs([
            dbc.Tab(html.P("Boutons de contrôle des servomoteurs (réduire/augmenter angle, remise à plat)."), label="Mode Forçage"),
            dbc.Tab(html.P("Formulaire de saisie des défis."), label="Défis"),
            dbc.Tab(html.P("Mise en veille, extinction de l'application."), label="Alimentation")
        ])
    ),
], id="modal-admin", is_open=False, size="lg")

# --- FOOTER MODALS ---
# Photobooth
modal_photobooth = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Photobooth")),
    dbc.ModalBody(html.P("Interface de capture photo.")),
], id="modal-photobooth", is_open=False, size="xl")

# Galerie
modal_galerie = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Galerie Photos")),
    dbc.ModalBody(html.P("Carrousel des photos stockées en mémoire.")),
], id="modal-galerie", is_open=False, size="lg")

# Ruche (Portail d'applications)
modal_ruche = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("La Ruche - Portail d'Applications")),
    dbc.ModalBody(html.Div(className="ruche-grid", children=[
        html.P("Alvéoles (boutons) pour lancer des jeux, apps d'exercices, etc.")
    ])),
], id="modal-ruche", is_open=False, fullscreen=True)

# --- CADEAUX MODALS ---
modal_retrait_cadeau = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Confirmation de retrait")),
    dbc.ModalBody(html.P("Voulez-vous vraiment retirer la récompense de ce niveau ?")),
], id="modal-retrait-cadeau", is_open=False)

modal_historique_cadeaux = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Historique des récompenses")),
    dbc.ModalBody(html.P("DataTable de l'historique à insérer ici.")),
], id="modal-historique-cadeaux", is_open=False, size="lg")