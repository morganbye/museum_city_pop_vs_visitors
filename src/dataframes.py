#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Data frame manipulation utilities"""

import pandas as pd


def column_replace_pattern(
        df: pd.DataFrame,
        col: str,
        match: str,
        replace: str = r''
) -> pd.DataFrame:
    """Replace

    Parameters
    ----------
    df : pd.DataFrame
    col : column
    match : str
        regex type string to match against
    replace : str
        regex type string to replace with

    Returns
    -------

    """
    df[col].replace(
        inplace=True,
        regex=True,
        to_replace=match,
        value=replace,
    )

    return df
