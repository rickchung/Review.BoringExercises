# %%

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.val)

    def get_bfs(self):
        out = []
        queue = [self]
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue
            out.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
            print(cur.val, cur.left, cur.right)
        return out

    @staticmethod
    def from_list(values: List[int]):
        if not values:
            return None
        _values = [_ for _ in values]
        for i in range(len(_values)):
            if _values[i] is None:
                continue
            
            if type(_values[i]) is int:
                _values[i] = TreeNode(_values[i])

            li = (i+1) * 2 - 1
            lr = (i+1) * 2

            if li < len(_values):
                if _values[li]:
                    _values[li] = TreeNode(_values[li])
                    _values[i].left = _values[li]  

            if lr < len(_values):
                if _values[lr]:
                    _values[lr] = TreeNode(_values[lr])
                    _values[i].right = _values[lr]

        return _values[0]


if __name__ == "__main__":
    x = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
    print(x.get_bfs())

    x = TreeNode.from_list([2, 1, 3])
    print(x.get_bfs())
