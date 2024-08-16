#!/usr/bin/python3
""" LockedBoxs """


def canUnlockAll(boxes):
    """ canUnlockAllBoxs """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keyChain = set()
    keyChain.add(0)
    result = True
    while result:
        result = False
        for i, box in enumerate(boxes):
            if i in keyChain:
                for key in box:
                    if key < len(boxes) and key not in keyChain:
                        keyChain.add(key)
                        result = True
                        if len(keyChain) == len(boxes):
                            return True
    return False
