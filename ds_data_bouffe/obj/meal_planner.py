import itertools
import numpy as np
import pandas as pd
import time


class MealPlanner:
    def __init__(self, df_meals, goals, n_days, tolerance=0.1):
        self.df_meals = df_meals
        self.goals = goals
        self.n_days = n_days
        self.tolerance = tolerance
        self.lst_all_meals = df_meals[list(goals.keys())].to_numpy() * 500  # 500g per meal
        # self.lst_all_meals = df_meals[list(goals.keys())].to_numpy() * 500  # 500g per meal

    @staticmethod
    def compute_loss(meal_plan, objective):
        return np.abs(meal_plan - objective).sum()

    @staticmethod
    def solve_naive(current_plan, all_meals, objective):
        n_meals = len(current_plan)
        all_meals_idx = list(range(len(all_meals)))

        for meal_plan_idx in itertools.combinations(all_meals_idx, n_meals):
            meal_plan = all_meals[list(meal_plan_idx)]
            yield meal_plan_idx, MealPlanner.compute_loss(meal_plan, objective)

    def solve_swap(self, current_plan, all_meals, objective, temperature=5, cooling_factor=0.001):
        n_meals = len(current_plan)
        best_loss = MealPlanner.compute_loss(all_meals[current_plan], objective)

        steps = 1
        while True:
            new_plan = current_plan.copy()
            new_meal = np.random.randint(0, len(all_meals) - 1)
            new_plan[steps % n_meals] = new_meal

            loss = self.compute_loss(all_meals[new_plan], objective)

            yield new_plan, loss

            if loss < best_loss:
                current_plan = new_plan
                best_loss = loss
            steps += 1

    def get_meal_plan(self, method="swap"):
        lst_all_meals = self.lst_all_meals
        lst_objective = np.array(list(self.goals.values())) * self.n_days

        lst_best_plan = list(range(len(lst_all_meals)))
        best_loss = self.compute_loss(lst_all_meals[lst_best_plan], lst_objective)

        if method == "swap":
            solve_method = self.solve_swap
        elif method == "naive":
            solve_method = self.solve_naive
        else:
            raise ValueError("Invalid method specified")

        start_time = time.time()
        steps = 0
        try:
            for plan_ids, loss in solve_method(lst_best_plan, lst_all_meals, lst_objective):
                steps += 1
                if steps % 10_000 == 0:
                    print(best_loss)
                if loss < best_loss:
                    best_loss = loss
                    best_plan = plan_ids

                    if loss < self.tolerance:
                        break
        except KeyboardInterrupt:
            pass

        plan_value = np.sum(lst_all_meals[best_plan], axis=0)

        meals = self.df_meals.iloc[best_plan][["name"] + list(self.goals.keys())]

        self.results[method] = {
            "meals": list(meals["name"]),
            "plan_value": plan_value,
            "loss": best_loss,
            "steps_taken": steps,
            "time_taken": time.time() - start_time
        }

    def compare_results_table(self):
        df_results = pd.DataFrame(self.results).T  # Transpose the DataFrame
        return df_results


if __name__ == "__main__":
    df_meals = pd.read_csv('database/ciqual.csv')
    default_daily_goals = {"kcal": 2000,
                           'protein': 50,
                           'glucid': 260,
                           'lipid': 70}

    meal_planner = MealPlanner(df_meals, default_daily_goals, 7)
    meal_planner.get_meal_plan(method="swap")
    meal_planner.get_meal_plan(method="naive")
    results_table = meal_planner.compare_results_table()

    print("Comparison Table:")
    print(results_table)

