#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     item.py
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

class Item:

  # items = set()

  def __init__(
        _self,
        _name,
        _price,
        _category,
        _discount):
    _self._db_items_path = _path_join(
                             _app_config._dirs[
                               'config'],
                             "items.db")
    if _path_exists(
         _self._db_items_path):
      _self._items = _self._db_load(
                       _self._db_items_path)
    else:
      _self._items = set()
      _self._db_write(
        _self._items,
        _self._db_items_path)

  def _db_load(
        _self,
        _db_path):
    _db = _file_read(
            _db_path)
    return _db

  def _db_write(
        _self,
        _obj,
        _db_path):
    _file_write(
            _obj,
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
