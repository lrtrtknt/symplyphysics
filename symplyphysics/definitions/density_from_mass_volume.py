from sympy import Expr
from symplyphysics import (
    Eq, pretty, solve, units, expr_to_quantity
)
from symplyphysics.core.quantity_decorator import validate_input_symbols, validate_output_symbol
from symplyphysics.core.symbols.quantities import Quantity
from symplyphysics.core.symbols.symbols import Symbol, to_printable

# Description
## The density (more precisely, the volumetric mass density), of a substance
## is its mass per unit volume.

# Definition: ρ = m / V
# Where:
## m is the mass
## V is volume
## ρ is the density

mass = Symbol("mass", units.mass)
volume = Symbol("volume", units.volume)
density = Symbol("density", units.mass / units.volume)

definition = Eq(density, mass / volume)

definition_units_SI = units.kilogram / units.meter**3

def print(expr: Expr) -> str:
    symbols = [mass, volume, density]
    return pretty(to_printable(expr, symbols), use_unicode=False)

@validate_input_symbols(mass_=mass, volume_=volume)
@validate_output_symbol(density)
def calculate_density(mass_: Quantity, volume_: Quantity) -> Quantity:
    solved = solve(definition, density, dict=True)[0][density]
    result_expr = solved.subs({mass: mass_, volume: volume_})
    return expr_to_quantity(result_expr)