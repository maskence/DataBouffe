<template>
    <aside class="bg-sidebar-color w-64 h-screen">
      <div class="p-4">
        <h2 class="text-maintextcolor text-xl font-semibold">DataBouffe</h2>
      </div>
      <nav>
        <ul>
          <li>
            <NuxtLink
              to="/meal_plan"
              class="sidebar-link"
              active-class="active-sidebar-link"
            >
              Meal Planner
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/meal-calendar"
              class="sidebar-link"
              active-class="active-sidebar-link"
            >
              Meal Calendar
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/nutritional-monitoring"
              class="sidebar-link"
              active-class="active-sidebar-link"
            >
              Nutritional Monitoring
            </NuxtLink>
          </li>
        </ul>
      </nav>
    </aside>
  </template>
  
  <style scoped>
  .bg-sidebar-color {
    background-color: var(--backgroundcolor);
  }
  
  .sidebar-link {
    display: block;
    padding: 1rem 2rem;
    color: var(--maintextcolor);
    background-color: var(--backgroundcolor);
    transition: background-color 0.2s, color 0.2s;
    text-decoration: none;
  }
  
  .sidebar-link:hover {
    color: var(--activecolor);
    background-color: var(--backgroundcolor);
  }
  
  .active-sidebar-link {
    color: white;
    background-color: var(--backgroundcolor);
  }
  
  /* Apply the button style to the links */
  .sidebar-link,
  .active-sidebar-link {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 9999px;
    transition: background-color 0.2s, color 0.2s;
    text-align: center;
  }
  
  .sidebar-link:hover,
  .active-sidebar-link:hover {
    color: white;
    background-color: var(--activecolor);
  }
  </style>
  