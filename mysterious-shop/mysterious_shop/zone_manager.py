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

  _zone_items_max = 4
  _zone_items_min = 2
  _zones = set()

  def __init__(
        _self,
        _discount_max,
        _price_delta_max,
        _zones):
    # The M parameter from the request
    _self._discount_max = _discount_max
    # The P parameter from the request
    _self._price_delta_max = _price_delta_max
    for _zone in _zones:
      _zone_add(
        _zone)

  def _zone_add(
        _self,
        _zone_name,
        _categories_allowed=set()):
    _zone_exists = any(
                     ( _zone_name ==
                       _zone['name'] ) for _zone in _self._zones)
    if ( _zone_exists ):
      raise ValueError(
              f"Zone '{_zone_name}' exists already.")
    else:
      _zone = {
        'name':
          _zone_name,
        'items':
          set(),
        'categories_allowed':
          _categories_allowed,
        'categories_allocated':
          set()
      }
      _self.zones.add(
        _zone)

  def _zone_items_min_check(
        _self,
        _zone):
    _zone_items = _zone[
                    'items']
    _zone_items_amount = len(
                           _zone_items)
    _zone_items_min = _self._zone_items_min
    if ( _item_items_amount > _zone_items_min ):
      raise ValueError(
              ("Not valid input: "
               f"zone '{_zone}' has already "
               f"'{_zone_items_amount}' items in it."))

  def _zone_items_max_check(
        _self,
        _zone):
    _zone_items = _zone[
                    'items']
    _zone_items_amount = len(
                           _zone_items)
    _zone_items_max = _self._zone_items_max
    if ( _item_items_amount > _zone_items_max ):
      raise ValueError(
              ("Not valid input: "
               f"zone '{_zone}' has already "
               f"'{_zone_items_amount}' items in it."))


  def _item_category_allowed_check(
        _self,
        _item,
        _zone):
    _item_category = _item[
                       'category']
    _categories_allowed = _zone[
                            'categories_allowed']
    if not _item_category in _categories_allowed:
      raise ValueError(
              ("Not valid input: "
               f"category {_item_category} for item "
               f"'{_item}' not in zone's allowed categories "
               f"'{_categories_allowed}'."))

  def _item_zone_single_check(
        _self,
        _item,
        _zone):
    _zone_items = _zone[
                    'items']
    if _item in _zone_items:
      pass
    elif any(
           _item in _zone[
                      'items'] for _zone in _self.zones):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' already in one"))
               f"of the zones."))

  def _item_zone_price_delta_max_check(
        _self,
        _item,
        _zone):
    _item_price = _item[
                    'price']
    _zone_items = _zone[
                    'items']
    _price_delta_max = _self._price_delta_max
    if any(
         ( abs(
             _item_price - _item[
                             'price'] ) >
           _price_delta_max ) for _item in _zone_items ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' total price '{_item_price}' "
               "differs from the total price of one of the items "
               f"in zone '{_zone}' more than"
               f"{_price_delta_max}."))

  def _item_zone_add(
        _self,
        _item,
        _zone):
    _self._zone_items_max_check(
      _zone)
    _self._item_discount_max_check(
      _item)
    _self._item_category_allowed_check(
      _item,
      _zone)
    _self._item_category_unused_check(
      _item,
      _zone)
    _self._item_zone_single_check(
      _item,
      _zone)
    self._item_zone_price_delta_max_check(
      _item,
      _zone)
    _zone_items = _zone[
                    'items']
    _zone_categories = _zone[
                         'categories_allocated']
    _item_category = _item[
                       'category']
    _zone_categories.add(
      _item_category)
    _zone_items.add(
      _item)

  def _item_zone_remove(
        _self,
        _item,
        _zone):
    _zone_items = _zone[
                    'items']
    _zone_items.remove(
      _items)

  def _items_zone_add(
        _self,
        _items,
        _zone):
    for _item in _items:
      _self._item_zone_add(
        _item)

  def _zone_validate(
        _self,
        _zone):
    _self._zone_items_min_check(
      _zone)
