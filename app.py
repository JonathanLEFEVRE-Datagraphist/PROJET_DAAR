import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State


# Importation de toutes nos modales depuis le fichier séparé
from modales import (modal_profils, modal_volume, modal_admin, 
                     modal_photobooth, modal_galerie, modal_ruche,
                     modal_retrait_cadeau, modal_historique_cadeaux)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --- LAYOUT ONGLET ENFANT (Modèle réutilisable) ---
def creer_onglet_enfant(nom_enfant):
    return html.Div(className="onglet-enfant-container", children=[
        dbc.Row([
            # Colonne Profil
            dbc.Col(html.Div([
                html.Img(src=f"/assets/photo_{nom_enfant}.png", className="photo-enfant"),
                html.H4(nom_enfant),
                html.P("Date de naissance: 01/01/2015"),
                html.P("Aime : La magie / Aime pas : Les épinards")
            ]), width=3),
            
            # Colonne Lumens & Eclairs
            dbc.Col(html.Div([
                html.H4("LUMENS & ÉCLAIRS"),
                html.P("Lumens en attente : 5"),
                html.P("Lumens activés : 12"),
                html.P("Éclairs : 2"),
                html.P("Bonus Patience : 3"),
                html.Div("Masque PNG du tube de remplissage ici", className="tube-visuel")
            ]), width=3),
            
            # Colonne Défis
            dbc.Col(html.Div([
                html.H4("DÉFIS"),
                html.Ul([
                    html.Li("Défi journalier : Ranger sa chambre (5 Lumens)"),
                    html.Li("Fil Rouge : Lire 5 livres (Remplissage total)")
                ])
            ]), width=3),
            
            # Colonne Cadeaux
            dbc.Col(html.Div([
                html.H4("CADEAUX"),
                dbc.Button("Retirer récompense", id=f"btn-retrait-{nom_enfant}", color="success", className="mb-2"),
                html.Br(),
                dbc.Button("Historique des récompenses", id=f"btn-historique-{nom_enfant}", color="info")
            ]), width=3)
        ])
    ])

# --- STRUCTURE GLOBALE ---
app.layout = html.Div(
    id="main-container",
    # Contrainte stricte de la résolution 1024x600
    style={"width": "1024px", "height": "600px", "margin": "0 auto", "position": "relative", "overflow": "hidden"},
    children=[

        # --- CALQUES DE FOND (Z-INDEX NÉGATIFS) ---
        
        # 1. Éclairage CSS Large & Cœur intense
        html.Div(className="galaxy-light-base"),
        html.Div(className="galaxy-heart-glow"),
        
        # 2. Le fond étoilé PNG (avec ses zones transparentes)
        html.Div(className="galaxy-stars-layer"),
        
        # 3. L'anneau de matière en rotation inclinée
        html.Div(className="galaxy-ring-perspective", children=[
            html.Div(className="galaxy-ring-inner")
        ]),


# --- INTERFACE APPLICATIVE (Z-INDEX POSITIF) ---
        
        html.Div(id="ui-layer", children=[
            # Header
        # Injection des modales invisibles dans le DOM
        modal_profils, modal_volume, modal_admin, modal_photobooth, 
        modal_galerie, modal_ruche, modal_retrait_cadeau, modal_historique_cadeaux,

        # HEADER
        dbc.Row(id="header", className="p-2 text-white align-items-center", children=[
            #dbc.Col(html.H5("Tour DAAR"), width=6),
            dbc.Col(html.Div([
                dbc.Button("Profils", id="btn-profils", size="sm", className="me-2"),
                dbc.Button("Volume", id="btn-volume", size="sm", className="me-2"),
                dbc.Button("Verrou", id="btn-admin", size="sm", color="danger"),
            ], className="d-flex justify-content-end"), width=6)
        ]),

        # BODY (Tabs)
        html.Div(id="body", className="p-2", style={"height": "400px","width": "80%","margin": "10px auto"}, children=[
            dbc.Tabs([
                dbc.Tab(label="Faustine", tab_id="tab-enfant-1", children=[creer_onglet_enfant("Faustine")]),
                dbc.Tab(label="KAMI", tab_id="tab-kami",label_style={"fontWeight": "bold","fontSize": "28px","margin": "0 20px"}, 
                        children=[
                        # --- INTÉGRATION DU MASQUE ET DES YEUX ICI ---
                        html.Div(id="esprit-sylvestre", className="kami-background", children=[
                            html.Div(className="yeux-gradient vert-repos"), # La lumière au fond (z-index 5)
                            html.Div(className="masque-png"),               # Le masque par-dessus (z-index 10)
                            html.Div(className="bouche-animation")          # La bouche (pour plus tard)
                        ]),
                ]),
                dbc.Tab(label="Irina", tab_id="tab-enfant-2", children=[creer_onglet_enfant("Irina")]),
            ], id="tabs-main", active_tab="tab-kami")
        ]),

        # FOOTER
        dbc.Row(id="footer", className="p-2 text-white position-absolute bottom-0 w-100", children=[
            dbc.Col(html.Div([
                dbc.Button("Micro", id="btn-micro", color="primary", className="me-2"),
                dbc.Button(id="btn-photobooth-img",className="btn-image-footer btn-photobooth-img me-2"),
                dbc.Button("Galerie", id="btn-galerie", color="primary", className="me-2"),
                dbc.Button("Ruche", id="btn-ruche", color="warning"),
            ], className="d-flex justify-content-center"))
        ])

       ])

    ]
)

# ==========================================
# CALLBACKS : GESTION DES FENÊTRES MODALES
# ==========================================

# 1. Callbacks pour le Header et le Footer (1 bouton = 1 modale)
@app.callback(Output("modal-profils", "is_open"), Input("btn-profils", "n_clicks"), State("modal-profils", "is_open"))
def toggle_profils(n, is_open):
    if n: return not is_open
    return is_open

@app.callback(Output("modal-volume", "is_open"), Input("btn-volume", "n_clicks"), State("modal-volume", "is_open"))
def toggle_volume(n, is_open):
    if n: return not is_open
    return is_open

@app.callback(Output("modal-admin", "is_open"), Input("btn-admin", "n_clicks"), State("modal-admin", "is_open"))
def toggle_admin(n, is_open):
    if n: return not is_open
    return is_open

@app.callback(Output("modal-photobooth", "is_open"), Input("btn-photobooth-img", "n_clicks"), State("modal-photobooth", "is_open"))
def toggle_photobooth(n, is_open):
    if n: return not is_open
    return is_open

@app.callback(Output("modal-galerie", "is_open"), Input("btn-galerie", "n_clicks"), State("modal-galerie", "is_open"))
def toggle_galerie(n, is_open):
    if n: return not is_open
    return is_open

@app.callback(Output("modal-ruche", "is_open"), Input("btn-ruche", "n_clicks"), State("modal-ruche", "is_open"))
def toggle_ruche(n, is_open):
    if n: return not is_open
    return is_open

# 2. Callbacks pour les zones Enfants (Plusieurs boutons pointent vers la même modale)
@app.callback(
    Output("modal-retrait-cadeau", "is_open"),
    [Input(f"btn-retrait-Faustine", "n_clicks"), Input("btn-retrait-Irina", "n_clicks")],
    State("modal-retrait-cadeau", "is_open")
)
def toggle_retrait(n_enfant1, n_enfant2, is_open):
    # Si l'un des deux boutons est cliqué, on inverse l'état de la modale
    if n_enfant1 or n_enfant2:
        return not is_open
    return is_open

@app.callback(
    Output("modal-historique-cadeaux", "is_open"),
    [Input("btn-historique-Faustine", "n_clicks"), Input("btn-historique-Irina", "n_clicks")],
    State("modal-historique-cadeaux", "is_open")
)
def toggle_historique(n_enfant1, n_enfant2, is_open):
    if n_enfant1 or n_enfant2:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8050)