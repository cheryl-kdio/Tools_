# Modèle de projet Python

Template réutilisable pour la recherche, les statistiques et la Data Science.

## Structure

```text
python-project-template/
├── data/
│   ├── raw/             # Données brutes, à ne pas modifier
│   ├── interim/         # Données intermédiaires
│   ├── processed/       # Données prêtes pour l'analyse
│   └── external/        # Données externes
├── code/
│   ├── src/
│   │   └── project_template/ # Package de fonctions réutilisables
│   │       ├── __init__.py
│   │       └── example.py
│   ├── scripts/         # Exécution non interactive et automatisation
│   └── notebooks/       # Exploration, analyses et interprétation
├── configs/             # Paramètres scientifiques et expérimentaux
├── outputs/
│   ├── figures/         # Graphiques
│   ├── tables/          # Tableaux
│   ├── models/          # Modèles sauvegardés
│   └── reports/         # Rapports générés
├── tests/               # Tests automatisés
├── docs/                # Documentation méthodologique et technique
├── pyproject.toml       # Métadonnées, dépendances et outils Python
├── .gitignore           # Exclusions Git
└── README.md            # Présentation et mode d'emploi
```

### Où placer mon code ?

- `code/src/project_template/` : fonctions et classes importables. Ajouter par exemple `preprocessing.py`, `statistics.py` ou `visualization.py` selon les besoins. Éviter de lancer une analyse lors d'un import.
- `code/notebooks/` : appliquer les méthodes à des données, expliquer les hypothèses, afficher et interpréter les résultats.
- `code/scripts/` : automatiser les traitements, simulations ou exports depuis le terminal. Ce dossier est facultatif si les notebooks suffisent.
- `configs/` : centraliser les paramètres, sans modifier les algorithmes. `config.yaml` est un exemple ; les valeurs ne constituent pas des recommandations statistiques universelles.
- `tests/` : vérifier les fonctions sur des cas connus et des cas limites.

Les dossiers vides contiennent un `.gitkeep`, simple convention permettant de les conserver dans Git. Les données et résultats sont ignorés par défaut pour éviter de publier des fichiers sensibles ou volumineux.

## Installation

Prérequis : Python 3.11 ou supérieur et Git pour le versionnage. Depuis la racine du projet :

```bash
python -m venv .venv
```

Activation sous Windows (PowerShell) :

```powershell
.\.venv\Scripts\Activate.ps1
```

Sous macOS / Linux :

```bash
source .venv/bin/activate
```

Installer le package local et ses dépendances :

```bash
python -m pip install -e ".[dev]"
```

L'installation éditable permet d'importer les fonctions depuis les notebooks sans modifier `sys.path`. Utiliser le même environnement Python pour le noyau Jupyter. Les dépendances proposées sont indicatives ; supprimer celles qui ne servent pas.

## Vérifier et utiliser le projet

Depuis la racine :

```bash
python -m pytest
python -m ruff check .
python code/scripts/run_example.py
python -m jupyter lab
```

Ouvrir `code/notebooks/01_example.ipynb`. Le script et le notebook utilisent la même fonction :

```python
from project_template.example import add
add(2, 3)
```

Résultat attendu : `5`. Remplacer cet exemple pédagogique par les méthodes du projet.

### Lire les paramètres

Depuis la racine du projet, par exemple dans un script :

```python
from pathlib import Path
import yaml

config = yaml.safe_load(Path("configs/config.yaml").read_text(encoding="utf-8"))
alpha = config["statistics"]["alpha"]
```

Dans un notebook dont le répertoire de travail est `code/notebooks/`, utiliser `../../configs/config.yaml`. Vérifier le répertoire de travail avec `Path.cwd()` si nécessaire.

## Publier sur GitHub comme template

1. Créer un dépôt GitHub vide (sans README, licence ou .gitignore initial).
2. Depuis la racine du dossier extrait, exécuter :

```bash
git init
git add .
git commit -m "Initial project template"
git branch -M main
git remote add origin https://github.com/VOTRE_COMPTE/VOTRE_DEPOT.git
git push -u origin main
```

Remplacer l'URL par celle de votre dépôt. Vérifier `git status` avant le commit.
3. Dans les paramètres du dépôt GitHub, activer **Template repository** (Settings > General).
4. Pour un nouveau projet, utiliser **Use this template** sur GitHub puis cloner le nouveau dépôt.

## Adapter à un nouveau projet

Renommer le dépôt et, si souhaité, le package `project_template` : modifier le dossier sous `code/src/`, le nom dans `pyproject.toml` et les imports dans les scripts, tests et notebooks. Réinstaller ensuite le package. Adapter les paramètres, dépendances et documentation. Choisir une licence si le code doit être redistribué ; aucune licence n'est imposée par ce modèle.

## Reproductibilité

Conserver les données brutes, documenter les sources, fixer les graines aléatoires lorsque pertinent, consigner les paramètres et versions du code, et verrouiller les dépendances pour les analyses finales. Le fichier `pyproject.toml` ne verrouille pas à lui seul les versions transitives. Ne jamais publier de secrets ou de données confidentielles. Redémarrer le noyau et exécuter toutes les cellules avant de considérer un notebook comme reproductible.
