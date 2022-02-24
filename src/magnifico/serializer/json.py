from cattr.preconf.json import make_converter


class JSONMixIn:
    """JSON serializer mixin for attrs classes."""

    def to_json(self):
        converter = make_converter()
        return converter.unstructure_attrs_asdict(self)
