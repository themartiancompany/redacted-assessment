# -*- coding: utf-8 -*-

#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     shop.py
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

from .app_config import AppConfig
from .db_manager import DbManager
from .categories_manager import CategoriesManager
from .items_manager import ItemsManager
from .zones_manager import ZonesManager

class Shop:

  def __init__(
        _self,
        **_shop_config):
    _self._app_config = AppConfig(
                          "mysterious-shop",
                          "Pellegrino Prevete",
                          True)
    _self._shop_config_init(
      **_shop_config)
    _self._db_manager = DbManager(
                          _self._app_config)
    _self._categories_manager = CategoriesManager(
                                  _self._db_manager._dbs[
                                    'categories'][
                                      'blob'])
    #     _items_price_max,
    #     _items_discount_max,
    #     _items):
    _self._items_manager = ItemsManager(
                                  _self._db_manager._dbs[
                                    'categories'][
                                      'blob'])

            )
    _self._zones_manager = ZonesManager()

  def _shop_config_init(
        _self,
        _cart_min_items=2,
        _cart_max_items=100,
        _zones_price_delta_min=1,
        _zones_price_delta_max=10000,
        _zones_discount_min=1,
        _zones_discount_max=70,
        _items_price_min=1,
        _items_price_max=5000,
        _categories_id_min=1,
        _categories_id_max=20,
        _items_discount_min=1,
        _items_discount_max=50):
    _shop_config = _self._app_config._data
    _shop_config[
      'cart_min_items'] = _cart
    _self._shop_config = _shop_config
