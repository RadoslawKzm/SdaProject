def long_short(tup: tuple[str, str]) -> str:
    # if len(tup[0]) < len(tup[1]):
    #     return f"{tup[0]}{tup[1]}{tup[0]}"
    # return f"{tup[1]}{tup[0]}{tup[1]}"
    return (
        f"{tup[0]}{tup[1]}{tup[0]}"
        if len(tup[0]) < len(tup[1])
        else f"{tup[1]}{tup[0]}{tup[1]}"
    )


if __name__ == "__main__":
    print(long_short(("1", "22")))
