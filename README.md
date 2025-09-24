# nba-analytics
Project data science : analysis and prediction NBA

# 🏀 NBA Analytics – Kevin Durant Career Analysis

## 🎯 Objectif du projet

Ce projet vise à analyser la carrière de **Kevin Durant** à travers ses statistiques NBA, afin de :

* Étudier l’évolution de ses performances au fil des saisons.
* Comparer ses performances en **saison régulière** et en **playoffs**.
* Visualiser son style de jeu (shot charts, efficacité par zone de tir).
* Mesurer son impact dans différentes équipes (OKC, Warriors, Nets, Suns).
* Construire des modèles de prédiction (points par match, efficacité, etc.).

---

## 📂 Structure du projet

```
nba-analytics/
├── data/                 # Données locales
│   ├── raw/              # Données brutes depuis nba_api
│   └── processed/        # Données nettoyées pour analyse
├── notebooks/            # Notebooks Jupyter
│   ├── 01_data_collection.ipynb   # Collecte des données de KD
│   ├── 02_eda.ipynb               # Analyse exploratoire & visualisations
│   └── 03_modeling.ipynb          # Modélisation & prédictions
├── src/                  # Scripts Python
│   ├── data/             # Scripts de collecte & préparation des données
│   ├── models/           # Scripts d’entraînement & évaluation de modèles
│   └── visualization/    # Fonctions de visualisation (graphiques, shot charts)
├── app/                  # Dashboard interactif
│   ├── app.py            # Application Streamlit
│   └── utils.py          # Fonctions utilitaires
├── models/               # Modèles ML sauvegardés
├── README.md             # Documentation du projet
├── requirements.txt      # Dépendances Python
└── .gitignore            # Fichiers/dossiers à ignorer
```

---

## 🛠️ Étapes du projet

### 1. Collecte des données

* Utilisation de `nba_api` pour récupérer :

  * Stats de Kevin Durant par saison (points, rebonds, passes, % au tir).
  * Stats avancées (TS%, eFG%, PER, usage rate).
  * Différences entre saison régulière et playoffs.
  * Shot charts (efficacité par zone de tir).

### 2. Exploration & Visualisation (EDA)

* Graphiques d’évolution (points, %3pts, TS%) au fil des saisons.
* Comparaison avant/après blessure (rupture tendon d’Achille en 2019).
* Comparaison par équipe (OKC vs GSW vs Nets vs Suns).
* Shot charts interactifs.

### 3. Analyses approfondies

* **Clutch stats** : performances dans les moments décisifs.
* **Impact collectif** : Net rating de l’équipe avec vs sans KD.
* **Comparaison avec d’autres stars** (LeBron, Curry, Giannis).

### 4. Machine Learning

* Régression pour prédire ses points/match en fonction du temps de jeu & usage rate.
* Classification des matchs : KD “scorer” vs KD “playmaker”.
* Clustering pour identifier les joueurs historiques qui lui ressemblent.

### 5. Mise en valeur

* Dashboard **Streamlit** permettant de :

  * Sélectionner une saison → afficher les stats et visualisations de KD.
  * Comparer KD à d’autres joueurs.
  * Explorer ses zones de tir préférées.
* Documentation claire avec conclusions & insights.

---

## 📊 Exemple de résultats attendus

* 📈 Évolution des points/match et TS% au fil de la carrière.
* 🏆 Comparaison des performances en playoffs vs saison régulière.
* 🎯 Zones de tir préférées de KD et efficacité.
* 🤖 Modèle prédictif simple pour estimer ses points/match.

---

## 🚀 Installation & Utilisation

1. Cloner le dépôt :

```bash
git clone https://github.com/ton-compte/nba-analytics.git
cd nba-analytics
```

2. Créer et activer un environnement virtuel (optionnel mais recommandé)

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Lancer les notebooks pour explorer les données :

```bash
jupyter notebook notebooks/
```

5. (Optionnel) Lancer le dashboard Streamlit :

```bash
streamlit run app/app.py
```

---

## 📦 Technologies utilisées

* **Python 3.9+**
* **nba\_api** (collecte des données NBA)
* **Pandas, NumPy** (traitement des données)
* **Matplotlib, Seaborn, Plotly** (visualisations)
* **Scikit-learn** (modélisation, ML)
* **Streamlit** (dashboard interactif)

---

## ✨ Auteur

Projet réalisé par *\[Ton Nom]* – Portfolio Data Science / NBA Analytics.
