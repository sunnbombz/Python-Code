# BACKEND TELEMETRY CHALLENGE 1

player_state = {
    "username": "ShadowByte99",
    "Health": 100,
    "XP": 1450,
    "Weapon": "Plasma Rifle",
    "Rank" : "Gold II",
    "Is_Online" : True,
    "Guild" : "Is in Guild",
    }

def print_hud(player):
    print("\t--- PLAYER HUD ---")
    print("\tUser:", player["username"])
    print("\tHealth:", player["Health"])
    print("\tXP:", player["XP"])
    print("\tRank:", player["Rank"])
    print("\tWeapon:", player["Weapon"])
    verd = player_state.get("Guild", "No Guild")
    print(f"\t{verd}")
    print("------------------------------------------")

#print_hud(player_state)
#player_state["Health"] += 50
#player_state["XP"] -= 100
#print_hud(player_state)

# API LATENCY MONITOR CHALLENGE 2

endpoint_latency_dict = {
    "/api/login": 120,
    "/api/users": 85,
    "/api/orders" : 340,
    "/api/payments" : 410,
    "/api/health" : 15
}

def audit_endpoints(metrics):
    print(" --- API LATENCY AUDIT ---")
    counter = 0
    leng = len(metrics.items())
    for endpoint, latency in metrics.items():
        if latency > 200:
            print(f"Checking: {endpoint} -> {latency} [SLOW]")
        else:
            print(f"Checking: {endpoint} -> {latency} [OK]")
            counter +=1
    print(f"Passed: {counter} of {leng} endpoints within target.")
    

#audit_endpoints(endpoint_latency_dict)

def get_average_latency(metrics):
    total = 0
    leng = len(metrics.items())
    for value in metrics.values():
        total += value
    average = total / leng
    return average


print(get_average_latency(endpoint_latency_dict))
