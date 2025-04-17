from collections import namedtuple
from enum import Enum
from enum import IntEnum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

# Define condition with numeric values as described in the assignment
class Condition(IntEnum):
    CURE = 0
    HEALTHY = 1
    SICK = 2
    DYING = 3
    DEAD = 4

def improve(agent: Agent) -> Agent:
    """
    Model the outcome of an agent improving its condition.
    """
    # SICK or DYING agents can improve by 1 step
    if agent.category in (Condition.SICK, Condition.DYING):
        return Agent(agent.name, Condition(agent.category - 1))
    # Other agents remain unchanged
    return agent

def worsen(agent: Agent) -> Agent:
    """
    Model the outcome of an agent worsening its condition.
    """
    # SICK or DYING agents can get worse by 1 step
    if agent.category in (Condition.SICK, Condition.DYING):
        return Agent(agent.name, Condition(agent.category + 1))
    # Other agents remain unchanged
    return agent

def meeting(pair: tuple[Agent, Agent]) -> tuple[Agent, Agent]:
    """
    Model the outcome of a meeting between two agents.

    - CURE improves SICK or DYING, to either HEALTHY or SICK in accordance.
    - SICK and dying agents worsen SICK or DYING to the next infection state.
    - Otherwise, no change.
    """
    a1, a2 = pair

    # CURE improves SICK or DYING by 1 step
    if a1.category == Condition.CURE and a2.category in (Condition.SICK, Condition.DYING):
        return a1, improve(a2)

    if a1.category in (Condition.SICK, Condition.DYING) and a2.category == Condition.CURE:
        return improve(a1), a2

    # DYING or SICK worsen SICK or DYING by 1 step
    if a1.category in (Condition.SICK, Condition.DYING)and a2.category in (Condition.SICK, Condition.DYING):
        return worsen(a1), worsen(a2)

    # Otherwise, no change
    return a1, a2

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    # Filter out inactive agents (healthy or dead)
    active_agents = [a for a in agent_listing if a.category not in (Condition.DEAD, Condition.HEALTHY)]
    # Keep inactive agents (healthy or dead) as they are
    inactive_agents = [a for a in agent_listing if a.category in (Condition.HEALTHY, Condition.DEAD)]   

    result = []
    for i in range(0, len(active_agents), 2):
        # Pair active agents for meetings by consecutive indexes
        pair = active_agents[i:i + 2]
        # If there are two agents in the pair, apply the meeting rules
        if len(pair) == 2:
            result.extend(meeting(pair))
        else:
            # is there is uneven number of agents, return the last agent as-is
            result.append(pair[0])
    # Return updated infection status and inactive agents
    return result + inactive_agents