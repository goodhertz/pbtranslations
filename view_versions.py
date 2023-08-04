from coldtype import *

VERSIONS = {}
for config in sorted(__sibling__("translatables/plugins/releases").glob("**/*.py")):
    catalog = config.stem
    VERSIONS[str(int(catalog))] = dict(
        config=config,
        layout=__sibling__("layouts") / f"{catalog}_layout.py"
    )