class Cell_exec_time:

    # the test is actually run in setup_cache
    # this allows running it once and getting multiple results
    # here mean and stddev
    def setup_cache(self):
        from. performance_test import test_performance
        mean, stddev = test_performance()
        return {'mean': mean, 'stddev': stddev}

    def track_mean(self, results):
        return results['mean']

    def track_stddev(self, results):
        return results['stddev']
