#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     db.py
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

class Db:

  items = set()

  def __init__(
        self):
    pass 

  def _item_add(
        self,
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
    _items.add(
      _item)
