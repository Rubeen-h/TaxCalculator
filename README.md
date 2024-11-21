# IRPF Tax Calculator

## Overview

This program calculates the **Income Tax (IRPF)** for individuals based on their income, age, disability percentage, and number of children. The tax is calculated using a set of progressive tax brackets, followed by several possible discounts that can reduce the final tax amount. 

### Tax Brackets

The income tax is calculated progressively, meaning that different portions of your income are taxed at different rates. Here’s how it works:

1. **First Portion**: The first **12,450€** of income is taxed at a rate of **19%**.
2. **Second Portion**: Any income above **12,450€** up to **20,200€** is taxed at a rate of **24%**.
3. **Third Portion**: Any income above **20,200€** up to **35,200€** is taxed at a rate of **30%**.
4. **Fourth Portion**: Any income above **35,200€** up to **60,000€** is taxed at a rate of **37%**.
5. **Fifth Portion**: Any income above **60,000€** is taxed at a rate of **45%**.

For example, if your income is **50,000€**, you would pay different rates for each portion of your income, calculated as follows:
- **19% on the first 12,450€**
- **24% on the income between 12,450€ and 20,200€**
- **30% on the income between 20,200€ and 35,200€**
- **37% on the income between 35,200€ and 50,000€**

### Discounts

Once the tax has been calculated using the tax brackets, several discounts are applied to reduce the total tax. These discounts are applied in a specific order and do not accumulate. Instead, each discount is applied one by one on the tax amount after the previous discount.

1. **Age Discount**:
   - If you are between **16 and 30 years old**, you receive a **15% discount** on your tax.
   - If you are **60 years or older**, you receive a **5% discount** on your tax.
   - If you are between **31 and 59 years old**, there is no age discount applied.

2. **Disability Discount**:
   - If you have a disability between **33% and 65%**, you receive a **10% discount** on your tax.
   - If you have a disability of **66% or more**, you receive a **15% discount** on your tax.
   - No discount is applied if the disability is below **33%**.

3. **Children Discount**:
   - For every child, you receive a **10% discount** on your tax.
   - The discount is capped at **100%** for 10 or more children. This means if you have 10 or more children, your entire tax will be reduced to **0**.
