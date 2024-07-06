
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