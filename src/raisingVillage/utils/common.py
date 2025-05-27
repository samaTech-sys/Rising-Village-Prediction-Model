import os 
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from raisingVillage import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Reads yaml file and returns 

    Args:
        path_to_yaml (Path): path like input 
        
    Raise: 
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: configbox type
    """
    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully" )
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty") 
    except Exception as e:
        raise e 
    
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): path to diirectories 
        verbose (bool, optional): Ignore if multiple directories are to be created. Defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict): 
    """
    Saves json file 

    Args:
        path (Path): path to json file 
        data (dict): data to be stored in json file 
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logger.info(f"json file saved at{path}")
        
@ensure_annotations
def load_json(path: Path)->ConfigBox:
    """
    Loads json file 

    Args:
        path (Path): path to json flle 

    Returns:
        ConfigBox: data as class atributes instead of dict
    """
    with open(path) as f:
        consent = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(consent)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file 

    Args:
        data (Any): data to be saved as binary
        path (Path): data to binary directory 
    """
    joblib.dump(value=data, filename= path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path)->Any:
    """
    Load binary data

    Args:
        path pah to binary data

    Returns:
        Any: any object stored in file 
    """
    data =joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    """
    Get size of file in KB 

    Args:
        path (Path): path to file 

    Returns:
        str: file path as string 
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
