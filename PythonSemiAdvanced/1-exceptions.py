try:
    x = 1 / 0
except ZeroDivisionError as exc:
    print("byl sobie error")

except KeyError:
    print("byl sobie error")

except AttributeError:
    print("byl sobie error")
finally:
    print("robie cos nie wazne czy byl error czy nie")
