#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     items_manager.py
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

class ItemsManager:

  _items = set()

  def __init__(
        _self,
        _items_price_min,
        _items_price_max,
        _items_discount_min,
        _items_discount_max,
        _items):
    _self._items_price_min = _items_price_min
    _self._items_price_max = _items_price_max
    _self._items_discount_min = _items_discount_min
    _self._items_discount_max = _items_discount_max
    _self._items = _items

  def _items_add(
        _self,
        _items):
    for _item in _items:
      _self._item_add(
        _item)
    
  def _item_new(
        _self,
        _item_name,
        _item_price,
        _item_categories,
        _item_discount_max):
    """Adds an item to the items managed by the manager.

    The items are added as dictionaries to the data structure
    which is then saved to the database, currently a pickle
    file.

    Args:
      _item_name (str): string representing the item name;
      _item_price (float): floating point rational representing
                           the item price.
      _item_categories (list(int)): list of integers representing 
                                    the categories the item belongs to;
    """
    _item_price = float(
                    _item_price)
    _item = {
      "name":
        _item_name,
      "price":
        _item_price,
      "category":
        _item_category,
      "discount":
        _item_discount_max
    }
    _self._item_add(
      _item)

  def _item_add(
        _self,
        _item):
    _self._item_validate(
      _item)
    _self._items.add(
      _item)

  def _item_price_type_check(
        _self,
        _item_price):
    """Checks the item price type

    Allowed values are integers or floating point
    rationals.

    Args:
      _item_price (float): float representing the item price.
    """
    _item_price_type = type(
                         _item_price)
    if ( _item_price_type != int or
         _item_price_type != float ):
      raise TypeError(
              ("Invalid input: "
               f"price '{_price}' must "
               "be a number."))

  def _item_price_range_check(
        _self,
        _item_price):
    """Checks the item price range

    The range must be 0 < price < price_max
    where price_max is indicated in the request

    Args:
      _item_price (float): float representing the item price.
    """
    _items_price_min = _self._items_price_min
    _items_price_max = _self._items_price_max
    if _item_price > _items_price_min:
      raise ValueError(
              ("Invalid input: "
               f"price '{_price}' must "
               "be greater than '{_items_price_min}'."))
    if _item_price > _items_price_max:
      raise ValueError(
              ("Invalid input: "
               f"price '{_item_price}' must "
               f"be lower than '{_items_price_max}'."))

  def _item_price_check(
        _self,
        _item):
    _self._item_price_type_check(
      _item_price)
    _self._item_price_range_check(
      _item_price)

  def _item_discount_range_check(
        _self,
        _item):
    """Checks the item discount range

    The range must be
    _items_discount_min < item_discount < _items_discount_max
    where M is indicated in the request.

    Args:
      _item (dict): dictionary representing the item.
    """
    _item_discount_max = _item[
                           'discount']
    _items_discount_max = _self._items_discount_max
    if ( _items_discount_min > _item_discount ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' has discount "
               f"'{_item_discount_max}' greater than "
               f"allowed item max discount '{_items_discount_max}'."))
    if ( _items_discount_max < _item_discount ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' has discount "
               f"'{_item_discount_max}' greater than "
               f"allowed item max discount '{_items_discount_max}'."))

  def _item_validate(
        _self,
        _item):
    _item_price = _item[
                    'price']
    _self._item_price_check(
      _item_price)
