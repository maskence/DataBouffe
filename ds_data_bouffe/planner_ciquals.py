from ds_data_bouffe.obj.meal_planner import MealPlanner


class PlannerCiquals(MealPlanner):

    def __init__(self, df_meals, goals, n_days, tolerance=0.1):
        self.df_meals = df_meals
        self.goals = goals
        self.n_days = n_days
        self.tolerance = tolerance
        self.all_meals = df_meals[list(goals.keys())].to_numpy() * 500  # 500g per meal
