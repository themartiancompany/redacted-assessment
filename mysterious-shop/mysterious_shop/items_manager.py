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

  _items = {}

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
    """A set of items to the managed items.

    Args:
      _items (iterable): an iterable containing the items to be added.
    """
    for _item in _items:
      _self._item_add(
        _item)
    
  def _item_new(
        _self,
        _item_name,
        _item_id,
        _item_price,
        _item_categories,
        _item_discount):
    """Creates and adds an item to be handled by the manager.

    The items are added as dictionaries to the data structure
    which is then saved to the database, currently a pickle
    file.

    Args:
      _item_name (str): string representing the item name;
      _item_id (int): id for the item;
      _item_price (float): floating point rational representing
                           the item price;
      _item_categories (list(int)): list of integers representing 
                                    the categories the item belongs to.
    """
    _item_price = float(
                    _item_price)
    _item = {
      "name":
        _item_name,
      "id":
        _item_id,
      "price":
        _item_price,
      "categories":
        _item_categories,
      "discount":
        _item_discount_max
    }
    _self._item_add(
      _item)

  def _item_add(
        _self,
        _item):
    """Adds an item to those of those handled by the manager.

    Args:
      _item (dict): a dictionary representing the item.
    """
    _self._item_validate(
      _item)
    _item_id = _item[
      'id']
    _self._items[
      _item_id] = _item

  def _item_remove(
        _self,
        _item):
    """Removes an item to those of those handled by the manager.

    Args:
      _item (dict): a dictionary representing the item.
    """
    _item_id = _item[
      'id']
    del _self.items[
      _item_id]

  def _item_price_type_check(
        _self,
        _item_price):
    """Checks the item price type.

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
    """Performs checks on items' price.

    Args:
      _item (dict): a dictionary representing the item.
    """
    _item_price = _item[
                    'price']
    _self._item_price_type_check(
      _item_price)
    _self._item_price_range_check(
      _item_price)

  def _item_discount_range_check(
        _self,
        _item):
    """Checks the item discount range.

    The allowed range interval is
    [_items_discount_min, _items_discount_max],
    where M is indicated in the request.

    Args:
      _item (dict): dictionary representing the item.
    """
    _item_discount = _item[
                       'discount']
    _items_discount_max = _self._items_discount_max
    if ( _items_discount_min > _item_discount ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' has discount "
               f"'{_item_discount_max}' lower than "
               f"allowed item minimum discount '{_items_discount_min}'."))
    if ( _items_discount_max < _item_discount ):
      raise ValueError(
              ("Not valid input: "
               f"item '{_item}' has discount "
               f"'{_item_discount_max}' greater than "
               f"allowed item maximum discount '{_items_discount_max}'."))

  def _item_validate(
        _self,
        _item):
    """Item validation.

    Args:
      _item (dict): dictionary representing the item.
    """
    _self._item_discount_range_check(
      _item)
    _self._item_price_check(
      _item)
