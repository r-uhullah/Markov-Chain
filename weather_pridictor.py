weather_chain = {
    "sun": [["sun", "rain"], [9, 1]],
    "rain": [["sun", "rain"], [1, 1]],
}

# print(weather_chain.keys())
current_weather = random.choice(list(weather_chain))
weather_list = [current_weather]

for _ in range(100):
    states, weights = weather_chain[current_weather]
    current_weather = random.choices(states, weights=weights, k=1)[0]
    weather_list.append(current_weather)

sun = 0
rain = 0

for weather in weather_list:
    if weather == "sun":
        sun += 1
    else:
        rain += 1

print(f"Sunny Days: {sun} - Rainy Days: {rain}")
