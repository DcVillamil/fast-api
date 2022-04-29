def superEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "age": item["age"],
        "country": item["country"],
        "superpower": item["superpower"],
        "universe": item["universe"],

    }

def supersEntity(entity) -> list:
   return [superEntity(item) for item in entity]