# Formulaire de Réponse Stage ESP

Un outil simple basé sur Flask permettant de remplir et d'imprimer le formulaire de réponse pour les demandes de stage de l'ESP (École Supérieure Polytechnique).

## Vue d'ensemble

Cet outil permet aux entreprises de :

- Remplir un formulaire interactif de réponse de stage en ligne
- Imprimer le formulaire rempli pour archivage

**Aucune donnée n'est stockée sur le serveur.**

## Technologies utilisées

- **Backend** : Flask (Python)
- **Formulaire** : Flask-WTF (WTForms)
- **Frontend** : HTML, CSS, JavaScript

## Fonctionnalités

- Formulaire interactif avec validation
- Mise en page optimisée pour l'impression
- Design responsive pour une utilisation sur mobile et ordinateur
- Interface utilisateur simple et directe

## Installation et configuration

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Cloner le dépôt :

   ```
   git clone https://github.com/mamour-dx/formulaire-reponse-stage-esp.git
   cd formulaire-reponse-stage-esp
   ```

2. Créer et activer un environnement virtuel :

   ```
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :

   ```
   pip install -r requirements.txt
   ```

4. Exécuter l'application :

   ```
   python app.py
   ```

5. Ouvrir votre navigateur et accéder à `http://localhost:8080`

## Structure du projet

```
formulaire-reponse-stage-esp/
├── app.py                  # Point d'entrée de l'application
├── forms.py                # Définitions des formulaires
├── requirements.txt        # Dépendances Python
├── README.md               # Ce fichier
├── static/                 # Ressources statiques
│   ├── css/
│   │   └── style.css       # Feuille de style principale
│   ├── js/
│   │   └── scripts.js      # JavaScript côté client
│   └── images/             # Images
├── templates/              # Templates HTML
│   ├── base.html           # Template de base
│   ├── form.html           # Formulaire de stage
│   └── 404.html            # Page d'erreur 404
```

## Utilisation

1. Accédez à la page d'accueil pour remplir le formulaire de stage
2. Remplissez tous les champs requis avec les détails de l'entreprise et du stage
3. Utilisez le bouton "Imprimer le formulaire" pour obtenir une version papier

## Confidentialité

Cet outil est conçu pour protéger votre vie privée :

- **Aucune donnée n'est stockée sur le serveur**
- Tous les formulaires sont traités uniquement dans votre navigateur
- Aucune information n'est envoyée à des tiers

## Optimisation pour l'impression

La mise en page pour l'impression a été optimisée :

- **Le formulaire s'adapte à une seule page A4** : Tout le contenu s'intègre correctement sur une page A4 standard
- **Typographie améliorée** : Tailles de police et épaisseurs optimisées
- **Disposition horizontale** : Les champs de téléphone, télécopie et email s'affichent horizontalement
- **Interface simplifiée** : Interface épurée axée sur les données du formulaire
- **Style spécifique à l'impression** : CSS complet spécifique à l'impression

Pour utiliser la fonction d'impression, cliquez simplement sur le bouton "Imprimer le formulaire".

## Remarque

Ce projet n'est pas affilié par le département génie informatique et a été maintenu par les étudiants pour faciliter le remplissement des formulaires des réponses pour les demandes de stages.

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
