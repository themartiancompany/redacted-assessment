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

class DatabaseManager:

  # items = set()
  _dbs = {}

  def __init__(
        _self,
        _app_config):
    _db_load(
      "items")
    _db_load(
      "zones")

  def _db_path_get(
        _self,
        _type):
    return _path_join(
             _app_config._dirs[
               'config'],
             f"{_type}.db")

  def _db_load(
        _self,
        _db_type):
    _db_path = _self._db_path_get(
                 _type)
    _db = _self.dbs[
            _type]
    _db = { 'path':
              _path }
    if _path_exists(
         _path):
      _db = _file_read(
              _db[
                _type][
                  'path'])
      _db[
        _type][
          'blob'] = _db
    else:
      _db = set()
      _self._dbs[
        _type][
          'blob'] = _db
      _self._db_write(
        _type)

  def _db_write(
        _self,
        _db_type):
    _db_path = _self.dbs[
              _type][
                'path']
    _db = _self.dbs[
            _type][
              'blob']
    _file_write(
      _db,
      _db_path)

  def _item_add(
        _self,
        _name,
        _price,
        _category,
        _discount):
    _item = {
      "name":
        _name,
      "price":
        _price,
      "category":
        _category,
      "discount":
        _discount
    }
    _self._items.add(
      _item)
