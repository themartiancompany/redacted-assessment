#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     item_manager.py
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

class ItemManager:

  _items = set()

  def __init__(
        _self,
        _price_max,
        _items):
    _self._price_max = _price_max
    _self._items = _items

  def _items_add(
        _self,
        _items):
    for _item in _items:
      _self._item_add(
        _item)
    
  def _item_add(
        _self,
        _name,
        _price,
        _category,
        _discount):
    _price = float(
               _price)
    # _self._item_price_check(
    #   _price)
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
    _self._item_validate(
      _item)
    _self._items.add(
      _item)

  def _item_price_check(
        _self,
        _price):
    _price_type = type(
                    _price)
    _price_max = _self._price_max
    if ( _price_type != int or
         _price_type != float ):
      raise TypeError(
              ("Invalid input: "
               f"price '{_price}' must "
               "be a number."))
    if not _price > 0:
      raise ValueError(
              ("Invalid input: "
               f"price '{_price}' must "
               "be a positive number."))
    if _price > _price_max:
      raise ValueError(
              ("Invalid input: "
               f"price '{_price}' must "
               f"be lower than '{_price_max}'."))

  def _item_discount_max_check(
        _self,
        _item):
    _item_discount_max = _item[
                           'discount_max']
    _discount_max = _self._discount_max
    if ( _item_discount_max > _discount_max ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' has discount "
               f"'{_item_discount_max}' greater than "
               f"allowed max discount '{_discount_max}'."))

  def _item_validate(
        _self,
        _item):
    _item_price = _item[
                    'price']
    _self._item_price_check(
      _item_price)
