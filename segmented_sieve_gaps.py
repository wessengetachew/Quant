#!/usr/bin/env python3
"""
Segmented Sieve for Prime Gap Analysis
Allows processing primes up to 1 billion+ without memory issues
"""

import math
import time
from collections import defaultdict
from decimal import Decimal, getcontext

# Set high precision for product calculations
getcontext().prec = 50

def simple_sieve(limit):
    """Generate all primes up to limit using simple sieve (for small ranges)"""
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return [i for i in range(limit + 1) if is_prime[i]]

def segmented_sieve(limit, segment_size=1_000_000, callback=None):
    """
    Generate primes up to limit using segmented sieve.
    
    Args:
        limit: Upper bound for primes
        segment_size: Size of each segment (default 1M for good performance)
        callback: Optional function called with (prime, next_prime) for each prime
    
    Yields:
        prime numbers in order
    """
    # Generate small primes up to sqrt(limit) for sieving
    sqrt_limit = int(math.sqrt(limit)) + 1
    small_primes = simple_sieve(sqrt_limit)
    
    # Process segments
    low = 0
    high = segment_size
    
    # Track the last prime for gap calculation
    last_prime = None
    
    while low <= limit:
        if high > limit:
            high = limit
        
        # Create segment
        segment = [True] * (high - low + 1)
        
        # Mark composites in this segment
        for p in small_primes:
            # Find first multiple of p in [low, high]
            start = max(p * p, ((low + p - 1) // p) * p)
            
            for j in range(start, high + 1, p):
                segment[j - low] = False
        
        # Collect primes from this segment
        for i in range(len(segment)):
            if segment[i] and (low + i >= 2):
                current_prime = low + i
                
                if callback and last_prime is not None:
                    callback(last_prime, current_prime)
                
                last_prime = current_prime
                yield current_prime
        
        # Move to next segment
        low = high + 1
        high = low + segment_size
    
    # Handle the final prime (it has no next prime in our range)
    if callback and last_prime is not None:
        callback(last_prime, None)

class GapAnalyzer:
    """Analyzes prime gaps and computes contributions to Euler product"""
    
    def __init__(self):
        self.gap_data = defaultdict(lambda: {
            'count': 0,
            'product': Decimal(1),
            'log_product': Decimal(0),
            'primes': []
        })
        self.total_primes = 0
        self.last_prime = None
    
    def process_prime(self, prime, next_prime):
        """Process a prime and its gap"""
        self.total_primes += 1
        
        # If this is the last prime (next_prime is None), skip gap calculation
        if next_prime is None:
            return
        
        gap = next_prime - prime
        
        # Calculate contribution: p^2 / (p^2 - 1)
        p_squared = Decimal(prime) * Decimal(prime)
        contribution = p_squared / (p_squared - Decimal(1))
        
        # Update gap family data
        self.gap_data[gap]['count'] += 1
        self.gap_data[gap]['product'] *= contribution
        self.gap_data[gap]['log_product'] += contribution.ln()
        
        # Store first 20 primes for each gap family
        if len(self.gap_data[gap]['primes']) < 20:
            self.gap_data[gap]['primes'].append(prime)
    
    def get_results(self):
        """Return sorted gap data"""
        return sorted(self.gap_data.items())
    
    def save_to_csv(self, filename, max_prime):
        """Save results in the same format as the input file"""
        from datetime import datetime
        
        with open(filename, 'w') as f:
            f.write("=================================================\n")
            f.write("GAP-CLASS DECOMPOSITION OF ZETA(2) = PI^2/6\n")
            f.write("Individual Gap Family Products\n")
            f.write("=================================================\n\n")
            
            f.write("ABSTRACT:\n")
            f.write("This dataset contains the individual product values P_g for each gap family.\n")
            f.write("Each P_g represents the contribution of all primes with forward gap g to the\n")
            f.write("overall Euler product. The data includes prime counts, product values, logarithmic\n")
            f.write("contributions, and the first primes in each family for verification and further analysis.\n\n")
            
            f.write("FORMULA:\n")
            f.write("P_g = product over all primes p where gap(p)=g of [p^2 / (p^2 - 1)]\n")
            f.write("where gap(p) = next_prime(p) - p\n\n")
            
            timestamp = datetime.now().isoformat()
            f.write(f"Analysis Date:,{timestamp}\n")
            f.write(f"Maximum Prime:,{max_prime}\n")
            f.write(f"Total Primes:,{self.total_primes}\n")
            f.write(f"Total Gap Families:,{len(self.gap_data)}\n\n")
            
            f.write("DATA TABLE:\n")
            f.write("Gap,Product P_g,Log(P_g),Prime Count,Percentage of Total,First 20 Primes in Family\n")
            
            for gap, data in self.get_results():
                product = float(data['product'])
                log_product = float(data['log_product'])
                count = data['count']
                percentage = (count / self.total_primes * 100) if self.total_primes > 0 else 0
                primes_str = " ".join(str(p) for p in data['primes'])
                
                f.write(f'{gap},{product:.10f},{log_product:.10f},{count},{percentage:.4f}%,"{primes_str}"\n')
            
            f.write("\n=================================================\n")
            f.write("END OF DATASET\n")
            f.write("=================================================\n")

def main():
    """Main function with examples of different scales"""
    
    print("Segmented Sieve Prime Gap Analyzer")
    print("=" * 60)
    
    # Ask user for the limit
    print("\nExample limits:")
    print("  100,000,000 (100 million) - ~5.7M primes, ~30 seconds")
    print("  1,000,000,000 (1 billion) - ~50.8M primes, ~5 minutes")
    print("  10,000,000,000 (10 billion) - ~455M primes, ~50 minutes")
    
    limit_input = input("\nEnter maximum prime to analyze (or press Enter for 100M): ").strip()
    
    if not limit_input:
        limit = 100_000_000
    else:
        # Parse input handling underscores and commas
        limit_input = limit_input.replace(",", "").replace("_", "")
        limit = int(limit_input)
    
    print(f"\nAnalyzing primes up to {limit:,}")
    print(f"Using segmented sieve with 1M segments")
    print("-" * 60)
    
    # Create analyzer
    analyzer = GapAnalyzer()
    
    # Track progress
    start_time = time.time()
    checkpoint = limit // 10  # Report every 10%
    next_checkpoint = checkpoint
    
    def progress_callback(prime, next_prime):
        nonlocal next_checkpoint
        analyzer.process_prime(prime, next_prime)
        
        if prime >= next_checkpoint:
            elapsed = time.time() - start_time
            percent = (prime / limit) * 100
            rate = prime / elapsed if elapsed > 0 else 0
            print(f"Progress: {percent:5.1f}% ({prime:,}) - "
                  f"{analyzer.total_primes:,} primes - "
                  f"{rate:,.0f} numbers/sec")
            next_checkpoint += checkpoint
    
    # Run the segmented sieve
    for prime in segmented_sieve(limit, segment_size=1_000_000, callback=progress_callback):
        pass  # Processing happens in callback
    
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 60)
    print(f"Analysis complete!")
    print(f"Time taken: {elapsed:.2f} seconds")
    print(f"Total primes found: {analyzer.total_primes:,}")
    print(f"Gap families: {len(analyzer.gap_data)}")
    print(f"Processing rate: {limit / elapsed:,.0f} numbers/second")
    
    # Save results
    output_file = f"/mnt/user-data/outputs/gap_contributions_{limit}.csv"
    analyzer.save_to_csv(output_file, limit)
    print(f"\nResults saved to: {output_file}")
    
    # Show top gap families
    print("\nTop 10 gap families by count:")
    print("-" * 60)
    results = analyzer.get_results()
    for gap, data in sorted(results, key=lambda x: x[1]['count'], reverse=True)[:10]:
        count = data['count']
        percent = (count / analyzer.total_primes) * 100
        print(f"Gap {gap:3d}: {count:10,} primes ({percent:5.2f}%)")

if __name__ == "__main__":
    main()
