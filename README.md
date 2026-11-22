# Grey–MRP: Material Requirements Planning with Discrete Grey Lead Times

This repository contains the Python implementations and Excel example workbooks accompanying the manuscript:

> **Selecting Planned Lead Times in Material Requirements Planning: A Discrete Grey Number Approach**

## Overview

Grey–MRP addresses multilevel material requirements planning when the possible replenishment lead times are known but their probabilities cannot be reliably estimated. A discrete grey number represents the feasible lead-time values without assigning probabilities to them. The **planned lead time** determines when an order is released; the **realised lead time** determines when it arrives. The framework compares release policies using the inventory holding and shortage costs associated with possible receipts.

The graphical interface provides two methods under **Grey POM → Grey MRP**:

| Menu option | Planned lead-time policy |
| --- | --- |
| **Grey MRP Simple Approach** (Algorithm 1) | Selects one planned lead time per item for the entire planning horizon. |
| **Grey MRP Complex Approach** (Algorithm 2) | Allows the planned lead time for each item to vary by period. |

The second approach explores a larger policy space and can take longer to run as the planning horizon grows.

## Repository Contents

| File | Description |
| --- | --- |
| `main_app.py` | Main graphical application. |
| `login_app.py` | Login interface module. |
| `grey_mrp_simple.py` | Implementation of Algorithm 1. |
| `grey_mrp_complex.py` | Implementation of Algorithm 2. |
| `discrete_grey_numbers.py`, `grey_comparison.py`, `grey_number_operation.py`, `analysis_classes.py` | Supporting modules for the application. |
| `example algorithm1.xlsx`, `example algirithm 2.xlsx` | Example workbooks for Algorithms 1 and 2, respectively. |
| `practical example.xlsx` | Additional worked example workbook. |

## Usage

1. Clone or download the repository. Install Python 3 and the dependencies required by the application. Keep the Python modules in their original folder structure.
2. From the directory containing `main_app.py`, open a terminal and launch the application:

   ```bash
   python main_app.py
   ```

3. In the left-hand menu, expand **Grey POM → Grey MRP** and select **Grey MRP Simple Approach** or **Grey MRP Complex Approach**.
4. Click **Browse** to select an example `.xlsx` workbook. To prepare your own data, click **Download template**, complete the workbook, and select it using **Browse**.
5. Click **Preview** to check the parsed planning periods, items, lead times, bill of materials, demand, and costs.
6. Click **Run** to execute the selected method. Use **Save Project** and **Load Project** to save or reopen a project. The input for a new Grey–MRP run is the Excel workbook; the JSON files are not a substitute for the workbook in the **Browse** field.

## Excel Input Format

Use the template supplied by the application and keep its sheet names and column headers unchanged.

| Worksheet | Contents |
| --- | --- |
| `Items` | One row per item: item name, lower and upper lead-time entries, lot quantity (`0` for lot-for-lot), safety stock, and initial inventory. |
| `BOM` | One row per parent–child relationship: `parent`, `child`, and `usage` (units of the child needed per unit of the parent). |
| `MPS & Costs` | One row per item: item name, holding cost, shortage cost (labelled `Slack cost` in the illustrated template), followed by one demand column per planning period. |

Use consistent item identifiers across all three sheets and express lead times in the same planning units as the demand columns.

**Lead-time input:** The illustrated template provides lower and upper lead-time columns. Check the values displayed by **Preview** before running the model. Bounds alone cannot distinguish a set such as `{1, 3}` from `{1, 2, 3}`. If an intermediate value cannot occur, do not assume that leaving it unspecified excludes it; check that the application has parsed exactly the feasible values.

## Manuscript Status

This repository provides supplementary code and example inputs for the manuscript *Selecting Planned Lead Times in Material Requirements Planning: A Discrete Grey Number Approach* by Tooraj Karimi.
