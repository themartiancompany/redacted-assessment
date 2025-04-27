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


from appdirs import user_data_dir as _user_cache_dir
from appdirs import user_data_dir as _user_config_dir
from appdirs import user_data_dir as _user_data_dir

from os.path import abspath as _abspath
from os.path import dirname as _dirname
from os.path import exists as _path_exists
from os.path import join as _path_join

from .util import _file_write, _file_read

class AppConfig:
    """Application configuration class.

    Attributes:
        exec_path (str): path where the class resides;
        appname (str): name of the app.
        appauthor (str): name of the app author.
        dirs (dict): paths of cache, data, config directories
    """

    exec_path = _dirname(
                  _abspath(
                    __file__))

    appname = "shop"
    appauthor = "Pellegrino Prevete"
    dirs = {
      'data':
        _user_data_dir(
          appname,
          appauthor),
      'config':
        _user_config_dir(
          appname,
          appauthor),
      'cache':
        _user_cache_dir(
          appname,
          appauthor)
    }

    def __init__(
          self,
          debug=True):
      self.debug = debug
      self._set_dirs()
      _config_file = _path_join(
                       self.dirs[
                         'config'],
                       "config.pkl")
      if not _path_exists(
               _config_file):
          self.data = {}
      else:
          self.data = _file_load(
                        str(_config_file))

