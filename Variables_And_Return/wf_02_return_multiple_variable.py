def measure():
    """Measure Temparature and humidity"""

    print("Begain measure...")
    temp = 39
    wetness =50
    print("measure over!")

    # when return multiple variable
    return temp, wetness

# Notice: this way is very inconvenient
result = measure()
print(result)

# new way: use two variable to accept this tuple
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)