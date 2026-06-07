"""
Utility module for deterministic behavior.
"""

import random
import numpy as np


def set_seed(seed: int = 42):
    """
    Set deterministic random seeds.
    """

    random.seed(seed)
    np.random.seed(seed)