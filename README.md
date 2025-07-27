# 🌌 Galaxy Calculator: Doppler Effect & Hubble's Law
A Python-based interactive tool that estimates **redshift**, **velocity**, and **distance** of galaxies using the **relativistic Doppler effect** and **Hubble’s Law**. Ideal for physics or astronomy students interested in applying spectral analysis to real-world astrophysics.

---

## 🧪 Features
- Calculate **spectral shift** (`z`) based on observed vs. rest frequency or wavelength.
- Estimate a galaxy's **recessional velocity** using the relativistic Doppler formula.
- Calculate **cosmological distances** (in Mpc, km, or m) using Hubble's Law.
- User-friendly input handling and custom galaxy naming.

---

## 📦 Requirements

- Python 3.x  
No external libraries required.

---

## 🚀 How to Use

1. **Run the script** in any Python environment:
    
   ```bash
   python3 galaxycalculator.py
   ```
    
2. Follow the prompts:
    - Choose what you want to calculate: 'spectral shift', 'velocity', or 'distance'.
    - Select your input type: 'wavelength' or 'frequency'.
    - Enter the required values (in the given units).

3. Get results:
    - Redshift is shown with direction (redshift or blueshift).
    - Velocity shows if the galaxy is moving towards or away from Earth.
    - Distance can be converted to Mpc, km, or m.

---

## 📖 Example
<pre> ```
Hi! Welcome to the galaxy calculator.
What galaxy are we looking at today? Andromeda
Please select what you would like to calculate:
'spectral shift', 'velocity', 'distance' velocity
Would you like to proceed using wavelength or frequency? frequency
Enter frequency in laboratory conditions (in Hz): 4.57e14
Enter observed frequency (in Hz): 4.53e14

Velocity = 2.63e+06 m/s
Andromeda galaxy is travelling away from Earth with a speed of 2630000.0 m/s. ``` </pre>

---

## 🧮 Scientific Basis

`c = 3.00 × 10^8 m/s`

Spectral Shift:
    `z = ((c / f_obs) - (c / f)) / (c / f)`

Recession Velocity:
    `v = c × ((1 - (f_obs / f)^2) / (1 + (f_obs / f)^2))`

Distance using Hubble's Law:
    `d = |v| / H₀` (Hubble's constant H0 averaged between 69.8 and 73 km/s/Mpc)

---

## 🛠️ Improvements You Could Add
- GUI version (Tkinter or Streamlit)
- Input from real galaxy databases (e.g., SDSS)
- Support for plotting redshift-distance graphs

---

## 📄 License
MIT License — feel free to modify and use with credit.

---

## 👩‍🚀 Author
Developed by Yuchu Wang
