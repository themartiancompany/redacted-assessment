# -*- coding: utf-8 -*-

#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     dummy_init.py
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

from .shop import Shop

class DummyInit:

  def __init__(
        _self):
    _shop = Shop()

  def _categories_init(
        _self,
        _shop)
    _category_manager = _shop._category_manager
    for _category_id in range(20):
      _category
    _categories = _shop._db_manager.
