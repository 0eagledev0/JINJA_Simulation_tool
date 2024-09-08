# JINJA_Simulation_tool

---

![](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white) ![](https://camo.githubusercontent.com/050fc4e602f25dd4fc337b873fbc62b7d393673a9f4b1e7529a9a61ea35485a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565) ![](https://img.shields.io/badge/Python-3.11-<>.svg) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)

---


## Description
Ce projet fournit une interface graphique (GUI) pour le rendu de modèles en utilisant Jinja2. L'application permet aux utilisateurs de sélectionner et de combiner des fichiers de variables (au format JSON, YAML ou Jinja) avec des modèles Jinja pour générer du contenu rendu. L'interface est construite en utilisant la bibliothèque Tkinter de Python.

## Fonctionnalités
- **Sélection de Fichiers :** Permet aux utilisateurs de sélectionner des fichiers de variables au format JSON, YAML ou Jinja et des fichiers de modèles au format Jinja.
- **Rendu de Contenu Dynamique :** Rend le contenu basé sur les fichiers de variables et de modèles sélectionnés en utilisant le moteur de modèles Jinja2.
- **Copie dans le Presse-papiers :** Offre une fonctionnalité pour copier le contenu rendu dans le presse-papiers.
- **Gestion des Erreurs :** Affiche des messages d'erreur si les fichiers ne sont pas sélectionnés ou si une erreur se produit lors du rendu.

## Prérequis
- Python 3.6, 3.7, 3.8, 3.9, 3.10 ou 3.11
- Tkinter (généralement inclus avec Python)
- Bibliothèque `jinja2`
- Bibliothèque `pyyaml`

## Installation
1. Clonez le dépôt ou téléchargez les fichiers du projet.
2. Installez les bibliothèques Python requises :
   ```bash
   pip install jinja2 pyyaml
   ```

## Utilisation
1. Exécutez le script `Main.py` pour lancer l'application GUI :
   ```bash
   python Main.py
   ```
2. Dans la fenêtre de l'application, sélectionnez le type de variables et de modèles que vous souhaitez utiliser à partir du menu déroulant.
3. Cliquez sur les boutons "Parcourir" pour sélectionner les fichiers de variables et de modèles.
4. Cliquez sur le bouton "Soumettre" pour rendre le contenu basé sur les fichiers sélectionnés.
5. Le contenu rendu sera affiché dans une nouvelle fenêtre avec une option pour le copier dans le presse-papiers.

## Structure du Projet
- `Main.py` : Contient le code principal de l'application, y compris l'interface graphique et la logique de sélection de fichiers et de rendu de contenu.
- `tools_jinja.py` : Contient des fonctions utilitaires pour lire les fichiers, fusionner les modèles et rendre le contenu en utilisant Jinja2.

## Contributions
Les contributions sont les bienvenues ! Si vous avez des suggestions d'améliorations ou de corrections de bugs, veuillez ouvrir un problème ou soumettre une demande de tirage sur le dépôt du projet.

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE.txt) pour plus de détails.

## Avertissements
- Assurez-vous que les fichiers sélectionnés sont au format correct pour éviter les erreurs lors du rendu.