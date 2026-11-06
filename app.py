"""Interactive web interface for the collaborative Git calculator."""
import streamlit as st

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    square,
    power,
    square_root,
    cube_root,
)

# Reuse the original calculation functions from calculator.py.
# Each entry specifies the callable and how many numbers it needs.
OPERATIONS = {
    "Addition": (add, 2),
    "Subtraction": (subtract, 2),
    "Multiplication": (multiply, 2),
    "Division": (divide, 2),
    "Square": (square, 1),
    "Power": (power, 2),
    "Square Root": (square_root, 1),
    "Cube Root": (cube_root, 1),
}

st.set_page_config(
    page_title="Git Practice Calculator",
    page_icon="🧮",
    layout="centered",
)

st.title("🧮 Git Practice Calculator")
st.write("Choose an operation, enter your number(s), and calculate.")
st.caption("A collaborative Python project powered by Streamlit.")
st.divider()

if "selected_operation" not in st.session_state:
    st.session_state.selected_operation = "Addition"

if "last_result" not in st.session_state:
    st.session_state.last_result = None

st.subheader("Choose an operation")

# Buttons are generated automatically from the registered operations.
columns = st.columns(2)
for index, name in enumerate(OPERATIONS):
    with columns[index % 2]:
        if st.button(name, key=f"operation_{name}", use_container_width=True):
            st.session_state.selected_operation = name
            st.session_state.last_result = None

operation = st.session_state.selected_operation
function, input_count = OPERATIONS[operation]

st.info(f"Selected operation: {operation}")

first_number = st.number_input("First number", value=0.0)

if input_count == 2:
    second_number = st.number_input("Second number", value=0.0)

if st.button("Calculate", type="primary", use_container_width=True):
    try:
        if input_count == 2:
            result = function(first_number, second_number)
        else:
            result = function(first_number)

        st.session_state.last_result = (True, result)
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        st.session_state.last_result = (False, str(error))

if st.session_state.last_result is not None:
    success, outcome = st.session_state.last_result
    if success:
        st.success(f"Result: {outcome:.12g}")
    else:
        st.error(outcome)

st.divider()
st.caption("Built for learning Git, Python, pull requests, and deployment.")
