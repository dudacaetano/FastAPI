from typing import List, Optional
from database import database
from model.item import Item

'''
parecido com view da arquitetura mvc
'''

class ItemService:

    def create_item(item: Item) -> Item:

        database.items.append(item)
        return item
    
    def get_items() -> List[Item]:
        return database.items
    
    def get_item(item_id: int) -> Optional[Item]:
        for item in database.items:
            if item.id == item_id:
                return item
        return None
    
    def update_item(item_id: int, update_item: Item) -> Optional[Item]:
        for index, item in enumerate(database.items):
            if item.id == item_id:
                database.items[index] = update_item
                return update_item
        return None
    
    def delete_item(item_id: int) -> bool:
        for index, item in enumerate(database.items):
            if item.id == item_id:
                del database.items[index]
                return True 
        return False

        