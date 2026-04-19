# Add a naming for block of values instead of naming each value manually <--

hws_cur = float(input("Input curret HotWater units value: "))
cws_cur = float(input("Input curret ColdWater units value: "))  # Current month values
kWh_cur = float(input("Input curret Electricity units value: "))

print()  # Add a naming for block of values instead of naming each value manually <--

hws_prev = float(input("Input previous HotWater units value: "))
cws_prev = float(
    input("Input previous ColdWater units value: ")
)  # Previos month values
kWh_prev = float(input("Input previous Electricity units value: "))

# Add ability to set additional value for another value of utility counter

hws_units_this_month = hws_cur - hws_prev
cws_units_this_month = cws_cur - cws_prev  # Used in this month
electricity_units_this_month = kWh_cur - kWh_prev

print(
    "\n\n",
    "Units used this month.",
    "\n\n",
    "HotWater units used this month:",
    hws_units_this_month,
    "\n",
    "ColdWater units used this mounth:",  # All consumed units by single metric
    cws_units_this_month,
    "\n",
    "Electricity units used this mounth:",
    electricity_units_this_month,
    "\n\n",
)

# Add a naming for block of values instead of naming each value manually <--

hws_per_unit = float(input("Input HotWater unit cost: "))
cws_per_unit = float(input("Input ColdWater unit cost: "))  # Cost of single unit
kWh_per_unit = float(input("Input Electricity unit cost: "))

hws_cost_this_month = hws_units_this_month * hws_per_unit
cws_cost_this_month = (
    cws_units_this_month * cws_per_unit
)  # Cost of all consumed units this month
kWh_cost_this_month = electricity_units_this_month * kWh_per_unit

total_cost = hws_cost_this_month + cws_cost_this_month + kWh_cost_this_month

print(
    "\n\n",
    "In total:",
    "\n\n",
    "Consumed HotWater:",
    hws_units_this_month,
    "Costs of consumed Hotwater:",
    hws_cost_this_month,
    "\n",
    "Consumed ColdWater:",
    cws_units_this_month,
    "Costs of consumed Coldwater:",  # Total. Consumed units and theirs cost
    cws_cost_this_month,
    "\n",
    "Consumed Electricity:",
    electricity_units_this_month,
    "Costs of consumed Howater:",
    kWh_cost_this_month,
    "\n\n" "Total cost of utilities this mounth:",
    total_cost,
    "\n\n",
)
