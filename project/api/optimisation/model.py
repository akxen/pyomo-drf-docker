"""Construct, solve, and extract results from a Pyomo model"""

import pyomo.environ as pyo

# Required if running within web app
# See: https://github.com/PyUtilib/pyutilib/issues/31#issuecomment-382479024
import pyutilib.subprocess.GlobalData
pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False


def construct_model(data):
    """
    Create concrete model with user data

    Parameters
    ----------
    data : dict
        Model parameters specified by user

    Returns
    -------
    m : Pyomo model
        Concrete model populated with user specified data
    """

    # Initialise model
    m = pyo.ConcreteModel()

    # Define parameters using input data
    m.PARAMETER_1 = pyo.Param(initialize=data['PARAMETER_1'])
    m.PARAMETER_2 = pyo.Param(initialize=data['PARAMETER_2'])
    m.PARAMETER_3 = pyo.Param(initialize=data['PARAMETER_3'])

    # Define variables
    m.x = pyo.Var(within=pyo.NonNegativeReals)
    m.y = pyo.Var(within=pyo.NonNegativeReals)

    # Define constraints
    m.CONSTRAINT_1 = pyo.Constraint(expr=m.x >= m.PARAMETER_1)
    m.CONSTRAINT_2 = pyo.Constraint(expr=m.x + (m.PARAMETER_2 * m.y)
                                    >= m.PARAMETER_3)

    # Define objective
    m.OBJECTIVE = pyo.Objective(expr=m.x + m.y, sense=pyo.minimize)

    return m


def solve_model(m):
    """
    Solve model - results attached to model instance

    Parameters
    ----------
    m : Pyomo model instance
        Model instance containing user defined data

    Returns
    -------
    m : Pyomo model instance
        Solved model instance
    """

    opt = pyo.SolverFactory('glpk')
    opt.solve(m)

    return m


def get_results(m):
    """
    Extract model results as dict


    Parameters
    ----------
    m : Pyomo model instance
        Model instance containing solution (post-solve)

    Returns
    -------
    results : dict
        Dictionary containing model results
    """

    results = {
        "x": m.x.value,
        "y": m.y.value
    }

    return results


def run_model(data):
    """
    Construct model, solve model, and extract results

    Parameters
    ----------
    data : dict
        User defined parameters for model instance

    Returns
    -------
    results : dict
        Model results    
    """

    m = construct_model(data=data)
    m = solve_model(m=m)
    results = get_results(m=m)

    return results
