# -*- coding: utf-8 -*-

#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#    util.py
#
#    ----------------------------------------------------------------------
#    Copyright © 2018, 2019, 2020, 2021, 2022,
#                2023, 2024, 2025 Pellegrino Prevete
#
#    All rights reserved
#    ----------------------------------------------------------------------
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from os import makedirs as _makedirs
from os import umask as _umask
from pickle import dump as _pickle_dump
from pickle import load as _pickle_load

def _file_write(
    _variable,
    _path):
  """Save variable on given path using Pickle

  Args:
    _variable: what to save
    _path (str): path of the output
  """
  with open(
         _path,
         'wb') as _f:
    _pickle_dump(
      _variable,
      _f)

def _file_read(
      _path):
  """Load variable from Pickle file

  Args:
    _path (str): path of the file to load

  Returns:
    variable read from path
  """
  with open(
         _path,
         'rb') as _f:
    _variable = _pickle_load(
                  _f)
  return _variable

def _mkdir(
      _dir,
      _mode=0o755):
  """Creates a directory.

  Args:
    _path (str): path of the file to load

  Returns:
    variable read from path
  """

  try:
    _original_umask = _umask(
                        0)
    _makedirs(
      _dir,
      _mode)
  except OSError:
    pass
  finally:
    _umask(
      _original_umask)
