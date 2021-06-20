import json

from datetime import datetime
from typing import Any, List

class Connections():
    
    def __init__(self, json_file: str) -> None:
        
        f = open(json_file)
        json_dict = json.load(f)
        f.close()
        
        self.usernames = []
        self.urls = []
        self.datetime = []
        for user in json_dict[list(json_dict.keys())[0]]:
            self.usernames.append(user['string_list_data'][0]['value'])
            self.urls.append(user['string_list_data'][0]['href'])
            self.datetime.append(datetime.fromtimestamp(
                user['string_list_data'][0]['timestamp']))
            

def find_diff_connections(c1: Connections, c2: Connections) -> List[str]:
    """
    Find users in c1 but not in c2.
    """
    return list(set(c1.usernames) - set(c2.usernames))

def find_same_connections(c1: Connections, c2: Connections) -> List[str]:
    """
    Find users in both c1 and c2.
    """
    return list(set(c1.usernames) & set(c2.usernames))

def write_list_to_file(lst: List[Any], filename: str) -> None:

    with open(filename, 'w') as f:
        f.write("\n".join(map(str, lst)))
    f.close()
    
if __name__ == "__main__":
    
    following = Connections(json_file="following.json")
    followers = Connections(json_file="followers.json")
    pending_requests = Connections(json_file="pending_follow_requests.json")
    
    rude = find_diff_connections(following, followers)
    print("Rude length: ", len(rude))
    write_list_to_file(rude, "rude.txt")

    stalkers = find_diff_connections(followers, following)
    print("Stalkers length: ", len(stalkers))
    write_list_to_file(stalkers, "stalkers.txt")    
    
