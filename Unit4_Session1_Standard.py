def extract_nft_names(nft_collection):
    names_list = []

    for i in nft_collection:
        names_list.append(i["name"])
    
    return names_list


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

print(extract_nft_names(nft_collection))