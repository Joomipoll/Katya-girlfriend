import json
import urllib.parse
from pathlib import Path
from uuid import uuid1

from steamship.cli.create_instance import _create_instance

from personality import personality

girlfriend_json = Path("girlfriend.json")
config = json.load(Path("Katya.conf").open())

girlfriend = []
workspace = str(uuid1())
for name, personality in personality.items():
    config["personality"] = name
    instance = _create_instance(workspace=workspace,
                                instance_handle=name,
                                config=json.dumps(config))
    girlfriend.append(
        {
            "name": name.title(),
            "description": personality.byline,
            "profile_image": personality.profile_image,
            "chat_src": f"https://www.steamship.com/embed/chat?userHandle=enias&workspaceHandle={workspace}&instanceHandle={name}&ai_name={urllib.parse.quote(name.title())}"
        }
    )

json.dump(girlfriend, girlfriend_json.open("w"))
