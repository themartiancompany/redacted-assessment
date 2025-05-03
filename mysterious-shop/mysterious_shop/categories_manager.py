#  SPDX-License-Identifier: AGPL-3.0-or-later

#
#     categories_manager.py
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

class CategoriesManager:

  _categories = {}

  def __init__(
        _self,
        _categories):
    # The request wants only 20 categories btw
    for _category in _categories:
      _category_add(
        _category)

  def _category_exists_check(
        _self,
        _category):
    _category_id = _category[
                     'id']
    _categories_ids = _self.categories.keys()
    if category_id in _categories_ids:
      raise Exception(
              ("Invalid input: "
               "it already exists a category "
               "with id '{_category_id}'."))

  def _category_new(
        _self,
        _category_name,
        _category_id,
        _items={}):
    """Creates a new category.

    Args:
      _category_name (str): a string representing the category name;
      _category_id (int): an integer representing the category id;
      _items (dict): the items dictionary.
    """
    _category = {
      'name':
        _category_name,
      'items':
        _items,
      'id':
        _category_id,
    }
    _self.category_add(
      _category)

  def _category_add(
        _self,
        _category):
    """Adds a category to those handled by the manager.

    Args:
      _category (dict): a dictionary representing the category.
    """
    _self._category_exists_check(
      _category)
    _self.category[
      _category_id] = _category

  def _category_remove(
        _self,
        _category):
    """Removes a category to those handled by the manager.

    Args:
      _category (dict): a dictionary representing the category.
    """
    _category_id = _category[
                     'id']
    _categories = _self.categories
    del _categories[
          _category_id]

  def _categories_add(
        _self,
        _categories):
    """Adds multiple categories to those handled by the manager.

    Args:
      _categories (iterable): an iterables of dictionaries
                              representing the categories.
    """
    for _category in _categories:
      _self._category_add(
        _category)

  def _category_validate(
        _self,
        _category):

    pass
