#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     zone.py
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

class ZoneManager:

  # _items = set()
  _items_max = 4
  _items_min = 2
  # _categories_allocated = set()
  _zones = set()

  def __init__(
        _self,
        _discount_max,
        _discount_delta):
    # The M parameter from the request
    _self._discount_max = _discount_max
    # The P parameter from the request
    _self._discount_delta = _discount_delta

  def _zone_add(
        _self,
        _zone_name):
    _zone = {}
    _zone_new = not any(
                      ( _zone_name ==
                        _zone['name'] ) for _zone in _self._zones) 
    if ( _zone_new ):
      _self.zones.add(
        _zone)
    else:
      print(
        f"Zone '{_zone_name}' exists already.")

  def _item_add(
        _self,
        _item,
        _zone):
    _item_category = _item[
      'category']
    _item_discount_max = _item[
      'discount_max']
    _item_discount_max_allowed = _item_discount_max < _self._discount_max
    _category_item_allowed = _item_category in _categories_allowed
    _category_item_unused = _item_category not in _categories_allocated
    _zone_unique = not any(_item in _zone for _zone in _self.zones)
    if ( _item_discount_max_allowed and
         _category_item_allowedl and
         _category_item_unused ):
      _self._items.add(
        _item)
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
