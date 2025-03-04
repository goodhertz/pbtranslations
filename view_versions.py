from coldtype import *

release_order = [
    1, 2, 3, 4, 5, 6, 7, 9, 12, 15, 13, 24, 30, 36, 47, 29, 48, 19, 66
]

configs = ººsiblingºº("translatables/plugins/releases").glob("**/*.py")
configs = sorted(configs, key=lambda p: release_order.index(int(p.stem)))

VERSIONS = {}
for config in configs:
    catalog = config.stem
    layout = ººsiblingºº("layouts") / f"{catalog}_layout.py"
    if not layout.exists():
        layout = None

    VERSIONS[str(int(catalog))] = dict(
        config=config,
        layout=layout
    )