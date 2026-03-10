class SimulationService:

    def generate_scenarios(income, debt):

        scenarios = []

        scenarios.append({
            "title": "Increase Income by 20%",
            "income": income * 1.2,
            "debt": debt
        })

        scenarios.append({
            "title": "Reduce Debt by 30%",
            "income": income,
            "debt": debt * 0.7
        })

        scenarios.append({
            "title": "Worst Case Scenario",
            "income": income * 0.8,
            "debt": debt * 1.2
        })

        return scenarios