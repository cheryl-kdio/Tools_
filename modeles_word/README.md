# Modèles Word — style LaTeX

Quatre modèles `.dotx` sans macros, conçus pour Word de bureau en français.

| Modèle | Usage |
|---|---|
| `Base.dotx` | Document vierge avec la charte et les styles préconfigurés. |
| `Article.dotx` | Article scientifique : résumé, cadre théorique, méthodologie, résultats, références, annexe. |
| `Note_technique.dotx` | Note de finance quantitative, modélisation ou documentation de code. |
| `Rapport.dotx` | Rapport long avec couverture, résumé exécutif et champ de table des matières. |

## Utilisation

1. Décompresser l'archive et conserver les fichiers `.dotx` dans un dossier de modèles.
2. Double-cliquer sur le modèle voulu pour créer un nouveau document, ou le sélectionner dans Word > Fichier > Nouveau, si le dossier est configuré comme emplacement de modèles personnels.
3. Remplacer les textes entre crochets, y compris le titre court et l'auteur de l'en-tête. Les sauts de page d'exemple peuvent être supprimés pour laisser le texte s'écouler naturellement.
4. Enregistrer le nouveau document en `.docx`. Pour modifier le modèle lui-même, l'ouvrir via Fichier > Ouvrir.

Sous Windows, l'emplacement de modèles personnels peut être défini dans Fichier > Options > Enregistrement. Sur Mac, les emplacements et les noms des menus varient selon la version de Word.

## Charte

- A4, portrait, marges de 2,5 cm, corps Times New Roman 11 pt, interligne 1,15, texte justifié.
- Titres hiérarchiques 1 à 9 liés à une liste multiniveau. Ne pas taper les numéros à la main.
- Titre du document centré, 25 pt ; sous-titre 13 pt ; titres 1/2/3 : 15/12/11 pt.
- Équations natives Word, police mathématique Cambria Math ; style Équation avec tabulations centrée et droite.
- Styles Définition, Hypothèse, Théorème, Proposition, Lemme, Corollaire, Démonstration, Exemple, Remarque, Limitation, Résultat, Bibliographie, Code Python (Courier New), Tableau texte et Légende.
- Les tableaux d'exemple suivent une présentation de type booktabs : règles horizontales, pas de quadrillage vertical.

Pour une apparence encore plus proche de LaTeX, installer séparément Latin Modern Roman depuis une source officielle, puis modifier les styles de texte. Aucune police externe n'est incluse ni nécessaire. Le rendu des équations et le moteur de composition de Word restent différents de TeX.

## Équivalents LaTeX dans Word

| LaTeX | Word |
|---|---|
| `\section`, `\subsection` | Styles Titre 1, Titre 2 |
| `equation` | Insertion > Équation ; style Équation |
| `\label`, `\ref` | Signet + champ REF / Références > Renvoi |
| `\caption` | Références > Insérer une légende |
| `\tableofcontents` | Références > Table des matières |
| `theorem`, `definition` | Styles dédiés ; recopier un exemple contenant le champ SEQ pour obtenir une numérotation, ou insérer un champ SEQ distinct par type |
| `\bibliography` | Références > Gérer les sources / Zotero (facultatif) |

Les équations sont de vrais objets mathématiques éditables et non des images. Dans les versions de Word qui le permettent, sélectionner le format de saisie LaTeX dans l'onglet Équation, puis convertir en format professionnel. Exemple : `\frac{P_T-P_0+C}{P_0}`. La syntaxe prise en charge n'est pas celle d'un moteur LaTeX complet.

Les exemples d'équations, de tableaux et de certains énoncés comportent des champs SEQ. La note contient également un exemple de renvoi REF à une équation. Pour dupliquer une équation, copier le paragraphe complet, créer un nouveau signet unique si un renvoi est nécessaire, puis actualiser les champs. Un style seul ne crée pas automatiquement un champ de numérotation. Pour les figures et tableaux supplémentaires, employer Références > Insérer une légende et le même libellé que celui choisi dans le document. Les références bibliographiques sont des exemples de texte à remplacer et non une base de références automatique.

Pour actualiser les numéros et le sommaire, sélectionner le document et mettre à jour les champs (Ctrl+A puis F9 sous Windows ; sur Mac utiliser la commande de mise à jour des champs ou la touche de fonction appropriée). Le sommaire du rapport doit être actualisé dans Word ; choisir la mise à jour de toute la table. Les champs des en-têtes et pieds de page peuvent nécessiter une actualisation séparée.

## Généraliser les styles à Word

Base.dotx n'est pas Normal.dotm. Ne pas renommer un `.dotx` en `.dotm`.

Pour les nouveaux documents, utiliser Base.dotx ou importer ses styles dans le modèle Normal.dotm via l'organisateur de styles de Word de bureau (faire d'abord une sauvegarde du modèle Normal). La numérotation, le thème et les paramètres de page peuvent nécessiter une configuration séparée dans Normal.dotm. Pour les documents existants, attacher le modèle ou copier les styles, sur une copie de test ; la mise en forme directe, les marges et les en-têtes ne sont pas automatiquement remplacés.

## Vérification et limites

Les packages ont été créés au format OOXML template et les documents équivalents rendus et inspectés dans LibreOffice. L'ouverture dans Microsoft Word et la mise à jour effective de tous les champs dans Word n'ont pas été testées ici. La pagination et les substitutions de polices peuvent varier. Aucun fichier local de Word n'a été modifié.
