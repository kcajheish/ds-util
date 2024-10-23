class SegmentTreeLazy:
    def __init__(self, n, arr):
        self.INF = 10**20
        self.lazy = [0]*(4*n)
        self.tree = [0]*(4*n)
        self.build(arr, 1, 0, n-1)

    def build(self, arr, index, seg_left, seg_right):
        if seg_left == seg_right:
            self.tree[seg_left] = self.arr[index]
            return
        seg_mid = seg_left + (seg_right-seg_left)//2
        self.build(arr, 2*index, seg_left, seg_mid)
        self.build(arr, 2*index+1, seg_mid+1, seg_right)
        self.tree[index] = self.tree[2*index] + self.tree[2*index+1]

    def push(self, index):
        self.lazy[2*index] += self.lazy[index]
        self.lazy[2*index+1] += self.lazy[index]
        self.tree[2*index] += self.lazy[index]
        self.tree[2*index+1] += self.lazy[index]
        self.lazy[index] = 0

    def sum(self, index, seg_left, seg_right, query_left, query_right):
        if query_left > query_right:
            return 0

        if seg_left == query_left and seg_right == query_right:
            return self.tree[index]

        self.push(index)
        seg_mid = seg_left + (seg_right-seg_left)//2
        left_seg_sum = self.sum(2*index, seg_left, seg_mid, query_left, min(seg_mid, query_right))
        right_seg_sum = self.sum(2*index+1, seg_mid+1, seg_right, max(seg_mid+1, query_left), seg_right)
        return left_seg_sum + right_seg_sum

    def update(self, index, seg_left, seg_right, query_left, query_right, add):
        if query_left > query_right:
            return

        if seg_left == query_left and seg_right == query_right:
            self.tree[index] += add
            self.lazy[index] += add
            return

        self.push(index)
        seg_mid = seg_left + (seg_right-seg_left)//2
        self.update(2*index, seg_left, seg_mid, query_left, min(seg_mid, query_right))
        self.update(2*index, seg_mid+1, seg_right, max(seg_mid+1, query_left), query_right)
