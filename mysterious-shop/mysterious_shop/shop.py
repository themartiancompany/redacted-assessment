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
from .db import Db
from .zone_manager import ZoneManager

class Shop:

  def __init__(
        _self):
    _self._app_config = AppConfig(
                      "mysterious-shop",
                      "Pellegrino Prevete",
                      True)
    _self._db = Db(
                  _self._app_config)
    _self._zone_manager = ZoneManager()
