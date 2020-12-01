import numpy as np
from scipy.optimize import linprog
import math


# For Nitrogen, specially handle Urea and Vijetha to ignore one of them when prices of both are same
def nitrogen_fert_filter(fertilizer_name,N_qty_per_bag,fertilizer_bag_cost):
    urea_found = False;
    urea_index = vijetha_index = 0;
    vijetha_found = False;

    for i in range(len(fertilizer_name)):
        # Check if Urea and Vijetha exist together and if both have the same cost, remove Vijetha
        if fertilizer_name[i] == "Urea":
            urea_found = True;
            urea_index = i;
        if fertilizer_name[i] == "Vijetha":
            vijetha_found = True;
            vijetha_index = i;

    if (urea_found) and (vijetha_found):
        if(fertilizer_bag_cost[urea_found] == fertilizer_bag_cost[vijetha_found]):
            N_qty_per_bag[vijetha_index] = 0;

    return N_qty_per_bag


#Main optimization logic to derive the quantity of each fertilizer
def optimize_minimize(N_deficit,P_deficit,K_deficit,fertilizer_bag_required,fertilizer_bag_cost,fertilizer_name,N_qty_per_bag, P_qty_per_bag,K_qty_per_bag,fertilizer_bag_weight):
    # N_qty_per_bag = nitrogen_fert_filter(fertilizer_name,N_qty_per_bag,fertilizer_bag_cost);
    b  = [];

    for i in range(0,len(fertilizer_name)):
        individual_bound = [];

        # Defining lower boundary as 0
        individual_bound.append(0);

        # Boundary for N
        if N_qty_per_bag[i] == 0:
            n_bound = 0;
        else:
            n_bound = (N_deficit/N_qty_per_bag[i]);
        # Boundary for P
        if P_qty_per_bag[i] == 0:
            p_bound = 0;
        else:
            p_bound = (P_deficit/P_qty_per_bag[i]);
        # Boundary for K
        if K_qty_per_bag[i] == 0:
            k_bound = 0
        else:
            k_bound = (K_deficit/K_qty_per_bag[i]);

        # Defining Upper boundary
        individual_bound.append(n_bound + p_bound + k_bound);

        b.append(tuple(individual_bound));

    bnds = tuple(b);
    c = fertilizer_bag_cost;
    A_eq = [N_qty_per_bag, P_qty_per_bag, K_qty_per_bag]
    b_eq = [N_deficit, P_deficit, K_deficit]

    sol = linprog(c, A_ub=None, b_ub=None, A_eq=A_eq, b_eq=b_eq, bounds=bnds, method='simplex', callback=None, options=None)

    updated_x = sol.x.tolist()

    ceil_x = np.ceil(updated_x)

    fertilizer_kgs = np.array(fertilizer_bag_weight) * np.array(updated_x)

    optimized_output = {
    "optimized_N_qty": sum(x*y for x,y in zip(updated_x,N_qty_per_bag)),
    "optimized_P_qty": sum(x*y for x,y in zip(updated_x,P_qty_per_bag)),
    "optimized_K_qty": sum(x*y for x,y in zip(updated_x,K_qty_per_bag)),
    "total_cost": sum(x*y for x,y in zip(ceil_x,fertilizer_bag_cost)),
    "fertilizer_quantity_kg": [round(elem, 2) for elem in fertilizer_kgs.tolist()],
    # round(fertilizer_kgs.tolist(),2),
    "fertilizer_name": fertilizer_name,
    "fertilizer_bag_required": [round(elem, 2) for elem in updated_x],
    "fertilizer_bag_cost": fertilizer_bag_cost,
    "fertilizer_bag_weight": fertilizer_bag_weight
    }

    return optimized_output
