# DecisionRulesPy

VERSION 3 CONTAINS MAJOR CHANGES IN API INTERFACES AND NOW SUPPORTS RULEFLOWS CRUD

A simple library that allows you to easily connect to 
[DecisionRules.io](https://decisionrules.io) from your application.

# Usage

* Solver (DecisionTables, ScriptRules, RuleFlow)
* Management API (CRUD operations on DecisionTables and RuleFlows)

# 1 - Solver

Solver is designed for solving rules made in DecisionRules application.

## 1.1 - Defining solver init

Before you start solving rules you need to setup an SolverAPI instance. How to do so is shown below.

```python
import decisionrules

def solver_test():
    solver = decisionrules.SolverAPI(solver_api_key)
```

## 1.2 - Defining solver method with data

Solver method expects 5 arguments

* SolverType - enum value - mandatory
* RuleId - str - mandatory
* Data - dict or json str - mandatory
* SolverStrategy - enum value - mandatory
* Version - str - optional

```python
def solver_test():
    data = {"say": "Hello from python"}

    solver = decisionrules.SolverAPI(api_key)

    # SolverType enum defines type of solver (Rule or Compostion)
    response = solver.solve(decisionrules.SolverType.RULE, get_rule, data, decisionrules.SolverStrategies.STANDARD)

    response2 = solver.solve(decisionrules.SolverType.RULEFLOW, compo_rule, data, decisionrules.SolverStrategies.STANDARD)
```

## 1.3 Solver with custom domain

For using custom domain just add `CustomDomain` instance to the `init method` with `url` and `protocol` parameters.

```python
def solver_test():
    data = {"say": "Hello from python"}

    solver = decisionrules.SolverAPI(api_key, decisionrules.CustomDomain("YOUR_URL", decisionrules.Protocols.HTTPS))
    
    response = solver.solve(decisionrules.SolverType.RULE, get_rule, data, decisionrules.SolverStrategies.STANDARD)

    response2 = solver.solve(decisionrules.SolverType.RULEFLOW, compo_rule, data, decisionrules.SolverStrategies.STANDARD)
```

# 2 - Management API

Management api is accessible via `ManagementApi` and required management api key that you can obtain in api key section in DecisionRules app.


Data for ruleflow import methods are represented as an array where index0 = RF, and index1...indexn are DTs

```python
def management_api_test():
    manager = decisionrules.ManagementApi(mng_key)

    #Or with custom domain

    manager = decisionrules.ManagementApi(mng_key, decisionrules.CustomDomain("YOUR_URL", decisionrules.Protocols.HTTPS))
```

## 2.1 Management API usage example

```python
def management_api_test():
    manager = decisionrules.ManagementApi(mng_key)

    manager.get_rule(get_rule)
    manager.get_rule(get_rule, "1")
    manager.get_space(get_space)

    manager.update_rule(put_rule, "1", put_data)
    manager.create_rule(post_rule, post_data)
    manager.delete_rule(delete_rule, "1")

    manager.create_ruleflow(new_ruleflow)
    manager.get_ruleflow(id)
    manager.get_ruleflow(id, 1)
    manager.update_ruleflow(id, 1, ruleflow)
    manager.export_ruleflow(id, 1)
    manager.export_ruleflow(id)
    manager.import_ruleflow([new_ruleflow_with_dt], 1,)
    manager.import_ruleflow(id, 1, [new_ruleflow_with_dt])
    manager.import_ruleflow([new_ruleflow_with_dt])
    manager.delele_ruleflow(id)
```

## 2.3 All available methods in management API

* GetRuleById - Search for single rule by its ID
* GetRuleByIdAndVersion - Search for single rule by its ID and version
* GetSpace - Search for space by its ID
* PostRuleForSpace - Post new rule to the space
* PutRule - Update existing rule
* DeleteRule - Delete existing rule
* Create Ruleflow - Creates empty rule flow
* Get Ruleflow - Returns RuleFlow
* Update RuleFlow - Updates RuleFlow
* Import RuleFlow - Imports RuleFlow (as a new RuleFLow, as a new version or replace existing version) and all RelatedDecisionTables (see chapter 2 on how to compose requests)
* Export RuleFlow - Exports RuleFlow and related DecisionTables
* Delete RuleFlow - Deletes existing RuleFlow
