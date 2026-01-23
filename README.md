# EDS API par JD
L'objectif des outils proposés dans ce dossier est d'accompagner l'utilisation des outils de l'EDS (API) par une API python bien construite.

## Création des modèles pydantic
Les modèles pydantic utilisés sont dérivés des schémas openAPI proposés sur la documentation de l'EDS.
La création se fait en deux étapes:
1) Récupération des schémas .json à partir de la doc de l'EDS (stockés dans le dossier `./schemas`)
2) Génération des modèles pydantic à partir des schémas (stockés dans le dossier `./models`)

L'execution nécessite l'installation préalable de `pydantic` et `datamodel-codegen`:
```bash
pip install -r ./requirements.txt
```

Génération des modèles :
```bash
python fetch_schemas.py
datamodel-codegen --input ./schemas --output ./eds_models --output-model-type pydantic_v2.BaseModel --type-mappings "string+byte=string" 
```


## Utilisation de l'API
