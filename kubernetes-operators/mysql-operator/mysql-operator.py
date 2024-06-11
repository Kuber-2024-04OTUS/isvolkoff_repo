from kubernetes import client
from os import path
import kopf
import yaml

def create_pvc(storage_size, name, namespace, logger):
    pathName = path.join(path.dirname(__file__), 'pvc-temp.yaml')
    tmpl = open(pathName, 'rt').read()
    text = tmpl.format(name=name, storage_size=storage_size)
    data = yaml.safe_load(text)
    kopf.adopt(data)
    api = client.CoreV1Api()
    obj = api.create_namespaced_persistent_volume_claim(
        namespace=namespace,
        body=data,
    )
    logger.info(f"PVC child is created: {obj}")    

def create_deploy(image, name, namespace, password, logger):
    pathName = path.join(path.dirname(__file__), 'deploy-temp.yaml')
    tmpl = open(pathName, 'rt').read()
    text = tmpl.format(name=name, image=image,  password= password)
    data = yaml.safe_load(text)
    kopf.adopt(data)
    api = client.AppsV1Api()
    obj = api.create_namespaced_deployment(
        namespace=namespace,
        body=data,
    )
    logger.info(f"Deploy is created: {obj}")

def create_service(name, namespace, port, logger):
    with open(path.join(path.dirname(__file__), 'svc-temp.yaml')) as file:
        text = (file.read()).format(name=name, port=port)
        data = yaml.safe_load(text)
        kopf.adopt(data)
        api = client.CoreV1Api()
        obj = api.create_namespaced_service(
            namespace=namespace,
            body=data,
        )
        logger.info(f"Service is created: {obj}")  

    
@kopf.on.create('mysqls')
def create_fn(spec, name, namespace, logger, **kwargs):
    storage_size = spec.get('storage_size')
    image = spec.get('image')
    password = spec.get('password')
    port = spec.get('port')
    
    create_pvc(storage_size, name, namespace, logger)
    create_deploy(image, name, namespace, password, logger)
    create_service(name, namespace, port, logger)
    