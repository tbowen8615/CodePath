"""
def find_task_pair(task_times, available_time):

    for i in range(len(task_times)):
        for j in range(i + 1, len(task_times)):
            if task_times[i] + task_times[j] == available_time:
                return True
    
    return False

task_times = [45, 60]
available_time = 105
print(find_task_pair(task_times, available_time))

"""

"""
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

print(extract_nft_names(nft_collection))"
"""

"""
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names += nft["name"]
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

print(extract_nft_names(nft_collection))"
"""

def identify_popular_creators(nft_collection):

    result_list = []
    new_set = set()

    for nft in nft_collection:
        if nft["creator"] in new_set:
            result_list.append(nft["creator"])

        else:
            new_set.add(nft["creator"])

    return result_list

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

print(identify_popular_creators(nft_collection))