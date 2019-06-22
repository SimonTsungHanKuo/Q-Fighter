from gym.envs.registration import register

register(
    id='qfighter-v0',
    entry_point='gym_qfighter.envs:QFighterEnv',
)
register(
    id='qfighter-extrahard-v0',
    entry_point='gym_qfighter.envs:QFighterExtraHardEnv',
)
