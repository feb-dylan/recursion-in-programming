import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Recursive Functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a

def generate_golden_spiral(n_terms):
    fib_sequence = [fibonacci(i) for i in range(1, n_terms + 1)]
    return fib_sequence


def plot_golden_spiral(fib_sequence):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    x, y = 0, 0
    direction = 0  # 0=right, 1=up, 2=left, 3=down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Track coordinates for dynamic plot limits
    x_coords, y_coords = [0], [0]
    
    for i, term in enumerate(fib_sequence):
        dx, dy = directions[direction % 4]
        
        # Draw the square and arc
        rect = plt.Rectangle((x, y), dx*term, dy*term, 
                            edgecolor='purple', facecolor='none', linestyle='--', alpha=0.5)
        ax.add_patch(rect)
        
        # Draw the golden spiral arc
        theta = np.linspace(direction * 90, (direction + 1) * 90, 100)
        radius = term
        x_arc = x + radius * np.cos(np.radians(theta))
        y_arc = y + radius * np.sin(np.radians(theta))
        ax.plot(x_arc, y_arc, color='gold', linewidth=2)
        
        # Update coordinates
        x += dx * term
        y += dy * term
        direction += 1
        
        x_coords.extend([x, x + dx * term])
        y_coords.extend([y, y + dy * term])
    
    # Set dynamic plot limits
    ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
    ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)
    
    return fig
    
# Recursive Guessing Game
def guessing_game(number, guess):
    if guess == number:
        return "🎉 Correct! You found the number!"
    elif guess > number:
        return "📉 Too high! Try again."
    else:
        return "📈 Too low! Try again."

# Tree Fractal Visualization
def draw_tree(ax, x, y, angle, depth):
    if depth == 0:
        return
    x2 = x + np.cos(np.radians(angle)) * depth * 5
    y2 = y + np.sin(np.radians(angle)) * depth * 5
    ax.plot([x, x2], [y, y2], 'g', linewidth=depth / 2)
    draw_tree(ax, x2, y2, angle - 20, depth - 1)
    draw_tree(ax, x2, y2, angle + 20, depth - 1)

# Recursive Puzzle Challenge
def recursive_puzzle(n):
    if n == 1:
        return "🎉 Congratulations! You've solved the recursion challenge!"
    return f"🔄 Solve this recursive step first: {n-1}"

# Recursive Sequence Visualization (Fibonacci)
def fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]

def fibonacci_spiral(n):
    return [fibonacci(i) for i in range(1, n+1)]  # Start from term 1, not 0

# Recursive Divide and Conquer (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursive call for both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Recursive Permutations
def permutations(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        first = [arr[i]]
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append(first + p)
    return result

# Streamlit UI
st.title("Recursion Explorer 🌀")
st.sidebar.header("Select a Mode")
option = st.sidebar.radio("Choose:", [
    "Explanation Page", "Factorial", "Power", "Prime Check", "Guessing Game", 
    "Tree Fractal", "Recursive Puzzle Challenge", "Fibonacci Visualization", 
    "Merge Sort", "Permutations"
])

if option == "Factorial":
    num = st.number_input("Enter a number:", min_value=0, step=1)
    if st.button("Calculate Factorial"):
        result = factorial(int(num))
        st.success(f"Factorial of {int(num)} is {result}")
        
        # Visualize factorial growth
        steps = [factorial(i) for i in range(1, int(num) + 1)]
        fig, ax = plt.subplots()
        ax.bar(range(1, int(num) + 1), steps)
        ax.set_xlabel("Steps")
        ax.set_ylabel("Factorial Value")
        ax.set_title(f"Factorial Growth for {int(num)}")
        st.pyplot(fig)
        plt.close()  # Close the figure to free memory


elif option == "Explanation Page":
    st.title("📚 Recursion Explorer - Explanation Page")
    st.write("""
    Welcome to **Recursion Explorer**! This app demonstrates various recursive algorithms and visualizations. 
    Below is a detailed explanation of each mode:
    """)
    
    st.markdown("---")
    
    # Factorial Explanation
    st.header("🔢 Factorial")
    st.write("""
    The **Factorial** mode calculates the factorial of a number using recursion. 
    - **Formula**: `n! = n * (n-1)!`
    - **Example**: `5! = 5 * 4 * 3 * 2 * 1 = 120`
    """)
    st.code("""
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    """, language="python")
    
    st.markdown("---")
    
    # Power Explanation
    st.header("⚡ Power")
    st.write("""
    The **Power** mode calculates the power of a number using recursion.
    - **Formula**: `base^exp = base * base^(exp-1)`
    - **Example**: `2^3 = 2 * 2 * 2 = 8`
    """)
    st.code("""
    def power(base, exp):
        if exp == 0:
            return 1
        return base * power(base, exp - 1)
    """, language="python")
    
    st.markdown("---")
    
    # Prime Check Explanation
    st.header("🔍 Prime Check")
    st.write("""
    The **Prime Check** mode determines if a number is prime using recursion.
    - **Logic**: A number is prime if it has no divisors other than 1 and itself.
    - **Example**: `7` is prime, but `9` is not.
    """)
    st.code("""
    def is_prime(n, divisor=None):
        if n < 2:
            return False
        if divisor is None:
            divisor = n - 1
        if divisor == 1:
            return True
        if n % divisor == 0:
            return False
        return is_prime(n, divisor - 1)
    """, language="python")
    
    st.markdown("---")
    
    # Guessing Game Explanation
    st.header("🎮 Guessing Game")
    st.write("""
    The **Guessing Game** mode lets you guess a random number between 1 and 100.
    - **Hint**: The app tells you if your guess is too high or too low.
    - **Example**: If the number is `42`, guessing `50` will return "📉 Too high!"
    """)
    st.code("""
    def guessing_game(number, guess):
        if guess == number:
            return "🎉 Correct! You found the number!"
        elif guess > number:
            return "📉 Too high! Try again."
        else:
            return "📈 Too low! Try again."
    """, language="python")
    
    st.markdown("---")
    
    # Tree Fractal Explanation
    st.header("🌳 Tree Fractal")
    st.write("""
    The **Tree Fractal** mode draws a recursive tree fractal.
    - **Logic**: Each branch splits into two smaller branches.
    - **Example**: A depth of `5` creates a complex tree structure.
    """)
    st.code("""
    def draw_tree(ax, x, y, angle, depth):
        if depth == 0:
            return
        x2 = x + np.cos(np.radians(angle)) * depth * 5
        y2 = y + np.sin(np.radians(angle)) * depth * 5
        ax.plot([x, x2], [y, y2], 'g', linewidth=depth / 2)
        draw_tree(ax, x2, y2, angle - 20, depth - 1)
        draw_tree(ax, x2, y2, angle + 20, depth - 1)
    """, language="python")
    
    st.markdown("---")
    
    # Recursive Puzzle Explanation
    st.header("🧩 Recursive Puzzle Challenge")
    st.write("""
    The **Recursive Puzzle Challenge** mode solves a recursive puzzle step-by-step.
    - **Logic**: Each step reduces the problem size until the base case is reached.
    - **Example**: Solving `n=5` requires solving `n=4`, `n=3`, etc.
    """)
    st.code("""
    def recursive_puzzle(n):
        if n == 1:
            return "🎉 Congratulations! You've solved the recursion challenge!"
        return f"🔄 Solve this recursive step first: {n-1}"
    """, language="python")
    
    st.markdown("---")
    
    # Fibonacci Visualization Explanation
    st.header("🌀 Fibonacci Visualization")
    st.write("""
    The **Fibonacci Visualization** mode draws the Fibonacci spiral.
    - **Logic**: Each term is the sum of the two preceding ones.
    - **Example**: `[1, 1, 2, 3, 5]` creates a spiral with 5 terms.
    """)
    st.code("""
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    """, language="python")
    
    st.markdown("---")
    
    # Merge Sort Explanation
    st.header("📊 Merge Sort")
    st.write("""
    The **Merge Sort** mode sorts an array using the merge sort algorithm.
    - **Logic**: Divide the array into halves, sort each half, and merge them.
    - **Example**: `[5, 3, 8, 1]` becomes `[1, 3, 5, 8]`.
    """)
    st.code("""
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr
    """, language="python")
    
    st.markdown("---")
    
    # Permutations Explanation
    st.header("🔀 Permutations")
    st.write("""
    The **Permutations** mode generates all permutations of a set using recursion.
    - **Logic**: Swap elements to generate all possible arrangements.
    - **Example**: `[a, b, c]` has `6` permutations.
    """)
    st.code("""
    def permutations(arr):
        if len(arr) == 1:
            return [arr]
        result = []
        for i in range(len(arr)):
            first = [arr[i]]
            rest = arr[:i] + arr[i+1:]
            for p in permutations(rest):
                result.append(first + p)
        return result
    """, language="python")
    
    st.markdown("---")
    
    # Footer
    st.write("""
    ### 📚 Further Reading
    - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
    - [Fibonacci Sequence (Wikipedia)](https://en.wikipedia.org/wiki/Fibonacci_number)
    - [Merge Sort (GeeksforGeeks)](https://www.geeksforgeeks.org/merge-sort/)
    """)

elif option == "Power":
    base = st.number_input("Enter base:", step=1)
    exp = st.number_input("Enter exponent:", min_value=0, step=1)
    if st.button("Calculate Power"):
        st.success(f"{int(base)}^{int(exp)} = {power(int(base), int(exp))}")

elif option == "Prime Check":
    num = st.number_input("Enter a number:", min_value=0, step=1)
    if st.button("Check Prime"):
        if is_prime(int(num)):
            st.success(f"{int(num)} is a prime number.")
        else:
            st.error(f"{int(num)} is not a prime number.")

elif option == "Guessing Game":
    number = random.randint(1, 100)
    guess = st.number_input("Guess a number (1-100):", min_value=1, max_value=100, step=1)
    if st.button("Check Guess"):
        st.write("⏳ Time to guess!")
        countdown_placeholder = st.empty()
        for i in range(5, 0, -1):  # Countdown timer
            countdown_placeholder.write(f"Time left: {i} seconds")
            time.sleep(1)
        
        # Check if the guess is close
        diff = abs(number - int(guess))
        if diff == 0:
            result = "🎉 Correct! You found the number!"
        elif diff <= 10:
            result = "🔥 Hot! You're really close!"
        else:
            result = "❄️ Cold! Try again."
        
        st.success(result)
        if "Correct" in result:
            st.balloons()

elif option == "Tree Fractal":
    depth = st.slider("Select Recursion Depth (1-10):", min_value=1, max_value=10, value=5)
    st.write(f"**Recursion Depth:** {depth}")
    st.write("Each branch splits into two smaller branches, demonstrating how recursion builds complexity.")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-50, 50)
    ax.set_ylim(0, 100)
    ax.axis("off")
    draw_tree(ax, 0, 10, 90, depth)
    st.pyplot(fig)
    plt.close()

elif option == "Recursive Puzzle Challenge":
    num = st.number_input("Enter a challenge level (1-10):", min_value=1, max_value=10, step=1)
    if st.button("Start Challenge"):
        st.info(recursive_puzzle(num))

elif option == "Fibonacci Visualization":
    st.write("## 🌟 Golden Spiral Visualization")
    n_terms = st.slider("Number of terms:", 1, 15, 5)
    
    if st.button("Generate Spiral"):
        fib_sequence = generate_golden_spiral(n_terms)
        fig = plot_golden_spiral(fib_sequence)
        st.pyplot(fig)
        plt.close()
        
        # Bonus: Display Fibonacci sequence
        st.write("**Fibonacci Sequence:**", fib_sequence)
         
elif option == "Merge Sort":
    arr = st.text_input("Enter numbers separated by commas (e.g., 5, 3, 8, 1):")
    if st.button("Sort"):
        arr = list(map(int, arr.split(',')))
        st.write("Original Array:", arr)
        sorted_arr = merge_sort(arr)
        st.write("Sorted Array:", sorted_arr)

elif option == "Permutations":
    st.write("**Recursive Permutations**")
    st.write("Generate all permutations of a set using recursion.")
    elements = st.text_input("Enter elements separated by commas (e.g., a, b, c):")
    if st.button("Generate Permutations"):
        elements = elements.split(',')
        perms = permutations(elements)
        st.write("All Permutations:")
        for p in perms:
            st.write(p)

st.sidebar.markdown("**Created by Paing Htoo 🚀**")
