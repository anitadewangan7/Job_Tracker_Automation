class CostTracker:

    total_calls = 0

    @classmethod
    def increment(cls):

        cls.total_calls += 1

    @classmethod
    def get_total_calls(cls):

        return cls.total_calls