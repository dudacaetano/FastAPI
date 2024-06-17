from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}



menu = [
    {
        'id' : 1,
        'titulo': 'compras',
        'prioridade': 'alta',
        'data': '2-6'

    },

    {   'id' : 2,
        'titulo': 'trabalhos',
        'prioridade': 'media',
        'data': '8-6'

    },

    {
        'id' : 3,
        'titulo': 'shopping',
        'prioridade': 'baixa',
        'data': '17-6'

    }
]


class Item(BaseModel):
    titulo: str
    prioridade: str
    data: str

class UpdateItem(BaseModel):
    titulo: str
    prioridade: str
    data: str


@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'ERROR': 'Item does not exist'}
    
    return{'Item': search[0]}

@app.get('/get-by-titulo')
def get_item(titulo: Optional[str] = None):

    search = list(filter(lambda x: x["titulo"] == titulo, menu))

    if search == []:
        return{'item': 'Does not exist'}
    
    return{'Item': search[0]}


@app.get('/list-menu')
def list_menu():
    return{'Menu': menu}


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search != []:
        return{'ERROR': 'Item exist'}
    
    item = item.dict()
    item['id'] = item_id

    menu.append(item)

    return item


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):

    search = list(filter(lambda x: x['id'] == item_id, menu))

    if search == []:
        return{'Item': 'Does not exist'}
    
    if item.titulo is not None:
        search[0]['titulo'] = item.titulo

    if item.prioridade is not None:
        search[0]['prioridade'] = item.prioridade
    
    if item.data is not None:
        search[0]['data'] = item.data
    
    return search


@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Item': 'Does not exist'}
    
    for i in range(len(menu)):
        if menu[i]['id'] == item_id:
            del menu[i]
            break
    return{'Message': 'Item deleted successfully'}