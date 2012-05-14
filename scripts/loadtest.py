#!/usr/bin/env python
# Corey Goldberg 2009

import pylot.core.engine as pylot_engine
import os
import sys
import time



def main():
    """
    Usage: >python pylot_mini_loadtest.py   
    """
    url = sys.argv[1]
    num_agents = int(sys.argv[2])
    duration = int(sys.argv[3])
    pylot_engine.GENERATE_RESULTS = False
    print '\nmini web load test \n---------------------------------'
    agent_stats = run_loadtest(url, num_agents, duration)
    throughput = sum([stat.count for stat in agent_stats.values()]) / float(duration)
    print '%.2f reqs/sec' % throughput
    for agent_num, stats in agent_stats.iteritems():
        print 'agent %i : %i reqs : avg %.3f secs' % \
            (agent_num + 1, stats.count, stats.avg_latency)
        


def run_loadtest(url, num_agents, duration):
    """
    Runs a load test and returns a dictionary of statistics from agents.
    """
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    
    runtime_stats = {}
    req = pylot_engine.Request(url)
    lm = pylot_engine.LoadManager(num_agents, 0, 0, False, runtime_stats, [])
    lm.add_req(req)
    
    lm.start()
    time.sleep(duration)
    lm.stop()
    
    sys.stdout = original_stdout
    
    return runtime_stats



if __name__ == '__main__':
    main()