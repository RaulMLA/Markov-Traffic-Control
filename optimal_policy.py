from probabilty_calculation import CalculateProbabilities
from cost_model import GetRewardFunction

S, A, P = CalculateProbabilities()
R = GetRewardFunction()

def R(s, a):
    if s == N:
        return 1
    else:
        return 0

def OptimalPolicy(S: list, A: list, P: str, R: str):
    """
    S -> Set of states.
    A -> Set of actions.
    P -> Transition function.
    R -> Reward function.
    """

    policy = {S: A[0] for s in S}

    while True:
        old_policy = policy.copy()

        V = PolicyEvaluation(policy, S)

        policy = PolicyImprovement(V, S, A)

        if all(old_policy[s] == policy[s] for s in S):
            break



def PolicyEvaluation(policy, S):
    """
    policy ->
    S -> Set of states.
    """

    V = {s: 0 for s in S}

    while True:
        oldV = V.copy()

        for s in S:
            a = policy[s]
            V[s] = R(s, a) + sum(P(s_next, s, a) * oldV[s_next] for s_next in S)

        if all(oldV[s] == V[s] for s in S):
            break

    return V



def PolicyImprovement(V, S, A):
    """
    V -> 
    S -> 
    A -> 
    """

    policy = {s: A[0] for s in S}

    for s in S:
        Q = {}
        for a in A:
            Q[a] = R(s, a) + sum(P(s_next, s, a) * V[s_next] for s_next in S)

        policy[s] = max(Q, key = Q.get)

    return policy
    