def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "email": str(item["email"]),
        "password": str(item["password"])
    }
    
def usersEntity(lst_entity) -> list:
    return [userEntity(item) for item in lst_entity]