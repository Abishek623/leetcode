
class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # component[i] stores which connected component node i belongs to
        component = [0] * n
        comp = 0

        for i in range(1, n):
            # If gap is greater than maxDiff,
            # start a new component
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            component[i] = comp

        # Answer the queries
        answer = []

        for u, v in queries:
            answer.append(component[u] == component[v])

        return answer