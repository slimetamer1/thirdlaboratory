import concurrent.futures
import time

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_payroll(employee):
    name, salary = employee
    
    sss_rate = 0.045        # 4.5%
    philhealth_rate = 0.025 # 2.5%
    pagibig_rate = 0.02     # 2%
    tax_rate = 0.10         # 10%
    
    d_sss = salary * sss_rate
    d_philhealth = salary * philhealth_rate
    d_pagibig = salary * pagibig_rate
    d_tax = salary * tax_rate
    
    total_deduction = d_sss + d_philhealth + d_pagibig + d_tax
    net_salary = salary - total_deduction
    
    return {
        "name": name,
        "gross": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }


if __name__ == '__main__':
    print("Starting Payroll Calculation using Data Parallelism (ProcessPoolExecutor)...\n")
    
    start_time = time.perf_counter()

    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        results = executor.map(compute_payroll, employees)

         
        print(f"{'Employee':<10} | {'Gross Salary':<15} | {'Total Deduction':<15} | {'Net Salary':<15}")
        print("-" * 65)
        
        for r in results:
            print(f"{r['name']:<10} | {r['gross']:<15,.2f} | {r['total_deduction']:<15,.2f} | {r['net_salary']:<15,.2f}")

    end_time = time.perf_counter()
    print(f"\nExecution finished in {end_time - start_time:.4f} seconds.")