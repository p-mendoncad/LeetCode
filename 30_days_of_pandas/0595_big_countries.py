import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[['name', 'population', 'area']]
    return world.query('area >= 3000000 | population >= 25000000')