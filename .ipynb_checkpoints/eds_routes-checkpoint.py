"""
EDS routes
"""
from urllib.parse import urljoin

TOKEN_URL = 'https://eds.chu-bordeaux.fr:5443/realms/eds-prod/protocol/openid-connect/token'
BASE_URL = 'http://eds-gateway:8080/'
SCHEMA_URLS = {
    'main': 'v3/api-docs',  # Main doc eds gateway
    'management': 'v3/api-docs?group=management', # EDS gateway management
    'candidate': 'services/edscandidatetermmicroservice/v3/api-docs',  # Candidate term microservice
    'cohort': 'services/edscohortmicroservice/v3/api-docs',  # Cohort microservice
    'lam': 'services/edsiamsystemmicroservice/v3/api-docs',  # LAM System Microservice
    'observation_import': 'services/edsobservationimportermicroservice/v3/api-docs',  # Observation importer microservice
    'observation': 'services/edsobservationmicroservice/v3/api-docs',  # Observation microservice
    'project': 'services/edsprojectmicroservice/v3/api-docs', # Project microservice
    'pseudonymizer': 'services/edspseudonymizermicroservice/v3/api-docs',  # Pseudonymizer microservice
    'query_builde': 'services/edsquerybuildermicroservice/v3/api-docs',  # Query Builder
    'query_engine': 'services/edsqueryenginemicroservice/v3/api-docs',  # Query engine
    'redcap': 'services/edsredcapmicroservice/v3/api-docs',  # RedCAP microservice
    'smartcrf': 'services/edssmartcrfmicroservice/v3/api-docs',  # SmartCRF microservice
    'metadata_import': 'services/metadataimportermicroservice/v3/api-docs',  # Metadata importer microservice
    'metadata': 'services/metadatamicroservice/v3/api-docs',  # Metadata Microservice
    'path_filter': 'services/pathfiltermicroservice/v3/api-docs',  # Path filter microservice
}

PROJECTS = {
    'list': urljoin(BASE_URL, 'services/edsprojectmicroservice/api/projects')
}

