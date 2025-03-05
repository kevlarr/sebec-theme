def merge_color_maps(*ds: dict[str, list[str]]) -> dict[str, list[str]]:
    rval = {}
    for d in ds:
        for key, values in d.items():
            final_values = rval.setdefault(key, [])
            final_values.extend(values)
    return rval

assert merge_color_maps({"one": [1, 2], "three": [3, 4]}, {"two": [2, 3], "three": [5, 6]}) == {
    "one": [1, 2],
    "two": [2, 3],
    "three": [3, 4, 5, 6],
}
