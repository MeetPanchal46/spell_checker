import time
import os
import sys
import matplotlib.pyplot as plt

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class DAAAlgorithmTracker:
    """Intercepts execution cycles to track runtimes, space costs, and complexity analysis."""
    def __init__(self, paradigm_name):
        self.paradigm_name = paradigm_name
        self.start_time = 0
        self.end_time = 0
        self.matrix_cells_computed = 0

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self, cells_computed=0):
        self.end_time = time.perf_counter()
        self.matrix_cells_computed = cells_computed

    def print_summary(self, input_word, corrections):
        elapsed_time = self.end_time - self.start_time
        print(f"\n=================== DAA TRACKER LOG ({self.paradigm_name}) ===================")
        print(f"➜ Input Token Checked: '{input_word}'")
        print(f"➜ DP State Matrix Size: {self.matrix_cells_computed:,} cells allocated")
        print(f"➜ Suggested Matches  : {corrections if corrections else 'None (Word Correct)'}")
        print(f"➜ Empirical Runtime  : {elapsed_time:.6f} seconds")
        print("========================================================================\n")


class SpellCheckerTracker:
    def __init__(self, dictionary_words):
        # Academic Dictionary configuration data structure
        self.dictionary = dictionary_words
        self.tracker = DAAAlgorithmTracker("Dynamic Programming - Edit Distance")

    def edit_distance(self, word1, word2):
        """
        Computes minimum operations using Dynamic Programming (Tabulation).
        DAA Complexity: O(M * N) space and time complexity.
        """
        m, n = len(word1), len(word2)
        
        # Bottom-Up Table Initialization: O(M * N) space overhead
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Cases tracking empty string transformations
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Tabulation Loop filled via optimal sub-structure properties
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # Deletion operation
                        dp[i][j - 1],    # Insertion operation
                        dp[i - 1][j - 1] # Substitution operation
                    )

        cells_processed = (m + 1) * (n + 1)
        return dp[m][n], cells_processed

    def check_and_suggest(self, query_word, max_suggestions=3, verbose=True):
        """Scans the master dictionary space evaluating edit bounds."""
        query_word = query_word.lower().strip()
        
        # Exact match structural bypass check
        if query_word in self.dictionary:
            if verbose:
                print(f"✨ '{query_word}' matches dictionary directly. No errors found.")
            return []

        self.tracker.start()
        
        suggestions = []
        total_cells_computed = 0

        # Loop through dictionary entries evaluating subproblem distances
        for dict_word in self.dictionary:
            distance, cells = self.edit_distance(query_word, dict_word)
            total_cells_computed += cells
            suggestions.append((dict_word, distance))

        # DAA Sorting / Greedy Selection phase: Order options by minimum modification cost
        suggestions.sort(key=lambda x: x[1])
        top_matches = [word for word, dist in suggestions[:max_suggestions]]

        self.tracker.stop(cells_computed=total_cells_computed)
        
        if verbose:
            self.tracker.print_summary(query_word, top_matches)
            
        return top_matches


# ==========================================
#   DEMO EXECUTION & EXPERIMENTAL SETUP
# ==========================================
if __name__ == "__main__":
    # 1. Instantiate a basic sample dictionary architecture
    sample_dictionary = [
        "algorithm", "analysis", "design", "dynamic", "programming", "greedy",
        "huffman", "compressor", "tracker", "project", "computer", "science",
        "sorting", "matrix", "graph", "complexity", "structure", "binary"
    ]
    
    checker = SpellCheckerTracker(sample_dictionary)

    print("⚡ [Phase 1] Executing Functional Spell Suggestion Test...")
    # Intentionally misspelled query token
    misspelled_input = "algoritm" 
    checker.check_and_suggest(misspelled_input, max_suggestions=3, verbose=True)

    # ----------------------------------------------------
    print("⚡ [Phase 2] Launching Empirical Scaling Benchmark...")
    
    # Scale test profiles: Emulating dictionary footprint growth spikes
    dictionary_sizes = [10, 50, 100, 200, 500]
    runtimes_ms = []

    # Generate mock dictionary scaling structures based on baseline keys
    for size in dictionary_sizes:
        scaled_dict = sample_dictionary * (size // len(sample_dictionary) + 1)
        scaled_dict = scaled_dict[:size]
        
        bench_checker = SpellCheckerTracker(scaled_dict)
        
        # Benchmark specific iteration loop metrics
        start = time.perf_counter()
        bench_checker.check_and_suggest("algoritm", max_suggestions=3, verbose=False)
        end = time.perf_counter()
        
        duration = (end - start) * 1000
        runtimes_ms.append(duration)
        print(f" ✔ Checked dictionary scale: {size} words inside {duration:.2f} ms")

    # ----------------------------------------------------
    # Generate and Export the Asymptotic Matrix Plot Graph
    plt.figure(figsize=(8, 5))
    plt.plot(dictionary_sizes, runtimes_ms, marker='s', color='#3498db', linewidth=2, label='Empirical Runtime')
    
    plt.title('DAA Project: Spell Checker Scaling vs Dictionary Size', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Dictionary Size (Number of Words)', fontsize=12)
    plt.ylabel('Execution Time (ms)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left')
    
    graph_filename = "spell_checker_curve.png"
    plt.savefig(graph_filename, dpi=300, bbox_inches='tight')
    print(f"\n📊 Performance curve graph successfully generated and saved as '{graph_filename}'!")
