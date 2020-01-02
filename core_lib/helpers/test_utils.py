import string
import random

import os

from hydra._internal.hydra import GlobalHydra, Hydra
from hydra._internal.utils import detect_calling_file_or_module
from hydra.experimental import compose


def get_test_configuration(config_dir, config_file):
    config_override = os.environ['CONFIG_OVERRIDE'].split(',') if 'CONFIG_OVERRIDE' in os.environ else []

    GlobalHydra().clear()
    caller_stack_depth = 1
    calling_file, calling_module = detect_calling_file_or_module(caller_stack_depth + 1)
    Hydra.create_main_hydra_file_or_module(
        calling_file, calling_module, config_dir, strict=True
    )
    if config_override:
        print('Overriding configuration with : {}'.format(config_override))
    return compose(config_file, config_override)

def generate_random_string(length: int = 10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def generate_email(domain: str = 'fdna.com'):
    return '{}@{}'.format(generate_random_string(), domain)