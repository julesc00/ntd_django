
def planets_query():
    return """
{
  allPlanets {
    planets {
      name
      population
      terrains
      climates
    }
  }
}
"""


def climates_query():
    return """
{
  allPlanets {
    planets {
      climates
    }
  }
}
"""


def terrains_query():
    return """
{
  allPlanets {
    planets {
      terrains
    }
  }
}
"""