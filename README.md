 Gap-Class Decomposition Explorer v2.0

Live at https://wessengetachew.github.io/Quant/

By Wessen Getachew


## What This Is

This is an interactive research tool built around a single question: can the value of the Riemann zeta function at s=2, which equals pi squared over 6, be recovered by partitioning primes into families based on the gap to the next prime and multiplying their individual Euler-product contributions together?

The answer is yes, and this tool lets you watch it happen in real time.

The core identity is that zeta(2) equals the product over all even gap sizes g of the partial Euler product formed by primes whose gap to the next prime equals g. Each gap family contributes one multiplicative factor, and those factors multiply together to pi squared over 6 as more primes are included.

This framework is called the gap-class decomposition. It connects three major areas of analytic number theory: the Euler product formula for zeta functions, the Hardy-Littlewood prime pair conjectures, and the Riemann Hypothesis through its equivalence to bounds on the Mertens function.


## How to Use It

Set a prime range using the input field at the top and press Run Analysis. The tool runs a segmented sieve to find all primes up to your chosen limit, groups them into gap families, and computes every product, ratio, and prediction shown across the page.

The browser handles up to around 300 million reliably. For larger ranges use the Python script described at the bottom of this file.

Every chart updates immediately after analysis completes. All sections are collapsible. Data tables are sortable and filterable. Charts can be exported as 4K PNG files and most data sections can be exported as CSV.


## The Charts

Progressive Convergence to zeta(2)

Shows the cumulative product as gap families are added one by one. The line climbs toward pi squared over 6 from below, with the convergence error shrinking as each new family is included. This is the central visual of the decomposition.

Individual Gap Family Products

Each gap g has a partial Euler product P(g) formed only by primes whose gap to the next prime equals g. This chart shows those individual values. Larger gaps tend to produce smaller products, but the relationship is not monotone because the Hardy-Littlewood singular series S(h) varies with the prime factorisation of h.

Prime Distribution by Gap Class

How many primes fall into each gap family. Gap 2 and gap 4 are roughly equal in count at any finite range, converging toward equal asymptotic density as predicted by Hardy-Littlewood. Gap 6 is approximately twice as frequent because its singular series constant is double that of gap 2.

Percentage Contribution to zeta(2)

Each family's share of the total log of pi squared over 6. Gap 1, containing only the prime 2, and gap 2, containing twin primes, dominate the early contributions. The chart shows how weight is distributed across gap sizes as the prime range grows.

Convergence Error Analysis

Tracks how far the running product is from the target pi squared over 6 at each step. The error decays as more gap families are included.

Log-Scale Product Growth

The same product data shown in log space, making additive contributions to log(zeta(2)) easier to compare across families spanning many orders of magnitude.

Gap Ratio Analysis and Twin Prime Conjecture Evidence

Three subcharts. The first shows the ratio Count(gap=2)/Count(gap=4), which converges to 1.0 as the range increases because both families have identical Hardy-Littlewood singular series constants. The second shows the percentage of all primes falling into each small gap family. The third compares the observed twin prime count against the Hardy-Littlewood prediction using the li2 integral with four correction terms. At 400 million this prediction is accurate to within 0.06 percent.

Hardy-Littlewood Conjecture B: Step-by-Step Calculations for Every Gap Family

The most detailed section on the page. Seven parts, each self-contained.

Part 1 states the full Hardy-Littlewood formula. The count of prime pairs (p, p+h) up to x is asymptotically S(h) times li2(x), where S(h) is the singular series and li2(x) is the logarithmic integral of 1/ln^2(t).

Part 2 derives the twin prime constant C2 = 0.6601618158468695 as an infinite Euler product over all primes p at least 3 of the factor p(p-2)/(p-1)^2. A table shows partial products through the first 20 primes. The product converges from above, meaning early partial products exceed the final value before settling down toward it.

Part 3 shows the singular series S(h) for the first 30 even gaps. For each gap the table shows the prime factorisation of h, which odd primes divide it, each correction factor (p-1)/(p-2), their product, and S(h). Gap 6 gets a correction of 2/1 from p=3 giving S(6) = 4*C2, exactly twice S(2). Gap 30 gets corrections 2/1 from p=3 and 4/3 from p=5 giving S(30) = 16*C2/3. Only odd prime factors of h contribute corrections. Even prime factor p=2 is already absorbed into the baseline C2.

Part 4 expands the li2 integral term by term. The asymptotic expansion is x/ln^2(x) times the sum of (k+1)!/ln^k(x) for k starting at 0, giving coefficients 1, 2, 6, 24, 120, 720. At 400 million the one-term approximation x/ln^2(x) is 10.7 percent off. Two terms brings the error to 1.7 percent. Three terms gives 0.33 percent. Four terms gives 0.06 percent. The expansion is asymptotic rather than convergent and eventually diverges for any fixed x, but the first four terms are accurate for ranges above 10 million.

Part 5 is a full gap-by-gap table that populates automatically after you run analysis. For every gap in your data it shows the odd prime factors, S(h), the Hardy-Littlewood prediction, your observed count, the ratio of observed to predicted, and a convergence bar showing how close the ratio is to 1.0.

Part 6 is an interactive arithmetic walkthrough. Choose any even gap and any x value. The tool walks through every step: factoring h, identifying its odd prime divisors, computing each (p-1)/(p-2) factor, building S(h), expanding li2(x) term by term showing the value and percentage contribution of each correction, multiplying to get the final prediction, and comparing against your observed count if analysis has been run. Presets for gaps 2, 4, 6, 10, 12, 30, and 210 are provided.

Part 7 shows how count ratios are converging to their theoretical limits derived from the singular series. Count(gap=2)/Count(gap=4) converges to 1.0. Count(gap=6)/Count(gap=2) converges to 2.0. Count(gap=10)/Count(gap=2) converges to 4/3. The table shows the current value from your data, the limit, and the percentage of the way there.

Custom Gap Family Comparison

Choose any combination of gap families to compare side by side. Presets include twins vs cousins, small gaps, multiples of 6, gaps near multiples of 6, and powers of 2.

Step-by-Step Gap Accumulation

A numerical table showing the running product as each gap family is added, with exact values at every step.

Gap Contribution Evolution Across zeta(s)

How the relative contribution of each gap family changes as the exponent s in zeta(s) varies. At s=2 twin primes and gap-1 dominate. The balance shifts at other values of s.

Decimal Place Convergence Analysis

Tracks which primes stabilise each decimal place of the product. Shows the weight each prime carries and the marginal contribution as the product settles toward its final value.

Mertens Function and Riemann Hypothesis Connection

A companion analysis section. The Mertens function M(n) is the cumulative sum of the Mobius function mu(k) from k=1 to n. It forms an integer-valued random walk through positive and negative territory. The Riemann Hypothesis is equivalent to the statement that M(n) stays within the boundary plus or minus sqrt(n) for all n. This is the same hypothesis governing the accuracy of the Hardy-Littlewood predictions in the gap decomposition above. Both analyses are measuring the same underlying property of the prime distribution.

The section includes an animated chart of M(n) with the sqrt(n) boundary curves, a full data table of mu(n), M(n), the change delta M, square-free status, distinct prime factor count, absolute value of M(n), and boundary compliance for every n in the chosen range. Animation plays forward or backward. The range can be set to any value up to 100,000 via manual input. CSV export is available.


## The Mathematical Connection

The gap decomposition and the Mertens function approach the same question from different directions. The Riemann Hypothesis states that all non-trivial zeros of the zeta function lie on the line with real part one half. This is equivalent to the Mertens function staying within its sqrt(n) envelope, and also to the Hardy-Littlewood gap predictions being accurate to within a specific error bound. The tight convergence visible in the gap product charts and the containment of M(n) within its boundary are two forms of the same numerical evidence.


## Browser Performance

The segmented sieve keeps memory constant at around 50 megabytes during prime generation regardless of the range. After generation the browser must store all primes simultaneously for analysis. Practical limits are roughly 200 million comfortably, 300 million reliably on most systems, and 400 million on occasion depending on available RAM and how many browser tabs are open. The browser will freeze attempting 1 billion. For ranges above 300 million use the Python script.


## Python Script for Large Ranges

The repository includes segmented_sieve_gaps.py. It runs the same analysis using Python's generator-based incremental processing, which means it never holds all primes in memory at once. Memory stays at around 50 megabytes regardless of range. Expected times are roughly 120 seconds at 400 million and 300 seconds at 1 billion. Output is a CSV file that can be uploaded to the tool for visualisation.

Run it with:

    python3 segmented_sieve_gaps.py

Then enter the desired upper limit when prompted.


## Exports

Every chart has a 4K PNG export. Most data sections have a CSV export containing a full header, the theoretical foundation in plain text, all computed values, and an interpretation section. The gap ratio CSV includes singular series values for each gap and conclusions about convergence. The Mertens section exports mu(n), M(n), delta M, square-free status, prime factor count, absolute value of M(n), boundary compliance, and status for every row in the current range.


## Attribution

Built by Wessen Getachew, Independent Mathematical Researcher.
Twitter: @7dview

If you use this tool or its findings in academic work, presentations, or publications, please provide attribution to Wessen Getachew and cite the gap-class decomposition framework.

Gap-Class Decomposition Explorer v2.0, February 2026.
