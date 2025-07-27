print("Hi! Welcome to the galaxy calculator.")
name = input("What galaxy are we looking at today? ")

# Important constants to define:
c = 3.00*10**8 # Speed of Light in vacuum, unit: m/s
Ho = (69.8 + 73)/2 # Hubble's Constant, unit: km/s/Mpc

while True:
    idot = input("Please select what you would like to calculate: \n'spectral shift', 'velocity', 'distance'").strip().lower()
    if idot in ('spectral shift', 'velocity', 'distance'):
        print("Got it!\n")
        break
    else:
        print("Invalid input. Please enter one of the options from above.")
        continue
        
while True:
    x = input("Would you like to proceed using wavelength or frequency? ").strip().lower()
    if x in ("wavelength", "frequency"):
        break
    else:
        print("Invalid input. Please enter 'wavelength' or 'frequency'.")
        continue

if x == "wavelength":  
    while True:
        restWave = input("Enter wavelength in laboratory conditions (in m): ").strip()
        wave = input("Enter observed wavelength (in m): ").strip()
        try:
            restWave = float(restWave)
            wave = float(wave)
            f = c/restWave
            fobs = c/wave
            break
        except: 
            print("Invalid input. Please enter numbers.")
            continue

elif x == "frequency":
    while True:
        f = input("Enter frequency in laboratory conditions (in Hz): ").strip()
        fobs = input("Enter observed frequency (in Hz): ").strip()
        try: 
            f = float(f)
            fobs = float(fobs)
            break
        except: 
            print("Invalid input. Please enter numbers.")
            continue

if idot == "spectral shift":
# Calculate the spectral shift using wavelength or frequency.
    z = ((c/fobs)-(c/f))/(c/f)
    if z > 0: 
        print("Redshift, z =", z)
    elif z < 0:
        print("Blueshift, z =", z)
    else: 
        print("Invalid: No shift detected.")
        quit()
    
    print("All done!")
    quit()

# Calculate the galaxy's velocity:
# v is defined as the velocity with which the galaxy is travelling away from Earth.
if idot in ("velocity", "distance"):   
    v = c * ((1-((fobs/f)**2))/(1+((fobs/f)**2)))
    if idot == "velocity":
        if v > 0:
            print("\nVelocity =", v, "m/s")
            print(name, "galaxy is travelling away from Earth with a speed of", v, "m/s.")
        elif v < 0:
            print("\nVelocity =", v, "m/s")
            print(name, "galaxy is travelling towards Earth with a speed of", abs(v), "m/s.")
        print("All done!")
        quit()
    
    elif idot == "distance":
    # Calculate the approximate distance using Hubble's law:
        v = v/1000.0
        d = abs(v)/Ho
        print("The distance between Earth and", name, "galaxy is", d, "Mpc.")
        while True:
            yn = input("\nWould you like that value in a different unit? ").strip().lower()
            if yn == "yes":
                while True:
                    unit = input("Got it! Please choose your preferred unit: m or km \n")
                    if unit == "m":
                        d = d * 3.09 * 10**22
                        print("\nDistance in metres:", d)
                        break
                    elif unit == "km":
                        d = d * 3.09 * 10**19
                        print("Distance in kilometres:", d)
                        break
                    else: 
                        print("Please enter either m or km.") 
                        continue
                print("\nAll done!")
                break
            elif yn == "no": 
                print("All done!")
                break
            else:
                print("Please enter either yes or no.")
                continue
        quit()
                
        