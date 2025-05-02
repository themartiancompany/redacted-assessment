#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     db_manager.py
#
#     ----------------------------------------------------------------------
#     Copyright © 2025  Pellegrino Prevete
# 
#     All rights reserved
#     ----------------------------------------------------------------------
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
# 
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# from sqlitedict import SqliteDict
from os.path import exists as _path_exists
from os.path import join as _path_join

from .util import _file_read, _file_write

class DbManager:

  # items = set()
  _dbs = {}

  def __init__(
        _self,
        _app_config):
    _self._db_load(
      "items")
    _self._db_load(
      "categories")
    _self._db_load(
      "zones")

  def _db_path_get(
        _self,
        _db_type):
    return _path_join(
             _app_config._dirs[
               'config'],
             f"{_db_type}.db")

  def _db_load(
        _self,
        _db_type):
    _db_path = _self._db_path_get(
                 _db_type)
    _db = _self.dbs[
            _db_type]
    _db = { 'path':
              _path }
    if _path_exists(
         _path):
      _db = _file_read(
              _db[
                _db_type][
                  'path'])
      _db[
        _db_type][
          'blob'] = _db
    else:
      _db = set()
      _self._dbs[
        _db_type][
          'blob'] = _db
      _self._db_write(
        _db_type)

  def _db_write(
        _self,
        _db_type):
    _db_path = _self.dbs[
              _db_type][
                'path']
    _db = _self.dbs[
            _db_type][
              'blob']
    _file_write(
      _db,
      _db_path)
