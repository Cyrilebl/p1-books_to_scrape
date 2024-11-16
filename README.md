# Analyse de marché

## Surveillance des prix du site **Books to Scrape**

### ✨ À propos

Ce projet propose un outil automatisé pour analyser les prix des livres disponibles sur le site **Books to Scrape**. Il collecte des données structurées et télécharge les images des livres correspondants à des fins d’analyse de marché.

---

### 📌 Étape 1 : Cloner le repository

Téléchargez le projet sur votre ordinateur.

- Dans le terminal exécutez :

```bash
git clone <_repository url_>
```

---

### 📌 Étape 2 : Initialiser un environnement virtuel

Un environnement virtuel permet d'isoler les dépendances du projet.
Utilisez le module Python venv pour créer et gérer cet environnement.

- Créer un environnement :

```bash
python3 -m venv env
```

- Activer l'environnement :

```bash
source env/bin/activate
```

- Désactiver l’environnement :

```bash
deactivate
```

---

### 📌 Étape 3 : Installer les packages nécessaires

Installez les dépendances listées dans le fichier `requirements.txt`.

- Dans le terminal, exécutez :

```bash
pip install -r requirements.txt
```

---

### 📌 Étape 4 : Exécuter le code

- Dans le terminal, exécutez :

```bash
python3 main.py
```

---

### 📁 Organisation des données extraites

Les données extraites sont enregistrées dans le dossier `data`, organisé de la manière suivante :

- Les données de chaque livre sont enregistrées par **catégorie**.
- Les images de chaque livre sont téléchargées dans un sous-dossier portant le nom de la **catégorie correspondante**.
