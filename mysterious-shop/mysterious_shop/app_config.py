# -*- coding: utf-8 -*-

#
#    app_config.py
#
#    ----------------------------------------------------------------------
#    Copyright © 2018, 2019, 2020, 2021, 2022, 2023, 2024,
#                2025 Pellegrino Prevete
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


from appdirs import user_cache_dir as _user_cache_dir
from appdirs import user_config_dir as _user_config_dir
from appdirs import user_data_dir as _user_data_dir

from os.path import abspath as _abspath
from os.path import dirname as _dirname
from os.path import exists as _path_exists
from os.path import join as _path_join
import logging as _logging

from .util import _file_write, _file_read, _mkdir

class AppConfig:
  """Application configuration class.

  Attributes:
      _exec_path (str): path where the class resides;
      _app_name (str): name of the app.
      _app_author (str): name of the app author.
      _dirs (dict): paths of cache, data, config directories
  """

  _exec_path = _dirname(
                _abspath(
                  __file__))

  def __init__(
        _self,
        _app_name,
        _app_author,
        _debug=True):
    _logging.basicConfig(
      level=_logging.DEBUG)
    _self._logger = _logging.getLogger(
                     __name__)
    _self._attributes_set(
      _app_name,
      _app_author,
      _debug)
    _self._debug = _debug
    _self._dirs_set()
    _config_file = _path_join(
                     _self._dirs[
                       'config'],
                     "config.pkl")
    if not _path_exists(
             _config_file):
      _self._data = {}
    else:
      _self._data = _file_load(
                     str(
                       _config_file))

  def _attributes_set(
        _self,
        _app_name,
        _app_author,
        _debug):
    """Set global attributes for the class."""
    _self._debug = _debug
    _self._app_name = _app_name
    _self._app_author = _app_author
    _self._dirs = {
     'data':
       _user_data_dir(
         _app_name,
         _app_author),
     'config':
       _user_config_dir(
         _app_name,
         _app_author),
     'cache':
       _user_cache_dir(
         _app_name,
         _app_author)
    }

  def _dirs_set(
      _self):
    """Make user dirs for mysterious-shop.
    """
    for _dir_type, _path in _self._dirs.items():
      _self._logger.info(
        f"Creating directory for {_dir_type}")
      _mkdir(
        _path)
