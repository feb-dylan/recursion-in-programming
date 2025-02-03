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
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

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
    fib_sequence = [fibonacci(i) for i in range(n)]
    return fib_sequence  

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
    "Factorial", "Power", "Prime Check", "Guessing Game", 
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
        plt.close()

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
    num = st.number_input("Enter number of terms:", min_value=1, step=1)
    if st.button("Generate Fibonacci"):
        fib_sequence = fibonacci_spiral(int(num))
        
        fig, ax = plt.subplots()
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 20)
        ax.set_aspect('equal', 'box')
        ax.axis('off')

        # Animation function
        def animate(i):
            ax.clear()
            ax.set_xlim(0, 20)
            ax.set_ylim(0, 20)
            ax.set_aspect('equal', 'box')
            ax.axis('off')
            fib_seq = fibonacci_spiral(i)
            x, y = 0, 0
            for j in range(len(fib_seq)):
                ax.plot([x, x + fib_seq[j]], [y, y], color='blue')
                x += fib_seq[j]

        ani = animation.FuncAnimation(fig, animate, frames=range(1, len(fib_sequence) + 1), interval=1000, repeat=False)
   
        st.pyplot(fig)
        plt.close()

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
