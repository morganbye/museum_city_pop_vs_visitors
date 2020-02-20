#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit test package for ``src.dataframes``."""

import pandas as pd
import pandas.testing as pdt

import src.dataframes


class TestColumnReplacePattern:
    """Testing for ``column_replace_pattern``."""

    abc = ['foo', 'bar', 'baz']
    xyz = ['abc', 'cde', 'feg']
    cit = ['a[1]', 'b[2]', 'c[3]']

    def test_plain_str_removal(self):
        """Test a plain string is removed."""
        # GIVEN
        df = pd.DataFrame({
            "abc": self.abc
        })
        expected_result = pd.DataFrame({"abc": ['foo', 'car', 'caz']})

        # WHEN
        result = src.dataframes.column_replace_pattern(
            df,
            "abc",
            r"b",
            r"c"
        )

        # THEN
        pdt.assert_frame_equal(expected_result, result)

    def test_other_columns_unaffected(self):
        """Test that other columns are not mutated."""
        # GIVEN
        df = pd.DataFrame({
            "abc": self.abc,
            "xyz": self.xyz
        })
        expected_result = pd.DataFrame({
            "abc": ['foo', 'car', 'caz'],
            "xyz": self.xyz,
        })

        # WHEN
        result = src.dataframes.column_replace_pattern(
            df,
            "abc",
            r"b",
            r"c"
        )

        # THEN
        pdt.assert_frame_equal(expected_result, result)

    def test_patterned_str_removal(self):
        """Test a regex string is removed."""
        # GIVEN
        df = pd.DataFrame({
            "cit": self.cit
        })
        expected_result = pd.DataFrame({
            "cit": ['a', 'b', 'c'],
        })

        # WHEN
        result = src.dataframes.column_replace_pattern(
            df,
            "cit",
            r"\[\S\]",
            r""
        )

        # THEN
        pdt.assert_frame_equal(expected_result, result)
