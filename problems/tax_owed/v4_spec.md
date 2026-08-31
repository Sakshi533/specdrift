Update: the frontend team needs more than a bare number. `tax(income)` must
now return a dict:

    {"tax": <int, same amount as before>,
     "effective_rate": <float, tax divided by income, rounded to 4 decimals>}

For `income == 0` the effective rate is `0.0`. All the bracket and deduction
rules stay exactly as they are.
